from .common import CommonHelper
from model.project import Project


class ProjectHelper(CommonHelper):

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd

    project_list_caсhe = None

    def open_project_page(self):
        wd = self.wd
        if not wd.current_url.endswith("/manage_proj_page.php"):
            wd.find_element_by_xpath('//*[@class="menu-icon fa fa-gears"]').click()
            wd.find_element_by_link_text('Управление проектами').click()


    def is_exist(self):
        self.open_project_page()
        return len(self.wd.find_elements_by_xpath
                   ('//*[@class="table-responsive"]/table/tbody[1]/tr'))

    def create(self, project):
        wd = self.wd
        self.open_project_page()
        wd.find_element_by_xpath("//*[contains(text(), 'Создать новый проект')]").click()
        self.fill_fields(project)
        wd.find_element_by_xpath("//*[@value='Добавить проект']").click()
        self.project_list_caсhe = None
        self.wait_for("//*[contains(text(), 'Создать новый проект')]")


    def remove(self, contact_name):
        wd = self.wd
        self.open_project_page()
        wd.find_element_by_link_text(contact_name).click()
        wd.find_element_by_xpath("//*[@value='Удалить проект']").click()
        wd.find_element_by_xpath("//*[@value='Удалить проект']").click()
        self.project_list_caсhe = None
        self.wait_for("//*[contains(text(), 'Создать новый проект')]")


    def get_project_list(self):
        if self.project_list_caсhe == None:
            wd = self.wd
            self.open_project_page()
            self.project_list_caсhe = []
            tables = wd.find_elements_by_xpath('//tbody')
            for row in tables[0].find_elements_by_xpath('.//tr'):
                name = row.find_element_by_xpath('.//td[1]').text
                description =row.find_element_by_xpath('.//td[2]').text
                self.project_list_caсhe.append(Project(name=name, description=description))
        return list(self.project_list_caсhe)