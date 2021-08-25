# Importamos selenium webdriver
from selenium import webdriver
import unittest

class ImplicitWaits(unittest.TestCase):

    def setUp(self):
        # Preconditions
        self.driver = webdriver.Chrome(executable_path="drivers/chromedriver")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.maximize_window()
        # Configuramos la espera implicita
        self.driver.implicitly_wait(time_to_wait=10) # Configurado para esperar 10 seg

    def test_login_page(self):
        # Verificar que estamos en el login page
        title_login_page = self.driver.title
        self.assertEqual(title_login_page, "OrangeHRM")

    def test_validate_login(self):
        # Hacer login en la app
        username = self.driver.find_element_by_id("txtUsername")
        password = self.driver.find_element_by_id("txtPassword")
        username.send_keys("Admin")
        password.send_keys("admin123")
        login_btn = self.driver.find_element_by_id("btnLogin")
        login_btn.click()
        # Verificamos que hicimos login consultando la clase menu ppal
        main_menu = self.driver.find_element_by_id("mainMenu")
        self.assertTrue(main_menu.is_displayed(), msg="WARNING: El login fallo")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
        unittest.main()