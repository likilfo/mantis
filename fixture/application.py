from selenium import webdriver
from .session import SessionHelper
from .project import ProjectHelper
from .soap import SoapHelper


class Application:

    def __init__(self, browser, url, user, password):
        if browser == 'firefox':
            self.wd = webdriver.Firefox(
                executable_path=r'C:\Windows\SysWOW64\geckodriver.exe')
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError('Unrecognized browser %s' % browser)
        self.wd.implicitly_wait(2)
        self.user = user
        self.password = password
        self.url = url
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.soap = SoapHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get(self.url)


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()
