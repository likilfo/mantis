from suds.client import Client
from .project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app


    def get_project_list(self):
        client = Client(self.app.url + 'api/soap/mantisconnect.php?wsdl')
        actual_projects = []
        projects = client.service.mc_projects_get_user_accessible\
            (self.app.user, self.app.password)
        for project in projects:
            actual_projects.append(Project(name=project.name, description=project.description))
        return actual_projects
