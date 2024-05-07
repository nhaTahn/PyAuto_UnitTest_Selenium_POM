import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


class TestChangePass(unittest.TestCase):
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

    # def test_1(self):
    #     self.driver.get('https://account.hcmut.edu.vn/')
    #     username = self.driver.find_element(By.NAME,"login")
    #     oldpassword = self.driver.find_element(By.NAME,"oldpassword")
    #     newpassword = self.driver.find_element(By.NAME,"newpassword")
    #     confirmpassword = self.driver.find_element(By.NAME,"confirmpassword")
    #     submitBtn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[3]/form/div[5]/div/button")
        
    #     username.send_keys("son.cuthanh27")
    #     oldpassword.send_keys("12345678")
    #     newpassword.send_keys("123456789")
    #     confirmpassword.send_keys("123456789")

    #     submitBtn.click()
    #     time.sleep(2)
    #     successAlert = self.driver.find_element(By.CLASS_NAME,'alert-success')
    #     # assert successAlert.text == "  Your password was changed and your email password on Gmail will updated after 12 hours"

    def test_b(self):
        self.driver.get('https://account.hcmut.edu.vn/')
        username = self.driver.find_element(By.NAME,"login")
        oldpassword = self.driver.find_element(By.NAME,"oldpassword")
        newpassword = self.driver.find_element(By.NAME,"newpassword")
        confirmpassword = self.driver.find_element(By.NAME,"confirmpassword")
        submitBtn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[3]/form/div[5]/div/button")
        
        username.send_keys("abcdef")
        oldpassword.send_keys("12345678")
        newpassword.send_keys("123456789")
        confirmpassword.send_keys("123456789")

        submitBtn.click()
        time.sleep(2)
        alertDanger = self.driver.find_element(By.CLASS_NAME,'alert-danger')
        assert alertDanger.text == "Login or password incorrect"

    def test_c(self):
        self.driver.get('https://account.hcmut.edu.vn/')
        username = self.driver.find_element(By.NAME,"login")
        oldpassword = self.driver.find_element(By.NAME,"oldpassword")
        newpassword = self.driver.find_element(By.NAME,"newpassword")
        confirmpassword = self.driver.find_element(By.NAME,"confirmpassword")
        submitBtn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[3]/form/div[5]/div/button")
        
        username.send_keys("")
        oldpassword.send_keys("12345678")
        newpassword.send_keys("123456789")
        confirmpassword.send_keys("123456789")

        submitBtn.click()
        time.sleep(2)
        alertDanger = self.driver.find_element(By.CLASS_NAME,'alert-warning')
        # assert alertDanger.text == " Your login is required"

    def test_d(self):
        self.driver.get('https://account.hcmut.edu.vn/')
        username = self.driver.find_element(By.NAME,"login")
        oldpassword = self.driver.find_element(By.NAME,"oldpassword")
        newpassword = self.driver.find_element(By.NAME,"newpassword")
        confirmpassword = self.driver.find_element(By.NAME,"confirmpassword")
        submitBtn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[3]/form/div[5]/div/button")
        
        username.send_keys("son.cuthanh27")
        oldpassword.send_keys("11111111")
        newpassword.send_keys("123456789")
        confirmpassword.send_keys("123456789")

        submitBtn.click()
        time.sleep(2)
        alertDanger = self.driver.find_element(By.CLASS_NAME,'alert-danger')
        # assert alertDanger.text == " Login or password incorrect"

    def test_e(self):
        self.driver.get('https://account.hcmut.edu.vn/')
        username = self.driver.find_element(By.NAME,"login")
        oldpassword = self.driver.find_element(By.NAME,"oldpassword")
        newpassword = self.driver.find_element(By.NAME,"newpassword")
        confirmpassword = self.driver.find_element(By.NAME,"confirmpassword")
        submitBtn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[3]/form/div[5]/div/button")
        
        username.send_keys("son.cuthanh27")
        newpassword.send_keys("123456789")
        confirmpassword.send_keys("123456789")

        submitBtn.click()
        time.sleep(2)
        alertDanger = self.driver.find_element(By.CLASS_NAME,'alert-warning')
        # assert alertDanger.text == " Your old password is required"

    def test_f(self):
        self.driver.get('https://account.hcmut.edu.vn/')
        username = self.driver.find_element(By.NAME,"login")
        oldpassword = self.driver.find_element(By.NAME,"oldpassword")
        newpassword = self.driver.find_element(By.NAME,"newpassword")
        confirmpassword = self.driver.find_element(By.NAME,"confirmpassword")
        submitBtn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[3]/form/div[5]/div/button")
        
        username.send_keys("son.cuthanh27")
        oldpassword.send_keys("12345678")
        confirmpassword.send_keys("123456789")

        submitBtn.click()
        time.sleep(2)
        alertDanger = self.driver.find_element(By.CLASS_NAME,'alert-danger')
        # assert alertDanger.text == " Passwords mismatch"


    def test_g(self):
        self.driver.get('https://account.hcmut.edu.vn/')
        username = self.driver.find_element(By.NAME,"login")
        oldpassword = self.driver.find_element(By.NAME,"oldpassword")
        newpassword = self.driver.find_element(By.NAME,"newpassword")
        confirmpassword = self.driver.find_element(By.NAME,"confirmpassword")
        submitBtn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[3]/form/div[5]/div/button")
        
        username.send_keys("son.cuthanh27")
        oldpassword.send_keys("12345678")
        newpassword.send_keys("dat.luongmason")
        confirmpassword.send_keys("dat.luongmason")

        submitBtn.click()
        time.sleep(2)
        alertDanger = self.driver.find_element(By.CLASS_NAME,'alert-danger')
        # assert alertDanger.text == " Your new password is identical to your login"

    def test_h(self):
        self.driver.get('https://account.hcmut.edu.vn/')
        username = self.driver.find_element(By.NAME,"login")
        oldpassword = self.driver.find_element(By.NAME,"oldpassword")
        newpassword = self.driver.find_element(By.NAME,"newpassword")
        confirmpassword = self.driver.find_element(By.NAME,"confirmpassword")
        submitBtn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[3]/form/div[5]/div/button")
        
        username.send_keys("son.cuthanh27")
        oldpassword.send_keys("12345678")
        newpassword.send_keys("12345678")
        confirmpassword.send_keys("12345678")

        submitBtn.click()
        time.sleep(2)
        alertDanger = self.driver.find_element(By.CLASS_NAME,'alert-danger')
        # assert alertDanger.text == " Your new password is identical to your old password"

    def test_i(self):
        self.driver.get('https://account.hcmut.edu.vn/')
        username = self.driver.find_element(By.NAME,"login")
        oldpassword = self.driver.find_element(By.NAME,"oldpassword")
        newpassword = self.driver.find_element(By.NAME,"newpassword")
        confirmpassword = self.driver.find_element(By.NAME,"confirmpassword")
        submitBtn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[3]/form/div[5]/div/button")
        
        username.send_keys("son.cuthanh27")
        oldpassword.send_keys("12345678")
        newpassword.send_keys("12345")
        confirmpassword.send_keys("12345")

        submitBtn.click()
        time.sleep(2)
        alertDanger = self.driver.find_element(By.CLASS_NAME,'alert-danger')
        # assert alertDanger.text == " Your password is too short"

    def test_k(self):
        self.driver.get('https://account.hcmut.edu.vn/')
        username = self.driver.find_element(By.NAME,"login")
        oldpassword = self.driver.find_element(By.NAME,"oldpassword")
        newpassword = self.driver.find_element(By.NAME,"newpassword")
        confirmpassword = self.driver.find_element(By.NAME,"confirmpassword")
        submitBtn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[3]/form/div[5]/div/button")
        
        username.send_keys("son.cuthanh27")
        oldpassword.send_keys("12345678")
        newpassword.send_keys("123456789101112131415")
        confirmpassword.send_keys("123456789101112131415")

        submitBtn.click()
        time.sleep(2)
        alertDanger = self.driver.find_element(By.CLASS_NAME,'alert-danger')
        # assert alertDanger.text == " Your password is too long"

    def test_j(self):
        self.driver.get('https://account.hcmut.edu.vn/')
        username = self.driver.find_element(By.NAME,"login")
        oldpassword = self.driver.find_element(By.NAME,"oldpassword")
        newpassword = self.driver.find_element(By.NAME,"newpassword")
        confirmpassword = self.driver.find_element(By.NAME,"confirmpassword")
        submitBtn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[3]/form/div[5]/div/button")
        
        username.send_keys("son.cuthanh27")
        oldpassword.send_keys("12345678")
        newpassword.send_keys("123456789")
        confirmpassword.send_keys("123456711")

        submitBtn.click()
        time.sleep(2)
        alertDanger = self.driver.find_element(By.CLASS_NAME,'alert-danger')
        # assert alertDanger.text == " Passwords mismatch"

    def test_l(self):
        self.driver.get('https://account.hcmut.edu.vn/')
        username = self.driver.find_element(By.NAME,"login")
        oldpassword = self.driver.find_element(By.NAME,"oldpassword")
        newpassword = self.driver.find_element(By.NAME,"newpassword")
        confirmpassword = self.driver.find_element(By.NAME,"confirmpassword")
        submitBtn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[3]/form/div[5]/div/button")
        
        username.send_keys("son.cuthanh27")
        oldpassword.send_keys("12345678")
        newpassword.send_keys("123456789")

        submitBtn.click()
        time.sleep(2)
        alertDanger = self.driver.find_element(By.CLASS_NAME,'alert-danger')
        # assert alertDanger.text == " Passwords mismatch"

    def test_m(self):
        self.driver.get('https://account.hcmut.edu.vn/')
        username = self.driver.find_element(By.NAME,"login")
        oldpassword = self.driver.find_element(By.NAME,"oldpassword")
        newpassword = self.driver.find_element(By.NAME,"newpassword")
        confirmpassword = self.driver.find_element(By.NAME,"confirmpassword")
        submitBtn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[3]/form/div[5]/div/button")
        
        username.send_keys("son.cuthanh27")
        oldpassword.send_keys("12345678")
        newpassword.send_keys("1111111")
        confirmpassword.send_keys("1111111")

        submitBtn.click()
        time.sleep(2)
        alertDanger = self.driver.find_element(By.CLASS_NAME,'alert-danger')
        # assert alertDanger.text == " Your password is too short"

    def test_n(self):
        self.driver.get('https://account.hcmut.edu.vn/')
        username = self.driver.find_element(By.NAME,"login")
        oldpassword = self.driver.find_element(By.NAME,"oldpassword")
        newpassword = self.driver.find_element(By.NAME,"newpassword")
        confirmpassword = self.driver.find_element(By.NAME,"confirmpassword")
        submitBtn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[3]/form/div[5]/div/button")
        
        username.send_keys("son.cuthanh27")
        oldpassword.send_keys("12345678")
        newpassword.send_keys("11111111")
        confirmpassword.send_keys("11111111")

        submitBtn.click()
        time.sleep(2)
        successAlert = self.driver.find_element(By.CLASS_NAME,'alert-success')
        # assert successAlert.text == "  Your password was changed and your email password on Gmail will updated after 12 hours"

    def test_o(self):
        self.driver.get('https://account.hcmut.edu.vn/')
        username = self.driver.find_element(By.NAME,"login")
        oldpassword = self.driver.find_element(By.NAME,"oldpassword")
        newpassword = self.driver.find_element(By.NAME,"newpassword")
        confirmpassword = self.driver.find_element(By.NAME,"confirmpassword")
        submitBtn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[3]/form/div[5]/div/button")
        
        username.send_keys("son.cuthanh27")
        oldpassword.send_keys("11111111")
        newpassword.send_keys("111111111111")
        confirmpassword.send_keys("111111111111")

        submitBtn.click()
        time.sleep(2)
        successAlert = self.driver.find_element(By.CLASS_NAME,'alert-success')
        # assert successAlert.text == "  Your password was changed and your email password on Gmail will updated after 12 hours"

    def test_p(self):
        self.driver.get('https://account.hcmut.edu.vn/')
        username = self.driver.find_element(By.NAME,"login")
        oldpassword = self.driver.find_element(By.NAME,"oldpassword")
        newpassword = self.driver.find_element(By.NAME,"newpassword")
        confirmpassword = self.driver.find_element(By.NAME,"confirmpassword")
        submitBtn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[3]/form/div[5]/div/button")
        
        username.send_keys("son.cuthanh27")
        oldpassword.send_keys("111111111111")
        newpassword.send_keys("111111111111111")
        confirmpassword.send_keys("111111111111111")

        submitBtn.click()
        time.sleep(2)
        successAlert = self.driver.find_element(By.CLASS_NAME,'alert-success')
        # assert successAlert.text == "  Your password was changed and your email password on Gmail will updated after 12 hours"

    def test_q(self):
        self.driver.get('https://account.hcmut.edu.vn/')
        username = self.driver.find_element(By.NAME,"login")
        oldpassword = self.driver.find_element(By.NAME,"oldpassword")
        newpassword = self.driver.find_element(By.NAME,"newpassword")
        confirmpassword = self.driver.find_element(By.NAME,"confirmpassword")
        submitBtn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[3]/form/div[5]/div/button")
        
        username.send_keys("son.cuthanh27")
        oldpassword.send_keys("111111111111111")
        newpassword.send_keys("1111111111111111")
        confirmpassword.send_keys("1111111111111111")

        submitBtn.click()
        time.sleep(2)
        successAlert = self.driver.find_element(By.CLASS_NAME,'alert-success')
        # assert successAlert.text == "  Your password was changed and your email password on Gmail will updated after 12 hours"

    def test_r(self):
        self.driver.get('https://account.hcmut.edu.vn/')
        username = self.driver.find_element(By.NAME,"login")
        oldpassword = self.driver.find_element(By.NAME,"oldpassword")
        newpassword = self.driver.find_element(By.NAME,"newpassword")
        confirmpassword = self.driver.find_element(By.NAME,"confirmpassword")
        submitBtn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[3]/form/div[5]/div/button")
        
        username.send_keys("son.cuthanh27")
        oldpassword.send_keys("1111111111111111")
        newpassword.send_keys("11111111111111111")
        confirmpassword.send_keys("11111111111111111")

        submitBtn.click()
        time.sleep(2)
        alertDanger = self.driver.find_element(By.CLASS_NAME,'alert-danger')
        # assert alertDanger.text == " Your password is too long"

    def test_t(self):
        self.driver.get('https://account.hcmut.edu.vn/')
        username = self.driver.find_element(By.NAME,"login")
        oldpassword = self.driver.find_element(By.NAME,"oldpassword")
        newpassword = self.driver.find_element(By.NAME,"newpassword")
        confirmpassword = self.driver.find_element(By.NAME,"confirmpassword")
        submitBtn = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[3]/form/div[5]/div/button")
        
        username.send_keys("son.cuthanh27")
        oldpassword.send_keys("1111111111111111")
        newpassword.send_keys("123456789")
        confirmpassword.send_keys("123456789")

        submitBtn.click()
        time.sleep(2)
        successAlert = self.driver.find_element(By.CLASS_NAME,'alert-success')
        assert successAlert.text == "  Your password was changed and your email password on Gmail will updated after 12 hours"

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()