import pytest
from fixture.application import Application
from pathlib import Path
import yaml
from model.project import Project

fixture = None
config = None

def load_config(config_file):
    global config
    root_path = Path(__file__).parent.absolute()
    if config is None:
        with open(root_path / config_file) as fp:
            config = yaml.load(fp.read())
    return config


@pytest.fixture
def app(request):
    global fixture
    web_config = load_config(request.config.getoption('--config'))['web']
    browser = request.config.getoption('--browser')
    if not fixture or not fixture.is_valid():
        fixture = Application(browser=browser, url=web_config['baseUrl'],
                              user=web_config['username'], password=web_config['password'])
    fixture.session.ensure_login()
    return fixture


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return app

@pytest.fixture
def create_group(app):
    fixture.project.create(Project(name=fixture.project.random_string(),
                                         description=fixture.project.random_string()))
    return app.soap.get_project_list()


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--config', action='store', default='config.yaml')




