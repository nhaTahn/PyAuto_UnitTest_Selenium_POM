import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def get_element_wait(self, element_id, timeout=3):
        try:
            return WebDriverWait(self.driver, timeout).until(
                # EC.presence_of_element_located((By.ID, element_id))
            )
        except TimeoutException:
            err = 'Element with id {} could not be found!'
            raise Exception(err.format(element_id))

    def test_1(self): #done
        self.driver.get('https://sso.hcmut.edu.vn/cas/login?service=https://mybk.hcmut.edu.vn/my/homeSSO.action')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("quoc.le1804")
        password.send_keys("baoquoc1804")
        submitBtn.click()
        time.sleep(2)
        logoutBtn = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/a[1]')
        logoutBtn.click()
        alert = self.driver.switch_to.alert
        time.sleep(1)
        alert.accept()
        time.sleep(1)
        loginPageBtn = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/a[1]')
        loginPageBtn.click()
        time.sleep(2)
        

    def test_2(self): #done
        self.driver.get('https://sso.hcmut.edu.vn/cas/login?service=https://mybk.hcmut.edu.vn/my/homeSSO.action')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("quoc1804")
        password.send_keys("quoc1178")
        submitBtn.click()  
        time.sleep(2)
        errorNotification = self.driver.find_element(By.XPATH,'//*[@id="msg"]')
        assert errorNotification.text == "The credentials you provided cannot be determined to be authentic."

    def test_3(self): #done
        self.driver.get('https://sso.hcmut.edu.vn/cas/login?service=https://mybk.hcmut.edu.vn/my/homeSSO.action')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("")
        password.send_keys("quocbao18")
        submitBtn.click()
        time.sleep(2)
        errorNotification = self.driver.find_element(By.XPATH,'//*[@id="msg"]')
        assert errorNotification.text == "Please enter your username."


    def test_4(self): #done
        self.driver.get('https://sso.hcmut.edu.vn/cas/login?service=https://mybk.hcmut.edu.vn/my/homeSSO.action')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("quocbao182002")
        password.send_keys("quoc12345")
        submitBtn.click()
        time.sleep(2)
        errorNotification = self.driver.find_element(By.XPATH,'//*[@id="msg"]')
        assert errorNotification.text == "The credentials you provided cannot be determined to be authentic."

    def test_5(self): #done
        self.driver.get('https://sso.hcmut.edu.vn/cas/login?service=https://mybk.hcmut.edu.vn/my/homeSSO.action')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("quoc.le1804")
        password.send_keys("")
        submitBtn.click()
        time.sleep(2)
        errorNotification = self.driver.find_element(By.XPATH,'//*[@id="msg"]')
        assert errorNotification.text == "Please enter your password."


    def test_6(self):
        self.driver.get('https://sso.hcmut.edu.vn/cas/login?service=https://mybk.hcmut.edu.vn/my/homeSSO.action')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("quocbao2002")
        password.send_keys("")
        submitBtn.click()
        time.sleep(2)
        errorNotification = self.driver.find_element(By.XPATH,'//*[@id="msg"]')
        assert errorNotification.text == "Please enter your password."

    def test_7(self):
        self.driver.get('https://sso.hcmut.edu.vn/cas/login?service=https://mybk.hcmut.edu.vn/my/homeSSO.action')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        username.send_keys("")
        password.send_keys("quoc1804")
        submitBtn.click()
        time.sleep(2)
        errorNotification = self.driver.find_element(By.XPATH,'//*[@id="msg"]')
        assert errorNotification.text == "Please enter your username."


    def test_8(self):
        self.driver.get('https://sso.hcmut.edu.vn/cas/login?service=https://mybk.hcmut.edu.vn/my/homeSSO.action')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")
        submitBtn = self.driver.find_element(By.NAME,"submit")
        submitBtn.click()
        time.sleep(2)
        assert self.driver.find_element(By.XPATH,'//*[@id="msg"]')
    

        
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()