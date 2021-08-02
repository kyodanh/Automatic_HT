from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys

class Excuteticket_1(unittest.TestCase):

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
        driver.find_element_by_xpath("//*[@id='login_with_account']/div[1]/input")
        driver.find_element_by_xpath("//*[@id='login_with_account']/div[1]/input").send_keys("create2")
        time.sleep(0.3)
        driver.find_element_by_xpath("//*[@id='login_with_account']/div[2]/input")
        driver.find_element_by_xpath("//*[@id='login_with_account']/div[2]/input").send_keys("123456789")
        time.sleep(0.3)
        driver.find_element_by_xpath("//*[@id='login_with_account']/div[4]/div/button").click()

    def test_3_checklogin(self):
        driver = self.driver
        time.sleep(0.3)
        banner = driver.find_element_by_xpath("//*[@id='welcome_text_content']").text
        if banner == "Chào mừng đến với hệ thống eOffice, chúng tôi có thể hỗ trợ bạn vấn đề gì?":
            print("Login Thành Công")
        else:
            print("Login không thành công")

    def test_4_clickmenu(self):
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='user_approvals']").click()

    def test_5_clicktikcet(self):
        driver = self.driver
        driver.find_element_by_css_selector("[title='test']").click()


    def test_6_scroll(self):
        driver = self.driver
        time.sleep(0.8)
        driver.switch_to.window(driver.window_handles[1])
        # chuyển đổi qua tab mới để focus
        driver.execute_script("window.scrollTo(0, 500)")
        driver.find_element_by_xpath("//*[@id='smsBeginImplementBtn']").click()
        




    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        # cls.driver.quit()
        print("Complete")
