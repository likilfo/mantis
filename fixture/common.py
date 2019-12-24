from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import rstr


class CommonHelper:

    def fill_fields(self, model_part):
        wd = self.wd
        for key, value in model_part.__dict__.items():
            if value:
                wd.find_element_by_name(key).click()
                wd.find_element_by_name(key).clear()
                wd.find_element_by_name(key).send_keys(value)

    def wait_for(self, path):
        try:
            WebDriverWait(self.wd, 10).until(
                EC.presence_of_element_located((By.XPATH, path))
            )
            return True
        except:
            return False

    def random_string(self):
        return rstr.xeger('[A-Za-z1-9 ]{3,15}')

    def random_phone(self):
        return rstr.xeger(r'(\+)?[0-9 ]{10,12}')

    def random_email(self):
        return rstr.xeger(r'[A-Za-z0-9]{3,10}@[a-z]{3,5}\.[a-z]{2,3}')

    def random_address(self):
        return rstr.xeger(r'[0-9A-Za-z\n ]{10,24}')

