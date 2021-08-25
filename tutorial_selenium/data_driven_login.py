# Importamos la dependencia ddt, data y file_data
from ddt import ddt, data, file_data
# Importamos la dependencia de selenium webdriver
from selenium import webdriver
# Importamos la dependencia unittest
import unittest
# Importamos la dependencia HtmlTestRunner
import HtmlTestRunner

@ddt
class DataDrivenLogin(unittest.TestCase):

    def setUp(self):
        # Preconditions
        self.driver = webdriver.Chrome(executable_path="drivers/chromedriver")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

    @file_data("data_login.json")
    def test_validate_login(self, value_username, value_password):
        # Hacer login en la app
        username = self.driver.find_element_by_id("txtUsername")
        password = self.driver.find_element_by_id("txtPassword")
        username.send_keys(value_username)
        password.send_keys(value_password)
        login_btn = self.driver.find_element_by_id("btnLogin")
        login_btn.click()
        # Verificamos que hicimos login consultando la clase menu ppal
        main_menu = self.driver.find_element_by_id("mainMenu")
        self.assertTrue(main_menu.is_displayed(), msg="WARNING: El login fallo")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/Users/augusto607/Documents/Learning/QA/Python_Selenium_WebDriver/tutorial_selenium/reports'))