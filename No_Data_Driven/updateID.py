import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
baseUrl = "https://mybk.hcmut.edu.vn/stinfo/"
id = "352611458"
place = "Tỉnh An Giang"
date = "06/12/2016"


class TestUpdateID(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://mybk.hcmut.edu.vn/my/logoutSSO.action")
        self.driver.get(
            'https://sso.hcmut.edu.vn/cas/login?service=https://mybk.hcmut.edu.vn/my/homeSSO.action')
        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")
        submitBtn = self.driver.find_element(By.NAME, "submit")

        username.send_keys("tan.lamcs1001")
        password.send_keys("lnt@H1720")
        submitBtn.click()

    def get_element_wait(self, element_id, timeout=3):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.ID, element_id))
            )
        except TimeoutException:
            err = 'Element with id {} could not be found!'
            raise Exception(err.format(element_id))

    def test_1(self):
        self.driver.get(baseUrl)
        time.sleep(3)
        self.driver.find_element(
            By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div/div[1]/a/div').click()
        time.sleep(10)

        self.driver.find_element(By.ID, "menu-cmnd-edit").click()
        time.sleep(5)

        idObj = self.driver.find_element(By.ID, "cmndEditCMND")
        placeObj = self.driver.find_element(By.ID, "cmndnoicapEditCMND")
        dateObj = self.driver.find_element(By.ID, "cmndngaycapEditCMND")

        idObj.click()
        idObj.send_keys(Keys.CONTROL + "a")
        idObj.send_keys(Keys.DELETE)

        placeObj.click()
        placeObj.send_keys(Keys.CONTROL + "a")
        placeObj.send_keys(Keys.DELETE)

        dateObj.click()
        dateObj.send_keys(Keys.CONTROL + "a")
        dateObj.send_keys(Keys.DELETE)

        idObj.send_keys(id)
        placeObj.send_keys(place)
        dateObj.send_keys(date)

        idObj = self.driver.find_element(By.ID, "cmndEditCMND")
        placeObj = self.driver.find_element(By.ID, "cmndnoicapEditCMND")
        dateObj = self.driver.find_element(By.ID, "cmndngaycapEditCMND")
        time.sleep(1)

        self.driver.find_element(By.ID, "btn_save_cmnd").click()
        time.sleep(5)

        print(self.driver.find_element(
            By.CLASS_NAME, 'bootbox-body').text)

    def test_2(self):
        self.driver.get(baseUrl)
        time.sleep(3)
        self.driver.find_element(
            By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div/div[1]/a/div').click()
        time.sleep(10)

        self.driver.find_element(By.ID, "menu-cmnd-edit").click()
        time.sleep(5)
        idObj = self.driver.find_element(By.ID, "cmndEditCMND")
        placeObj = self.driver.find_element(By.ID, "cmndnoicapEditCMND")
        dateObj = self.driver.find_element(By.ID, "cmndngaycapEditCMND")

        idObj.click()
        idObj.send_keys(Keys.CONTROL + "a")
        idObj.send_keys(Keys.DELETE)

        placeObj.click()
        placeObj.send_keys(Keys.CONTROL + "a")
        placeObj.send_keys(Keys.DELETE)

        dateObj.click()
        dateObj.send_keys(Keys.CONTROL + "a")
        dateObj.send_keys(Keys.DELETE)

        idObj.send_keys("")
        placeObj.send_keys(place)
        dateObj.send_keys(date)

        idObj = self.driver.find_element(By.ID, "cmndEditCMND")
        placeObj = self.driver.find_element(By.ID, "cmndnoicapEditCMND")
        dateObj = self.driver.find_element(By.ID, "cmndngaycapEditCMND")
        time.sleep(1)

        self.driver.find_element(By.ID, "btn_save_cmnd").click()
        time.sleep(5)

        print(self.driver.find_element(
            By.XPATH, '//*[@id="editcmndForm"]/div[1]/div/div[3]/div[1]/div/ul/li').text)

    def test_3(self):
        self.driver.get(baseUrl)
        time.sleep(3)
        self.driver.find_element(
            By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div/div[1]/a/div').click()
        time.sleep(10)

        self.driver.find_element(By.ID, "menu-cmnd-edit").click()
        time.sleep(5)
        idObj = self.driver.find_element(By.ID, "cmndEditCMND")
        placeObj = self.driver.find_element(By.ID, "cmndnoicapEditCMND")
        dateObj = self.driver.find_element(By.ID, "cmndngaycapEditCMND")

        idObj.click()
        idObj.send_keys(Keys.CONTROL + "a")
        idObj.send_keys(Keys.DELETE)

        placeObj.click()
        placeObj.send_keys(Keys.CONTROL + "a")
        placeObj.send_keys(Keys.DELETE)

        dateObj.click()
        dateObj.send_keys(Keys.CONTROL + "a")
        dateObj.send_keys(Keys.DELETE)

        idObj.send_keys(id)
        placeObj.send_keys("")
        dateObj.send_keys(date)

        idObj = self.driver.find_element(By.ID, "cmndEditCMND")
        placeObj = self.driver.find_element(By.ID, "cmndnoicapEditCMND")
        dateObj = self.driver.find_element(By.ID, "cmndngaycapEditCMND")
        time.sleep(1)

        self.driver.find_element(By.ID, "btn_save_cmnd").click()
        time.sleep(5)

        print(self.driver.find_element(
            By.XPATH, '//*[@id="editcmndForm"]/div[1]/div/div[3]/div[2]/div/ul/li').text)

    def test_4(self):
        self.driver.get(baseUrl)
        time.sleep(3)
        self.driver.find_element(
            By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div/div[1]/a/div').click()
        time.sleep(10)

        self.driver.find_element(By.ID, "menu-cmnd-edit").click()
        time.sleep(5)
        idObj = self.driver.find_element(By.ID, "cmndEditCMND")
        placeObj = self.driver.find_element(By.ID, "cmndnoicapEditCMND")
        dateObj = self.driver.find_element(By.ID, "cmndngaycapEditCMND")

        idObj.click()
        idObj.send_keys(Keys.CONTROL + "a")
        idObj.send_keys(Keys.DELETE)

        placeObj.click()
        placeObj.send_keys(Keys.CONTROL + "a")
        placeObj.send_keys(Keys.DELETE)

        dateObj.click()
        dateObj.send_keys(Keys.CONTROL + "a")
        dateObj.send_keys(Keys.DELETE)

        idObj.send_keys(id)
        placeObj.send_keys(place)
        dateObj.send_keys("")

        idObj = self.driver.find_element(By.ID, "cmndEditCMND")
        placeObj = self.driver.find_element(By.ID, "cmndnoicapEditCMND")
        dateObj = self.driver.find_element(By.ID, "cmndngaycapEditCMND")
        time.sleep(1)

        self.driver.find_element(By.ID, "btn_save_cmnd").click()
        time.sleep(5)

        print(self.driver.find_element(
            By.XPATH, '//*[@id="editcmndForm"]/div[1]/div/div[3]/div[3]/div/ul/li').text)

    def test_5(self):
        self.driver.get(baseUrl)
        time.sleep(3)
        self.driver.find_element(
            By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div/div[1]/div/div[1]/a/div').click()
        time.sleep(10)

        self.driver.find_element(By.ID, "menu-cmnd-edit").click()
        time.sleep(5)
        idObj = self.driver.find_element(By.ID, "cmndEditCMND")
        placeObj = self.driver.find_element(By.ID, "cmndnoicapEditCMND")
        dateObj = self.driver.find_element(By.ID, "cmndngaycapEditCMND")

        idObj.click()
        idObj.send_keys(Keys.CONTROL + "a")
        idObj.send_keys(Keys.DELETE)

        placeObj.click()
        placeObj.send_keys(Keys.CONTROL + "a")
        placeObj.send_keys(Keys.DELETE)

        dateObj.click()
        dateObj.send_keys(Keys.CONTROL + "a")
        dateObj.send_keys(Keys.DELETE)

        idObj.send_keys("")
        placeObj.send_keys("")
        dateObj.send_keys("")

        idObj = self.driver.find_element(By.ID, "cmndEditCMND")
        placeObj = self.driver.find_element(By.ID, "cmndnoicapEditCMND")
        dateObj = self.driver.find_element(By.ID, "cmndngaycapEditCMND")
        time.sleep(1)

        self.driver.find_element(By.ID, "btn_save_cmnd").click()
        time.sleep(5)

        print(self.driver.find_element(
            By.XPATH, '//*[@id="editcmndForm"]/div[1]/div/div[3]/div[1]/div/ul/li').text)

    def teardown_method(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
