from selenium.webdriver.support.select import Select

from Locator.Login import Login
class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.username = Login.username
        self.password = Login.password
        self.button_login = Login.button_login

    def input_username(self, username):
        self.driver.find_element_by_xpath(self.username)
        self.driver.find_element_by_xpath(self.username).send_keys(username)

    def input_password(self, password):
        self.driver.find_element_by_xpath(self.password)
        self.driver.find_element_by_xpath(self.password).send_keys(password)

    def click_button_login(self):
        self.driver.find_element_by_xpath(self.button_login).click()