# Importamos selenium webdriver
from selenium import webdriver
# Importamos de selenium la clase By
from selenium.webdriver.common.by import By
# Importamos de selenium webdriverwait
from selenium.webdriver.support.ui import WebDriverWait
# Importamos desde selenium los expected_condition
from selenium.webdriver.support import expected_conditions as EC
# Importamos el framework unittest
import unittest

class ExplicitWaits(unittest.TestCase):

    def setUp(self):
        # Preconditions
        self.driver = webdriver.Chrome(executable_path="drivers/chromedriver")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()

    def test_validate_logout(self):
        # Hacer login en la app
        username = self.driver.find_element_by_id("txtUsername")
        password = self.driver.find_element_by_id("txtPassword")
        username.send_keys("Admin")
        password.send_keys("admin123")
        login_btn = self.driver.find_element_by_id("btnLogin")
        login_btn.click()

        welcome_admin_link = self.driver.find_element(By.LINK_TEXT, "Welcome Paul")
        welcome_admin_link.click()
        wait = WebDriverWait(self.driver, 10) # Explicit Wait
        logout_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
        logout_link.click()
        # Verificamos que realmente hicimos logout
        title_login = self.driver.title
        wait.until(EC.title_contains("OrangeHRM"))
        self.assertEquals(title_login, "OrangeHRM")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()