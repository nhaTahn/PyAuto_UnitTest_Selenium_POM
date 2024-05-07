import unittest
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select

cwd = os.getcwd()


class TestPrintTranscript(unittest.TestCase):
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

    def test_1(self):  # done
        self.driver.get(
            "https://mybk.hcmut.edu.vn/apps/src/nopccav/index.aspx")
        self.driver.find_element(By.XPATH, '//*[@id="bnt_themmoi"]').click()
        time.sleep(1)
        selectType = Select(self.driver.find_element(By.ID, 'cbo_loaicc'))
        selectType.select_by_value("TOEIC_1")
        time.sleep(1)
        id = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_IdNumber")
        date = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TestDate")
        listeningInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Listening")
        readingInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Reading")
        total = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TotalScore")
        load_file = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_ftp_ccav"]')
        time.sleep(1)
        id.send_keys("1111111111")
        date.send_keys("08/07/2022")
        readingInp.send_keys(4)
        listeningInp.send_keys(250)
        total.send_keys(254)
        load_file.send_keys(cwd + '\Data_Driven\SubmitCertificate\TOEIC.jpg')
        time.sleep(5)

        btn = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_bnt_xacnhan"]')
        time.sleep(1)
        btn.click()

        noti = self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[1]/div[2]/p/span').text
        print(noti)
        time.sleep(5)

        self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[2]/input').click()

        time.sleep(2)
        self.driver.find_element(
            By.XPATH, '/html/body/form/div[4]/div/div[8]/table/tbody/tr[1]/td[7]/input[3]').click()
        assert noti == "Điểm thành phần không hợp lệ, điểm chỉ bao gồm số và dấu chấm (.)"

    def test_2(self):  # done
        self.driver.get(
            "https://mybk.hcmut.edu.vn/apps/src/nopccav/index.aspx")
        self.driver.find_element(By.XPATH, '//*[@id="bnt_themmoi"]').click()
        time.sleep(1)
        selectType = Select(self.driver.find_element(By.ID, 'cbo_loaicc'))
        selectType.select_by_value("TOEIC_1")
        time.sleep(1)
        id = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_IdNumber")
        date = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TestDate")
        listeningInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Listening")
        readingInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Reading")
        total = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TotalScore")
        load_file = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_ftp_ccav"]')
        time.sleep(1)
        id.send_keys("1111111111")
        date.send_keys("08/07/2022")
        readingInp.send_keys(5)
        listeningInp.send_keys(250)
        total.send_keys(255)
        load_file.send_keys(cwd + '\Data_Driven\SubmitCertificate\TOEIC.jpg')
        time.sleep(2)

        btn = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_bnt_xacnhan"]')
        time.sleep(1)
        btn.click()

        noti = self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[1]/div[2]/p/span').text
        print(noti)
        time.sleep(5)

        self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[2]/input').click()

        time.sleep(2)
        self.driver.find_element(
            By.XPATH, '/html/body/form/div[4]/div/div[8]/table/tbody/tr[1]/td[7]/input[3]').click()
        assert noti == "Thông tin chứng chỉ đã được cập nhật"

    def test_3(self):  # done
        self.driver.get(
            "https://mybk.hcmut.edu.vn/apps/src/nopccav/index.aspx")
        self.driver.find_element(By.XPATH, '//*[@id="bnt_themmoi"]').click()
        time.sleep(1)
        selectType = Select(self.driver.find_element(By.ID, 'cbo_loaicc'))
        selectType.select_by_value("TOEIC_1")
        time.sleep(1)
        id = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_IdNumber")
        date = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TestDate")
        listeningInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Listening")
        readingInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Reading")
        total = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TotalScore")
        load_file = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_ftp_ccav"]')
        time.sleep(1)
        id.send_keys("1111111111")
        date.send_keys("08/07/2022")
        readingInp.send_keys(6)
        listeningInp.send_keys(250)
        total.send_keys(256)
        load_file.send_keys(cwd + '\Data_Driven\SubmitCertificate\TOEIC.jpg')
        time.sleep(2)

        btn = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_bnt_xacnhan"]')
        time.sleep(1)
        btn.click()

        noti = self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[1]/div[2]/p/span').text
        print(noti)
        time.sleep(5)
        self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[2]/input').click()

        time.sleep(3)
        self.driver.find_element(
            By.XPATH, '/html/body/form/div[4]/div/div[8]/table/tbody/tr[1]/td[7]/input[3]').click()
        assert noti == "Thông tin chứng chỉ đã được cập nhật"

    def test_4(self):  # done
        self.driver.get(
            "https://mybk.hcmut.edu.vn/apps/src/nopccav/index.aspx")
        self.driver.find_element(By.XPATH, '//*[@id="bnt_themmoi"]').click()
        time.sleep(2)
        selectType = Select(self.driver.find_element(By.ID, 'cbo_loaicc'))
        selectType.select_by_value("TOEIC_1")
        time.sleep(2)
        id = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_IdNumber")
        date = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TestDate")
        listeningInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Listening")
        readingInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Reading")
        total = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TotalScore")
        load_file = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_ftp_ccav"]')
        time.sleep(1)
        id.send_keys("1111111111")
        date.send_keys("08/07/2022")
        readingInp.send_keys(250)
        listeningInp.send_keys(4)
        total.send_keys(254)
        load_file.send_keys(cwd + '\Data_Driven\SubmitCertificate\TOEIC.jpg')
        time.sleep(2)

        btn = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_bnt_xacnhan"]')
        time.sleep(1)
        btn.click()

        noti = self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[1]/div[2]/p/span').text
        print(noti)
        time.sleep(5)

        self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[2]/input').click()

        time.sleep(2)
        self.driver.find_element(
            By.XPATH, '/html/body/form/div[4]/div/div[8]/table/tbody/tr[1]/td[7]/input[3]').click()
        assert noti == "Điểm thành phần không hợp lệ, điểm chỉ bao gồm số và dấu chấm (.)"

    def test_5(self):  # done
        self.driver.get(
            "https://mybk.hcmut.edu.vn/apps/src/nopccav/index.aspx")
        self.driver.find_element(By.XPATH, '//*[@id="bnt_themmoi"]').click()
        time.sleep(1)
        selectType = Select(self.driver.find_element(By.ID, 'cbo_loaicc'))
        selectType.select_by_value("TOEIC_1")
        time.sleep(1)
        id = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_IdNumber")
        date = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TestDate")
        listeningInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Listening")
        readingInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Reading")
        total = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TotalScore")
        load_file = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_ftp_ccav"]')
        time.sleep(1)
        id.send_keys("1111111111")
        date.send_keys("08/07/2022")
        readingInp.send_keys(250)
        listeningInp.send_keys(5)
        total.send_keys(255)
        load_file.send_keys(cwd + '\Data_Driven\SubmitCertificate\TOEIC.jpg')
        time.sleep(2)

        btn = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_bnt_xacnhan"]')
        time.sleep(1)
        btn.click()

        noti = self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[1]/div[2]/p/span').text
        print(noti)
        time.sleep(5)

        self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[2]/input').click()

        time.sleep(2)
        self.driver.find_element(
            By.XPATH, '/html/body/form/div[4]/div/div[8]/table/tbody/tr[1]/td[7]/input[3]').click()
        assert noti == "Thông tin chứng chỉ đã được cập nhật"

    def test_6(self):  # done
        self.driver.get(
            "https://mybk.hcmut.edu.vn/apps/src/nopccav/index.aspx")
        self.driver.find_element(By.XPATH, '//*[@id="bnt_themmoi"]').click()
        time.sleep(1)
        selectType = Select(self.driver.find_element(By.ID, 'cbo_loaicc'))
        selectType.select_by_value("TOEIC_1")
        time.sleep(1)
        id = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_IdNumber")
        date = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TestDate")
        listeningInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Listening")
        readingInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Reading")
        total = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TotalScore")
        load_file = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_ftp_ccav"]')
        time.sleep(1)
        id.send_keys("1111111111")
        date.send_keys("08/07/2022")
        readingInp.send_keys(250)
        listeningInp.send_keys(6)
        total.send_keys(256)
        load_file.send_keys(cwd + '\Data_Driven\SubmitCertificate\TOEIC.jpg')
        time.sleep(2)

        btn = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_bnt_xacnhan"]')
        time.sleep(1)
        btn.click()

        noti = self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[1]/div[2]/p/span').text
        print(noti)
        time.sleep(5)

        self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[2]/input').click()

        time.sleep(2)
        self.driver.find_element(
            By.XPATH, '/html/body/form/div[4]/div/div[8]/table/tbody/tr[1]/td[7]/input[3]').click()
        assert noti == "Thông tin chứng chỉ đã được cập nhật"

    def test_7(self):  # done
        self.driver.get(
            "https://mybk.hcmut.edu.vn/apps/src/nopccav/index.aspx")
        self.driver.find_element(By.XPATH, '//*[@id="bnt_themmoi"]').click()
        time.sleep(2)
        selectType = Select(self.driver.find_element(By.ID, 'cbo_loaicc'))
        selectType.select_by_value("TOEIC_1")
        time.sleep(2)
        id = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_IdNumber")
        date = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TestDate")
        listeningInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Listening")
        readingInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Reading")
        total = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TotalScore")
        load_file = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_ftp_ccav"]')
        time.sleep(1)
        id.send_keys("1111111111")
        date.send_keys("08/07/2022")
        readingInp.send_keys(250)
        listeningInp.send_keys(494)
        total.send_keys(744)
        load_file.send_keys(cwd + '\Data_Driven\SubmitCertificate\TOEIC.jpg')
        time.sleep(5)

        btn = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_bnt_xacnhan"]')
        time.sleep(1)
        btn.click()
        time.sleep(6)

        noti = self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[1]/div[2]/p/span').text
        print(noti)
        self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[2]/input').click()

        time.sleep(2)
        self.driver.find_element(
            By.XPATH, '/html/body/form/div[4]/div/div[8]/table/tbody/tr[1]/td[7]/input[3]').click()
        assert noti == "Thông tin chứng chỉ đã được cập nhật"

    def test_8(self):  # done
        self.driver.get(
            "https://mybk.hcmut.edu.vn/apps/src/nopccav/index.aspx")
        self.driver.find_element(By.XPATH, '//*[@id="bnt_themmoi"]').click()
        time.sleep(2)
        selectType = Select(self.driver.find_element(By.ID, 'cbo_loaicc'))
        selectType.select_by_value("TOEIC_1")
        time.sleep(2)
        id = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_IdNumber")
        date = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TestDate")
        listeningInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Listening")
        readingInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Reading")
        total = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TotalScore")
        load_file = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_ftp_ccav"]')
        time.sleep(1)
        id.send_keys("1111111111")
        date.send_keys("08/07/2022")
        readingInp.send_keys(250)
        listeningInp.send_keys(495)
        total.send_keys(745)
        load_file.send_keys(cwd + '\Data_Driven\SubmitCertificate\TOEIC.jpg')
        time.sleep(5)

        btn = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_bnt_xacnhan"]')
        time.sleep(1)
        btn.click()
        time.sleep(6)

        noti = self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[1]/div[2]/p/span').text
        print(noti)
        self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[2]/input').click()

        time.sleep(2)
        self.driver.find_element(
            By.XPATH, '/html/body/form/div[4]/div/div[8]/table/tbody/tr[1]/td[7]/input[3]').click()
        assert noti == "Thông tin chứng chỉ đã được cập nhật"

    def test_9(self):  # done
        self.driver.get(
            "https://mybk.hcmut.edu.vn/apps/src/nopccav/index.aspx")
        self.driver.find_element(By.XPATH, '//*[@id="bnt_themmoi"]').click()
        time.sleep(2)
        selectType = Select(self.driver.find_element(By.ID, 'cbo_loaicc'))
        selectType.select_by_value("TOEIC_1")
        time.sleep(2)
        id = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_IdNumber")
        date = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TestDate")
        listeningInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Listening")
        readingInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Reading")
        total = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TotalScore")
        load_file = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_ftp_ccav"]')
        time.sleep(1)
        id.send_keys("1111111111")
        date.send_keys("08/07/2022")
        readingInp.send_keys(250)
        listeningInp.send_keys(496)
        total.send_keys(746)
        load_file.send_keys(cwd + '\Data_Driven\SubmitCertificate\TOEIC.jpg')
        time.sleep(5)

        btn = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_bnt_xacnhan"]')
        time.sleep(1)
        btn.click()
        time.sleep(6)

        noti = self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[1]/div[2]/p/span').text
        print(noti)
        self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[2]/input').click()

        time.sleep(2)
        self.driver.find_element(
            By.XPATH, '/html/body/form/div[4]/div/div[8]/table/tbody/tr[1]/td[7]/input[3]').click()
        assert noti == "Điểm thành phần không hợp lệ, điểm chỉ bao gồm số và dấu chấm (.)"

    def test_10(self):  # done
        self.driver.get(
            "https://mybk.hcmut.edu.vn/apps/src/nopccav/index.aspx")
        self.driver.find_element(By.XPATH, '//*[@id="bnt_themmoi"]').click()
        time.sleep(2)
        selectType = Select(self.driver.find_element(By.ID, 'cbo_loaicc'))
        selectType.select_by_value("TOEIC_1")
        time.sleep(2)
        id = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_IdNumber")
        date = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TestDate")
        listeningInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Listening")
        readingInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Reading")
        total = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TotalScore")
        load_file = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_ftp_ccav"]')
        time.sleep(1)
        id.send_keys("1111111111")
        date.send_keys("08/07/2022")
        readingInp.send_keys(494)
        listeningInp.send_keys(250)
        total.send_keys(744)
        load_file.send_keys(cwd + '\Data_Driven\SubmitCertificate\TOEIC.jpg')
        time.sleep(5)

        btn = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_bnt_xacnhan"]')
        time.sleep(1)
        btn.click()
        time.sleep(6)

        noti = self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[1]/div[2]/p/span').text
        print(noti)
        self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[2]/input').click()

        time.sleep(2)
        self.driver.find_element(
            By.XPATH, '/html/body/form/div[4]/div/div[8]/table/tbody/tr[1]/td[7]/input[3]').click()
        assert noti == "Thông tin chứng chỉ đã được cập nhật"

    def test_11(self):  # done
        self.driver.get(
            "https://mybk.hcmut.edu.vn/apps/src/nopccav/index.aspx")
        self.driver.find_element(By.XPATH, '//*[@id="bnt_themmoi"]').click()
        time.sleep(2)
        selectType = Select(self.driver.find_element(By.ID, 'cbo_loaicc'))
        selectType.select_by_value("TOEIC_1")
        time.sleep(2)
        id = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_IdNumber")
        date = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TestDate")
        listeningInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Listening")
        readingInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Reading")
        total = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TotalScore")
        load_file = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_ftp_ccav"]')
        time.sleep(1)
        id.send_keys("1111111111")
        date.send_keys("08/07/2022")
        readingInp.send_keys(495)
        listeningInp.send_keys(250)
        total.send_keys(744)
        load_file.send_keys(cwd + '\Data_Driven\SubmitCertificate\TOEIC.jpg')
        time.sleep(5)

        btn = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_bnt_xacnhan"]')
        time.sleep(1)
        btn.click()
        time.sleep(6)

        noti = self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[1]/div[2]/p/span').text
        print(noti)
        self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[2]/input').click()

        time.sleep(2)
        self.driver.find_element(
            By.XPATH, '/html/body/form/div[4]/div/div[8]/table/tbody/tr[1]/td[7]/input[3]').click()
        assert noti == "Thông tin chứng chỉ đã được cập nhật"

    def test_12(self):  # done
        self.driver.get(
            "https://mybk.hcmut.edu.vn/apps/src/nopccav/index.aspx")
        self.driver.find_element(By.XPATH, '//*[@id="bnt_themmoi"]').click()
        time.sleep(2)
        selectType = Select(self.driver.find_element(By.ID, 'cbo_loaicc'))
        selectType.select_by_value("TOEIC_1")
        time.sleep(2)
        id = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_IdNumber")
        date = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TestDate")
        listeningInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Listening")
        readingInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Reading")
        total = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TotalScore")
        load_file = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_ftp_ccav"]')
        time.sleep(1)
        id.send_keys("1111111111")
        date.send_keys("08/07/2022")
        readingInp.send_keys(496)
        listeningInp.send_keys(250)
        total.send_keys(746)
        load_file.send_keys(cwd + '\Data_Driven\SubmitCertificate\TOEIC.jpg')
        time.sleep(5)

        btn = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_bnt_xacnhan"]')
        time.sleep(1)
        btn.click()
        time.sleep(6)

        noti = self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[1]/div[2]/p/span').text
        print(noti)
        self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[2]/input').click()

        time.sleep(2)
        self.driver.find_element(
            By.XPATH, '/html/body/form/div[4]/div/div[8]/table/tbody/tr[1]/td[7]/input[3]').click()
        assert noti == "Điểm thành phần không hợp lệ, điểm chỉ bao gồm số và dấu chấm (.)"

    def test_15(self):  # done
        self.driver.get(
            "https://mybk.hcmut.edu.vn/apps/src/nopccav/index.aspx")
        self.driver.find_element(By.XPATH, '//*[@id="bnt_themmoi"]').click()
        time.sleep(2)
        selectType = Select(self.driver.find_element(By.ID, 'cbo_loaicc'))
        selectType.select_by_value("TOEIC_1")
        time.sleep(2)
        id = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_IdNumber")
        date = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TestDate")
        listeningInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Listening")
        readingInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Reading")
        total = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TotalScore")
        load_file = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_ftp_ccav"]')
        time.sleep(1)
        id.send_keys("1111111111")
        date.send_keys("08/07/2022")
        readingInp.send_keys(495)
        listeningInp.send_keys(495)
        total.send_keys(990)
        load_file.send_keys(cwd + '\Data_Driven\SubmitCertificate\TOEIC.jpg')
        time.sleep(5)

        btn = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_bnt_xacnhan"]')
        time.sleep(1)
        btn.click()
        time.sleep(6)

        noti = self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[1]/div[2]/p/span').text
        print(noti)
        self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[2]/input').click()

        time.sleep(2)
        self.driver.find_element(
            By.XPATH, '/html/body/form/div[4]/div/div[8]/table/tbody/tr[1]/td[7]/input[3]').click()
        assert noti == "Thông tin chứng chỉ đã được cập nhật"

    def test_16(self):  # done
        self.driver.get(
            "https://mybk.hcmut.edu.vn/apps/src/nopccav/index.aspx")
        self.driver.find_element(By.XPATH, '//*[@id="bnt_themmoi"]').click()
        time.sleep(2)
        selectType = Select(self.driver.find_element(By.ID, 'cbo_loaicc'))
        selectType.select_by_value("TOEIC_1")
        time.sleep(2)
        id = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_IdNumber")
        date = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TestDate")
        listeningInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Listening")
        readingInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Reading")
        total = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TotalScore")
        load_file = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_ftp_ccav"]')
        time.sleep(1)
        id.send_keys("1111111111")
        date.send_keys("08/07/2022")
        readingInp.send_keys(496)
        listeningInp.send_keys(496)
        total.send_keys(992)
        load_file.send_keys(cwd + '\Data_Driven\SubmitCertificate\TOEIC.jpg')
        time.sleep(5)

        btn = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_bnt_xacnhan"]')
        time.sleep(1)
        btn.click()
        time.sleep(6)

        noti = self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[1]/div[2]/p/span').text
        print(noti)
        self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[2]/input').click()

        time.sleep(2)
        self.driver.find_element(
            By.XPATH, '/html/body/form/div[4]/div/div[8]/table/tbody/tr[1]/td[7]/input[3]').click()
        assert noti == "Điểm tổng không hợp lệ, điểm chỉ bao gồm số và dấu chấm (.)"

    def test_17(self):  # done
        self.driver.get(
            "https://mybk.hcmut.edu.vn/apps/src/nopccav/index.aspx")
        self.driver.find_element(By.XPATH, '//*[@id="bnt_themmoi"]').click()
        time.sleep(2)
        selectType = Select(self.driver.find_element(By.ID, 'cbo_loaicc'))
        selectType.select_by_value("TOEIC_1")
        time.sleep(2)
        id = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_IdNumber")
        date = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TestDate")
        listeningInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Listening")
        readingInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Reading")
        total = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TotalScore")
        load_file = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_ftp_ccav"]')
        time.sleep(1)
        id.send_keys("1111111111")
        date.send_keys("08/07/2022")
        readingInp.send_keys(-1)
        listeningInp.send_keys(-1)
        total.send_keys(-2)
        load_file.send_keys(cwd + '\Data_Driven\SubmitCertificate\TOEIC.jpg')
        time.sleep(5)

        btn = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_bnt_xacnhan"]')
        time.sleep(1)
        btn.click()
        time.sleep(6)

        noti = self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[1]/div[2]/p/span').text
        print(noti)
        self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[2]/input').click()

        time.sleep(2)
        self.driver.find_element(
            By.XPATH, '/html/body/form/div[4]/div/div[8]/table/tbody/tr[1]/td[7]/input[3]').click()
        assert noti == "Điểm tổng không hợp lệ, điểm chỉ bao gồm số và dấu chấm (.)"

    def test_18(self):  # done
        self.driver.get(
            "https://mybk.hcmut.edu.vn/apps/src/nopccav/index.aspx")
        self.driver.find_element(By.XPATH, '//*[@id="bnt_themmoi"]').click()
        time.sleep(2)
        selectType = Select(self.driver.find_element(By.ID, 'cbo_loaicc'))
        selectType.select_by_value("TOEIC_1")
        time.sleep(2)
        id = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_IdNumber")
        date = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TestDate")
        listeningInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Listening")
        readingInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Reading")
        total = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TotalScore")
        load_file = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_ftp_ccav"]')
        time.sleep(1)
        id.send_keys("1111111111")
        date.send_keys("08/07/2022")
        readingInp.send_keys(4)
        listeningInp.send_keys(4)
        total.send_keys(8)
        load_file.send_keys(cwd + '\Data_Driven\SubmitCertificate\TOEIC.jpg')
        time.sleep(5)

        btn = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_bnt_xacnhan"]')
        time.sleep(1)
        btn.click()
        time.sleep(6)

        noti = self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[1]/div[2]/p/span').text
        print(noti)
        self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[2]/input').click()

        time.sleep(2)
        self.driver.find_element(
            By.XPATH, '/html/body/form/div[4]/div/div[8]/table/tbody/tr[1]/td[7]/input[3]').click()
        assert noti == "Điểm tổng không hợp lệ, điểm chỉ bao gồm số và dấu chấm (.)"

    def test_19(self):  # done
        self.driver.get(
            "https://mybk.hcmut.edu.vn/apps/src/nopccav/index.aspx")
        self.driver.find_element(By.XPATH, '//*[@id="bnt_themmoi"]').click()
        time.sleep(2)
        selectType = Select(self.driver.find_element(By.ID, 'cbo_loaicc'))
        selectType.select_by_value("TOEIC_1")
        time.sleep(2)
        id = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_IdNumber")
        date = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TestDate")
        listeningInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Listening")
        readingInp = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_Reading")
        total = self.driver.find_element(
            By.NAME, "ctl00$ContentPlaceHolder1$txt_TOEIC_TotalScore")
        load_file = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_ftp_ccav"]')
        time.sleep(1)
        id.send_keys("1111111111")
        date.send_keys("08/07/2022")
        readingInp.send_keys(250)
        listeningInp.send_keys(250)
        total.send_keys(500)
        load_file.send_keys(cwd + '\Data_Driven\SubmitCertificate\TOEIC.jpg')
        time.sleep(5)

        btn = self.driver.find_element(
            By.XPATH, '//*[@id="ctl00_ContentPlaceHolder1_bnt_xacnhan"]')
        time.sleep(1)
        btn.click()
        time.sleep(6)

        noti = self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[1]/div[2]/p/span').text
        print(noti)
        self.driver.find_element(
            By.XPATH, '/html/div[2]/div[2]/div[2]/input').click()

        time.sleep(2)
        self.driver.find_element(
            By.XPATH, '/html/body/form/div[4]/div/div[8]/table/tbody/tr[1]/td[7]/input[3]').click()
        assert noti == "Thông tin chứng chỉ đã được cập nhật"

    def tearDown(self):
        self.driver.get("https://mybk.hcmut.edu.vn/my/homeSSO.action")
        logoutBtn = self.driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div/div[2]/div/a[1]")
        logoutBtn.click()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
