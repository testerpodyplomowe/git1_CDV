import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

email = "tester@mailinator.com"
name = "Janeczek"

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def testLogin(self):
        signin_btn = self.driver.find_element_by_class_name("login")
        signin_btn.click()
        email_input = self.driver.find_element_by_id("email")
        email_input.send_keys(email)
        passwd_input = self.driver.find_element_by_id("passwd")
        passwd_input.send_keys(password)
        create_btn = self.driver.find_element_by_name("SubmitLogin")
        create_btn.click()

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)