import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select


class TestPrintTranscript(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://mybk.hcmut.edu.vn/my/logoutSSO.action")
        self.driver.get('https://sso.hcmut.edu.vn/cas/login?service=https://mybk.hcmut.edu.vn/my/homeSSO.action')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")  
        submitBtn = self.driver.find_element(By.NAME,"submit")  
        
        username.send_keys("son.cuthanh27")
        password.send_keys("02072002")
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
        self.driver.get('https://mybk.hcmut.edu.vn/apps/src/inbd/index.aspx')
        selectType = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_loaidangkyin"))
        selectType.select_by_value("TB")

        selectDest = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_coso"))
        selectDest.select_by_value("CS2")

        quantityInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txt_soluong")
        
        confirmInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_chk_allow")
        confirmInp.click()

        submitBtn = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_bnt_xacnhan")
        submitBtn.click()
        
        notification = self.driver.find_element(By.CSS_SELECTOR,'.msgBoxContent span')
        assert  "Nhập số lượng" == notification.text

    def test_2(self):
        self.driver.get('https://mybk.hcmut.edu.vn/apps/src/inbd/index.aspx')
        selectType = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_loaidangkyin"))
        selectType.select_by_value("TB")
        
        selectDest = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_coso"))
        selectDest.select_by_value("CS2")
        
        quantityInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txt_soluong")
        quantityInp.send_keys("0")
        
        confirmInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_chk_allow")
        
        submitBtn = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_bnt_xacnhan")
        assert not submitBtn.is_enabled()


    def test_3(self):
        self.driver.get('https://mybk.hcmut.edu.vn/apps/src/inbd/index.aspx')
        selectType = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_loaidangkyin"))
        selectType.select_by_value("TB")
        
        selectDest = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_coso"))
        
        quantityInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txt_soluong")
        quantityInp.send_keys("0")

        confirmInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_chk_allow")
        
        submitBtn = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_bnt_xacnhan")
        assert not submitBtn.is_enabled()
        

    def test_4(self):
        self.driver.get('https://mybk.hcmut.edu.vn/apps/src/inbd/index.aspx')
        selectType = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_loaidangkyin"))
        selectType.select_by_value("TB")
        
        selectDest = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_coso"))
        selectDest.select_by_value("CS2")
        
        quantityInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txt_soluong")
        
        confirmInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_chk_allow")
        
        submitBtn = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_bnt_xacnhan")
        assert not submitBtn.is_enabled()

    def test_5(self):
        self.driver.get('https://mybk.hcmut.edu.vn/apps/src/inbd/index.aspx')
        selectType = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_loaidangkyin"))
        selectType.select_by_value("TB")
        
        selectDest = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_coso"))
        
        quantityInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txt_soluong")
        
        confirmInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_chk_allow")
        
        submitBtn = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_bnt_xacnhan")
        assert not submitBtn.is_enabled()
        

    def test_6(self):
        self.driver.get('https://mybk.hcmut.edu.vn/apps/src/inbd/index.aspx')
        selectType = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_loaidangkyin"))
        selectType.select_by_value("TB")
        
        selectDest = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_coso"))
        selectDest.select_by_value("CS2")
        
        quantityInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txt_soluong")
        quantityInp.send_keys("1")
        
        confirmInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_chk_allow")
        confirmInp.click()
        
        submitBtn = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_bnt_xacnhan")
        submitBtn.click()
        time.sleep(2)
        
        cancelPrint = self.driver.find_element(By.NAME,'ctl00$ContentPlaceHolder1$lst_dsphieu$ctl00$bnt_huyphieu')
        cancelPrint.click()

    def test_7(self):
        self.driver.get('https://mybk.hcmut.edu.vn/apps/src/inbd/index.aspx')
        selectType = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_loaidangkyin"))
        selectType.select_by_value("TB")
        
        selectDest = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_coso"))
        selectDest.select_by_value("CS2")
        
        quantityInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txt_soluong")
        quantityInp.send_keys("2")

        
        confirmInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_chk_allow")
        
        submitBtn = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_bnt_xacnhan")
        assert not submitBtn.is_enabled()
        

    def test_8(self):
        self.driver.get('https://mybk.hcmut.edu.vn/apps/src/inbd/index.aspx')
        selectType = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_loaidangkyin"))
        selectType.select_by_value("TB")
        
        selectDest = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_coso"))
        
        quantityInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txt_soluong")
        quantityInp.send_keys("2")

        confirmInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_chk_allow")
        
        submitBtn = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_bnt_xacnhan")
        assert not submitBtn.is_enabled()

    def test_9(self):
        self.driver.get('https://mybk.hcmut.edu.vn/apps/src/inbd/index.aspx')
        selectType = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_loaidangkyin"))
        selectType.select_by_value("TB")
        
        selectDest = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_coso"))
        selectDest.select_by_value("CS2")
        
        quantityInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txt_soluong")
        quantityInp.send_keys("0")

        confirmInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_chk_allow")
        confirmInp.click()
        
        submitBtn = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_bnt_xacnhan")
        submitBtn.click()
        time.sleep(2)
        
        notification = self.driver.find_element(By.CSS_SELECTOR,'.msgBoxContent span')
        assert notification.text == "Số lượng in tối thiểu 1 và tối đa 9"
        

    def test_10(self):
        self.driver.get('https://mybk.hcmut.edu.vn/apps/src/inbd/index.aspx')
        selectType = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_loaidangkyin"))
        selectType.select_by_value("TB")
        
        selectDest = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_coso"))
        
        quantityInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txt_soluong")
        
        confirmInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_chk_allow")
        confirmInp.click()
        
        submitBtn = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_bnt_xacnhan")
        submitBtn.click()
        time.sleep(2)
        
        notification = self.driver.find_element(By.CSS_SELECTOR,'.msgBoxContent span')
        assert notification.text == "Chọn nơi nhận kết quả"
        
    def test_11(self):
        self.driver.get('https://mybk.hcmut.edu.vn/apps/src/inbd/index.aspx')
        selectType = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_loaidangkyin"))
        selectType.select_by_value("TB")
        
        selectDest = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_coso"))
        
        quantityInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txt_soluong")
        quantityInp.send_keys("0")
        
        confirmInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_chk_allow")
        confirmInp.click()
        
        submitBtn = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_bnt_xacnhan")
        submitBtn.click()
        time.sleep(2)
        
        notification = self.driver.find_element(By.CSS_SELECTOR,'.msgBoxContent span')
        assert notification.text == "Chọn nơi nhận kết quả"
        

    def test_12(self):
        self.driver.get('https://mybk.hcmut.edu.vn/apps/src/inbd/index.aspx')
        selectType = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_loaidangkyin"))
        selectType.select_by_value("TB")
        
        selectDest = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_coso"))
        
        quantityInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txt_soluong")
        quantityInp.send_keys("2")
        
        confirmInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_chk_allow")
        confirmInp.click()
        
        submitBtn = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_bnt_xacnhan")
        submitBtn.click()
        time.sleep(2)
        
        notification = self.driver.find_element(By.CSS_SELECTOR,'.msgBoxContent span')
        assert notification.text == "Chọn nơi nhận kết quả"

    def test_13(self):
        self.driver.get('https://mybk.hcmut.edu.vn/apps/src/inbd/index.aspx')
        selectType = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_loaidangkyin"))
        selectType.select_by_value("TB")
        
        selectDest = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_coso"))
        selectDest.select_by_value("CS2")
        
        quantityInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txt_soluong")
        quantityInp.send_keys("a")
        
        confirmInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_chk_allow")
        confirmInp.click()
        
        submitBtn = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_bnt_xacnhan")
        submitBtn.click()
        time.sleep(2)
        
        notification = self.driver.find_element(By.CSS_SELECTOR,'.msgBoxContent span')
        assert notification.text == "Nhập số lượng"
        

    def test_14(self):
        self.driver.get('https://mybk.hcmut.edu.vn/apps/src/inbd/index.aspx')
        selectType = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_loaidangkyin"))
        selectType.select_by_value("TB")
        
        selectDest = Select(self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_cbo_coso"))
        selectDest.select_by_value("CS2")
        
        quantityInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_txt_soluong")
        quantityInp.send_keys("1")

        confirmInp = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_chk_allow")
        
        submitBtn = self.driver.find_element(By.ID,"ctl00_ContentPlaceHolder1_bnt_xacnhan")
        assert not submitBtn.is_enabled()
        


    def tearDown(self):
        self.driver.get("https://mybk.hcmut.edu.vn/my/homeSSO.action")
        logoutBtn = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/a[1]")
        logoutBtn.click()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()