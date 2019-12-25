

class SessionHelper:

    def __init__(self, app):
        self.app = app
        self.app.open_home_page()

    def login(self, login, password):
        wd = self.app.wd
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(login)
        wd.find_element_by_xpath('//*[@value="Войти"]').click()
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_xpath('//*[@value="Войти"]').click()


    def is_logged_in(self):
        return len(self.app.wd.find_elements_by_xpath
                   ("//*[@class='fa fa-edit']")) > 0

    def is_logged_in_as(self, user):
        return self.app.wd.find_element_by_xpath\
                   ("//*[@class='user-info']").text == user

    def logout(self):
        for attemtp in range(2):
            try:
                self.app.wd.find_element_by_link_text("Logout").click()
            except:
                pass

    def ensure_logout(self):
        if len(self.app.wd.find_elements_by_link_text("Logout")) > 0:
            self.logout()

    def ensure_login(self):
        if self.is_logged_in():
            if not self.is_logged_in_as(self.app.user):
                self.logout()
                self.login(self.app.user, self.app.password)
        else:
            self.login(self.app.user, self.app.password)