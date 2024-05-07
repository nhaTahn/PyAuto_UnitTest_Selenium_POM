import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


class TestRegisterWithDraw(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://mybk.hcmut.edu.vn/my/logoutSSO.action")
        self.driver.get('https://sso.hcmut.edu.vn/cas/login?service=https://mybk.hcmut.edu.vn/my/homeSSO.action')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")  
        submitBtn = self.driver.find_element(By.NAME,"submit")  
        #----Submit---#
        username.send_keys("quan.thibluesky17")
        password.send_keys("khacquan211")
        submitBtn.click()

    def get_element_wait(self, element_id, timeout=3):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.ID, element_id))
            )
        except TimeoutException:
            err = 'Element with id {} could not be found!'
            raise Exception(err.format(element_id))

    def test_1(self): #done
        self.driver.get('https://mybk.hcmut.edu.vn/app')
        self.driver.get('https://mybk.hcmut.edu.vn/app/sinh-vien/chung-nhan-sinh-vien/dang-ky')
        time.sleep(1)
        reasonInput = self.driver.find_element(By.ID,'select2-cboLoaiDangKy-container')
        reasonInput.click()
        time.sleep(1)
        ToeicBtn = self.driver.find_element(By.XPATH,'/html/body/span/span/span[2]/ul/li[1]')
        ToeicBtn.click()
        time.sleep(1)
        addressInput = self.driver.find_element(By.ID,'select2-cboNoiNhan-container')
        addressInput.click()
        time.sleep(1)
        Cs2btn = self.driver.find_element(By.XPATH,'/html/body/span/span/span[2]/ul/li[4]')
        Cs2btn.click()
        time.sleep(1)
        submitbtn = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/section[2]/div/div/ul/li[3]/div/div[2]/button[1]')
        submitbtn.click()
        time.sleep(2)
        assert self.driver.find_element(By.XPATH,'//*[@id="lstPhieuDangChoXuLy"]/tbody/tr')

    def test_2(self): #done
        self.driver.get('https://mybk.hcmut.edu.vn/app')
        self.driver.get('https://mybk.hcmut.edu.vn/app/sinh-vien/chung-nhan-sinh-vien/dang-ky')
        time.sleep(1)
        reasonInput = self.driver.find_element(By.ID,'select2-cboLoaiDangKy-container')
        time.sleep(1)
        addressInput = self.driver.find_element(By.ID,'select2-cboNoiNhan-container')
        addressInput.click()
        time.sleep(1)
        Cs2btn = self.driver.find_element(By.XPATH,'/html/body/span/span/span[2]/ul/li[4]')
        Cs2btn.click()
        time.sleep(1)
        submitbtn = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/section[2]/div/div/ul/li[3]/div/div[2]/button[1]')
        submitbtn.click()
        time.sleep(2)
        annoucement = self.driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div[1]')
        assert annoucement.text == "Bạn chưa chọn lý do đăng ký chứng nhận sinh viên"
    
    def test_3(self): #done
        self.driver.get('https://mybk.hcmut.edu.vn/app')
        self.driver.get('https://mybk.hcmut.edu.vn/app/sinh-vien/chung-nhan-sinh-vien/dang-ky')
        time.sleep(1)
        reasonInput = self.driver.find_element(By.ID,'select2-cboLoaiDangKy-container')
        reasonInput.click()
        time.sleep(1)
        ToeicBtn = self.driver.find_element(By.XPATH,'/html/body/span/span/span[2]/ul/li[1]')
        ToeicBtn.click()
        time.sleep(1)
        submitbtn = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/section[2]/div/div/ul/li[3]/div/div[2]/button[1]')
        submitbtn.click()
        time.sleep(2)
        annoucement = self.driver.find_element(By.XPATH,'//*[@id="swal2-content"]')
        assert annoucement.text == "Bạn chưa chọn nơi nhận kết quả"

    def test_4(self): #done
        self.driver.get('https://mybk.hcmut.edu.vn/app')
        self.driver.get('https://mybk.hcmut.edu.vn/app/sinh-vien/chung-nhan-sinh-vien/dang-ky')
        time.sleep(1)
        reasonInput = self.driver.find_element(By.ID,'select2-cboLoaiDangKy-container')
        reasonInput.click()
        time.sleep(1)
        ForeginBtn = self.driver.find_element(By.XPATH,'//*[@id="select2-cboLoaiDangKy-results"]/li[3]')
        ForeginBtn.click()
        time.sleep(1)
        addressInput = self.driver.find_element(By.ID,'select2-cboNoiNhan-container')
        addressInput.click()
        time.sleep(1)
        Cs2btn = self.driver.find_element(By.XPATH,'/html/body/span/span/span[2]/ul/li[4]')
        Cs2btn.click()
        time.sleep(1)
        submitbtn = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/section[2]/div/div/ul/li[3]/div/div[2]/button[1]')
        submitbtn.click()
        time.sleep(2)
        assert self.driver.find_element(By.XPATH,'//*[@id="lstPhieuDangChoXuLy"]/tbody/tr')
    
    def test_5(self): #done
        self.driver.get('https://mybk.hcmut.edu.vn/app')
        self.driver.get('https://mybk.hcmut.edu.vn/app/sinh-vien/chung-nhan-sinh-vien/dang-ky')
        time.sleep(1)
        reasonInput = self.driver.find_element(By.ID,'select2-cboLoaiDangKy-container')
        time.sleep(1)
        addressInput = self.driver.find_element(By.ID,'select2-cboNoiNhan-container')
        addressInput.click()
        time.sleep(1)
        Cs1btn = self.driver.find_element(By.XPATH,'//*[@id="select2-cboNoiNhan-results"]/li[1]')
        Cs1btn.click()
        time.sleep(1)
        submitbtn = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/section[2]/div/div/ul/li[3]/div/div[2]/button[1]')
        submitbtn.click()
        time.sleep(2)
        annoucement = self.driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div[1]')
        assert annoucement.text == "Bạn chưa chọn lý do đăng ký chứng nhận sinh viên"
    
    def test_6(self): #done
        self.driver.get('https://mybk.hcmut.edu.vn/app')
        self.driver.get('https://mybk.hcmut.edu.vn/app/sinh-vien/chung-nhan-sinh-vien/dang-ky')
        time.sleep(1)
        reasonInput = self.driver.find_element(By.ID,'select2-cboLoaiDangKy-container')
        reasonInput.click()
        time.sleep(1)
        ForeginBtn = self.driver.find_element(By.XPATH,'//*[@id="select2-cboLoaiDangKy-results"]/li[3]')
        ForeginBtn.click()
        time.sleep(1)
        submitbtn = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/section[2]/div/div/ul/li[3]/div/div[2]/button[1]')
        submitbtn.click()
        time.sleep(2)
        annoucement = self.driver.find_element(By.XPATH,'//*[@id="swal2-content"]')
        assert annoucement.text == "Bạn chưa chọn nơi nhận kết quả"

    def test_7(self): #done
        self.driver.get('https://mybk.hcmut.edu.vn/app')
        self.driver.get('https://mybk.hcmut.edu.vn/app/sinh-vien/chung-nhan-sinh-vien/dang-ky')
        time.sleep(1)
        reasonInput = self.driver.find_element(By.ID,'select2-cboLoaiDangKy-container')
        reasonInput.click()
        time.sleep(1)
        ForeginBtn = self.driver.find_element(By.XPATH,'//*[@id="select2-cboLoaiDangKy-results"]/li[3]')
        ForeginBtn.click()
        time.sleep(1)
        addressInput = self.driver.find_element(By.ID,'select2-cboNoiNhan-container')
        addressInput.click()
        time.sleep(1)
        Cs2btn = self.driver.find_element(By.XPATH,'/html/body/span/span/span[2]/ul/li[4]')
        Cs2btn.click()
        time.sleep(1)
        again = self.driver.find_element(By.XPATH,'//*[@id="btnNhapLai"]')
        again.click()
        time.sleep(1)
        reasonInput.click()
        time.sleep(1)
        ForeginBtn = self.driver.find_element(By.XPATH,'/html/body/span/span/span[2]/ul/li[6]')
        ForeginBtn.click()
        time.sleep(1)
        addressInput.click()
        time.sleep(1)
        Cs2btn = self.driver.find_element(By.XPATH,'//*[@id="select2-cboNoiNhan-results"]/li[2]')
        Cs2btn.click()
        time.sleep(1)
        submitbtn = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/section[2]/div/div/ul/li[3]/div/div[2]/button[1]')
        submitbtn.click()
        time.sleep(2)
        assert self.driver.find_element(By.XPATH,'//*[@id="lstPhieuDangChoXuLy"]/tbody/tr')
    
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()