from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys

class CreateTicket_2(unittest.TestCase):

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
        driver.find_element_by_xpath("//*[@id='login_with_account']/div[1]/input").send_keys("create1")
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

    def test_4_slide(self):
        driver = self.driver
        time.sleep(0.3)
        target = driver.find_element_by_xpath("//*[@id='544']")
        driver.execute_script("arguments[0].scrollIntoView();", target)

    def test_5_ChosseTiket(self):
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='545']").click()

    def test_6_Input(self):
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='sms-ticket-title-real']").click()
        driver.find_element_by_xpath("//*[@id='sms-ticket-title-real']").send_keys("QC_Test_Automation")
        time.sleep(0.3)
        driver.find_element_by_css_selector("a.select2-choice").click()
        driver.find_element_by_xpath("(//a[@onclick='return false;'])[4]").click()
        driver.find_element_by_xpath("//*[@id='select2-drop']/ul/li[2322]/div").click()
        driver.find_element_by_xpath("//*[@id='s2id_autogen9']/a/span[1]").click()
        driver.find_element_by_xpath("//*[@id='select2-drop']/div/input").send_keys("create1")
        driver.find_element_by_xpath("//*[@id='select2-drop']/ul/li[1]/div").click()
        driver.find_element_by_xpath("//*[@id='s2id_autogen12']/a/span[1]").click()
        driver.find_element_by_xpath("//*[@id='select2-drop']/div/input").send_keys("create1")
        driver.find_element_by_xpath("//*[@id='select2-drop']/ul/li[1]/div").click()
        driver.find_element_by_xpath("//*[@id='s2id_autogen15']").click()
        driver.find_element_by_xpath("//*[@id='s2id_autogen15']").send_keys("create1")
        driver.find_element_by_xpath("//*[@id='select2-drop']/ul/li[1]/div").click()
        driver.find_element_by_xpath("//input[@name='Số điện thoại / Line nội bộ']").click()
        driver.find_element_by_xpath("//input[@name='Số điện thoại / Line nội bộ']").send_keys("123456789")
        time.sleep(0.5)


    def test_7_Submit(self):
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='add-ticket-submit']").click()



    @classmethod
    def tearDownClass(cls):
        # cls.driver.close()
        # cls.driver.quit()
        print("Complete")
