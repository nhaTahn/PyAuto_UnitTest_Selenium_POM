import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


class TestCreateTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def get_element_wait(self, element_id, timeout=3):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.ID, element_id))
            )
        except TimeoutException:
            err = 'Element with id {} could not be found!'
            raise Exception(err.format(element_id))
    
    def first_step(self):
        self.driver.get('https://sso.hcmut.edu.vn/cas/login?service=https%3A%2F%2Fe-learning.hcmut.edu.vn%2Flogin%2Findex.php%3FauthCAS%3DCAS')

        self.driver.find_element(By.NAME,"username").send_keys("010010")
        self.driver.find_element(By.NAME,"password").send_keys("123456")
        self.driver.find_element(By.NAME,"submit").click()
        time.sleep(2)

        self.driver.get('https://e-learning.hcmut.edu.vn/course/modedit.php?update=73403&return=1')
        time.sleep(1)

        self.driver.find_element(By.ID, 'collapseElement-1').click()
        time.sleep(5)
    
    def test_1(self): 
        self.first_step()

        self.driver.execute_script("arguments[0].setAttribute('value','test1')", self.driver.find_element(By.ID, 'id_name'))

        self.driver.find_element(By.ID,"id_submitbutton2").click()
        time.sleep(5)

        self.driver.find_element(By.ID,'topofscroll')
    
    def test_2(self): 
        self.first_step()

        self.driver.execute_script("arguments[0].setAttribute('value','')", self.driver.find_element(By.ID, 'id_name'))

        self.driver.find_element(By.ID,"id_submitbutton2").click()
        time.sleep(5)

        self.driver.find_element(By.ID,'id_error_name')

    def test_3(self): 
        self.first_step()

        self.driver.execute_script("arguments[0].setAttribute('value','test3')", self.driver.find_element(By.ID, 'id_name'))

        self.driver.find_element(By.ID, 'id_timeopen_enabled').click()
        self.driver.find_element(By.ID,"id_submitbutton2").click()
        time.sleep(5)

        self.driver.find_element(By.ID,'topofscroll')

    def test_4(self): 
        self.first_step()

        self.driver.execute_script("arguments[0].setAttribute('value','test4')", self.driver.find_element(By.ID, 'id_name'))

        self.driver.find_element(By.ID, 'id_timeclose_enabled').click()
        self.driver.find_element(By.ID,"id_submitbutton2").click()
        time.sleep(5)

        self.driver.find_element(By.ID,'topofscroll')

    def test_5(self): 
        self.first_step()

        self.driver.execute_script("arguments[0].setAttribute('value','test5')", self.driver.find_element(By.ID, 'id_name'))

        self.driver.find_element(By.ID, 'id_timelimit_enabled').click()
        self.driver.find_element(By.ID,"id_submitbutton2").click()
        time.sleep(5)

        self.driver.find_element(By.ID,'topofscroll')
    
    def test_6(self): 
        self.first_step()

        self.driver.execute_script("arguments[0].setAttribute('value','test6')", self.driver.find_element(By.ID, 'id_name'))

        self.driver.find_element(By.ID, 'id_timeopen_enabled').click()
        self.driver.find_element(By.ID, 'id_timeclose_enabled').click()
        self.driver.find_element(By.XPATH, '//*[@id="id_timeclose_year"]/option[text()="2000"]').click()

        self.driver.find_element(By.ID,"id_submitbutton2").click()
        time.sleep(5)

        self.driver.find_element(By.ID,'id_error_timeclose')

    def test_7(self): 
        self.first_step()

        self.driver.execute_script("arguments[0].setAttribute('value','test7')", self.driver.find_element(By.ID, 'id_name'))

        self.driver.find_element(By.ID, 'id_timelimit_enabled').click()
        self.driver.execute_script("arguments[0].setAttribute('value','-1')", self.driver.find_element(By.ID, 'id_timelimit_number'))

        self.driver.find_element(By.ID,"id_submitbutton2").click()
        time.sleep(5)

        self.driver.find_element(By.ID,'id_error_timeclose')
        
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()