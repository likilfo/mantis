from model.project import Project
import random


def test_add_new_project(app):
    old_projects = app.project.get_project_list()
    project = Project(name=app.project.random_string(),
                      description=app.project.random_string())
    app.project.create(project)
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.pj_name)\
           == sorted(new_projects, key=Project.pj_name)



def test_delete_project(app, create_group):
    old_projects = create_group
    project = random.choice(old_projects)
    app.project.remove(project.name)
    new_projects = app.project.get_project_list()
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.pj_name)\
           == sorted(new_projects, key=Project.pj_name)
