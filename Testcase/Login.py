from selenium import webdriver
import unittest
import time
from Page.LoginPage import LoginPage

class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="D:\pythonProject\driver\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_1_openWeb(self):
        driver = self.driver
        driver.get("https://uat-eoffice.hungthinhcorp.com.vn/")  # openwweb
        driver.set_page_load_timeout(20)
        time.sleep(0.3)

    def test_2_login(self):
        driver = self.driver
        login = LoginPage(driver)
        login.input_username("create1")
        time.sleep(0.3)
        login.input_password("123456789")
        time.sleep(0.3)
        login.click_button_login()

    def test_3_checklogin(self):
        driver = self.driver
        banner = driver.find_element_by_xpath("//*[@id='welcome_text_content']").text
        if banner == "Chào mừng đến với hệ thống eOffice, chúng tôi có thể hỗ trợ bạn vấn đề gì?":
          print("Login Thành Công")
        else:
          print("Login không thành công")


    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        # cls.driver.quit()
        print("Complete")
