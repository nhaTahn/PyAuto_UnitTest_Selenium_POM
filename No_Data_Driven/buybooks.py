import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


class TestBuyBooks(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.vars = {}
        self.driver.get("https://mybk.hcmut.edu.vn/my/logoutSSO.action")
        self.driver.get('https://sso.hcmut.edu.vn/cas/login?service=https://mybk.hcmut.edu.vn/my/homeSSO.action')
        username = self.driver.find_element(By.NAME,"username")
        password = self.driver.find_element(By.NAME,"password")  
        submitBtn = self.driver.find_element(By.NAME,"submit")  
    
        username.send_keys("quoc.le1804")
        password.send_keys("baoquoc1804")
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
        self.driver.get("https://mybk.hcmut.edu.vn/bookstore/product/2")
        quantityInput = self.driver.find_element(By.XPATH,'//*[@id="txtQuantity"]')
        quantityInput.clear()
        quantityInput.send_keys(0)
        time.sleep(2)
        addToCartBtn = self.driver.find_element(By.ID,'bntAddToCart')
        addToCartBtn.click()
        time.sleep(3)
        assert self.driver.find_element(By.XPATH,'//*[@id="swal2-content"]')

    def test_2(self): #done
        self.driver.get("https://mybk.hcmut.edu.vn/bookstore/product/2")
        quantityInput = self.driver.find_element(By.XPATH,'//*[@id="txtQuantity"]')
        quantityInput.clear()
        quantityInput.send_keys(1)
        time.sleep(2)
        addToCartBtn = self.driver.find_element(By.ID,'bntAddToCart')
        addToCartBtn.click()
        time.sleep(3)
        # notification = self.driver.find_element(By.XPATH,'//*[@id="swal2-content"]')
        # assert notification == 'Số lượng mua phải lớn hơn 0' or  notification == 'Số lượng mua tối đa 5 cuốn cho 1 tên sách'
        # assert notification == ""

    def test_3(self): #done
        self.driver.get("https://mybk.hcmut.edu.vn/bookstore/product/2")
        quantityInput = self.driver.find_element(By.XPATH,'//*[@id="txtQuantity"]')
        quantityInput.clear()
        quantityInput.send_keys(2)
        time.sleep(2)
        addToCartBtn = self.driver.find_element(By.ID,'bntAddToCart')
        addToCartBtn.click()
        time.sleep(3)
        # notification = self.driver.find_element(By.XPATH,'//*[@id="swal2-content"]')
        # assert notification == 'Số lượng mua phải lớn hơn 0' or  notification == 'Số lượng mua tối đa 5 cuốn cho 1 tên sách'
        # assert notification == ""
        
    def test_4(self): #done
        self.driver.get("https://mybk.hcmut.edu.vn/bookstore/product/2")
        quantityInput = self.driver.find_element(By.XPATH,'//*[@id="txtQuantity"]')
        quantityInput.clear()
        quantityInput.send_keys(3)
        time.sleep(2)
        addToCartBtn = self.driver.find_element(By.ID,'bntAddToCart')
        addToCartBtn.click()
        time.sleep(3)
        # notification = self.driver.find_element(By.XPATH,'//*[@id="swal2-content"]')
        # assert notification == 'Số lượng mua phải lớn hơn 0' or  notification == 'Số lượng mua tối đa 5 cuốn cho 1 tên sách'
        # assert notification == ""
  
    def test_5(self): #done
        self.driver.get("https://mybk.hcmut.edu.vn/bookstore/product/2")
        quantityInput = self.driver.find_element(By.XPATH,'//*[@id="txtQuantity"]')
        quantityInput.clear()
        quantityInput.send_keys(4)
        time.sleep(2)
        addToCartBtn = self.driver.find_element(By.ID,'bntAddToCart')
        addToCartBtn.click()
        time.sleep(3)
        # notification = self.driver.find_element(By.XPATH,'//*[@id="swal2-content"]')
        # assert notification == 'Số lượng mua phải lớn hơn 0' or  notification == 'Số lượng mua tối đa 5 cuốn cho 1 tên sách'
        # assert notification == "" 

    def test_6(self): #done
        self.driver.get("https://mybk.hcmut.edu.vn/bookstore/product/2")
        quantityInput = self.driver.find_element(By.XPATH,'//*[@id="txtQuantity"]')
        quantityInput.clear()
        quantityInput.send_keys(5)
        time.sleep(2)
        addToCartBtn = self.driver.find_element(By.ID,'bntAddToCart')
        addToCartBtn.click()
        time.sleep(3)
        # notification = self.driver.find_element(By.XPATH,'//*[@id="swal2-content"]')
        # assert notification == 'Số lượng mua phải lớn hơn 0' or  notification == 'Số lượng mua tối đa 5 cuốn cho 1 tên sách'
        # assert notification == ""  

    def test_7(self): #done
        self.driver.get("https://mybk.hcmut.edu.vn/bookstore/product/2")
        quantityInput = self.driver.find_element(By.XPATH,'//*[@id="txtQuantity"]')
        quantityInput.clear()
        quantityInput.send_keys(6)
        time.sleep(2)
        addToCartBtn = self.driver.find_element(By.ID,'bntAddToCart')
        addToCartBtn.click()
        time.sleep(3)
        assert self.driver.find_element(By.XPATH,'//*[@id="swal2-content"]')

    # USE_CASE TESTING FROM HERE
    def test_8(self): #done
        self.driver.get("https://mybk.hcmut.edu.vn/bookstore/product/2")
        quantityInput = self.driver.find_element(By.XPATH,'//*[@id="txtQuantity"]')
        quantityInput.clear()
        quantityInput.send_keys(1)
        time.sleep(2)
        addToCartBtn = self.driver.find_element(By.ID,'bntAddToCart')
        addToCartBtn.click()
        time.sleep(2)
        self.driver.get("https://mybk.hcmut.edu.vn/bookstore/cart")
        time.sleep(2)
        checkOutBtn = self.driver.find_element(By.XPATH,'//*[@id="bntCheckout"]')
        checkOutBtn.click()
        time.sleep(2)
        while self.driver.current_url != 'https://mybk.hcmut.edu.vn/bookstore/checkout':
            self.driver.get("https://mybk.hcmut.edu.vn/bookstore/cart")
            time.sleep(2)
            checkOutBtn = self.driver.find_element(By.XPATH,'//*[@id="bntCheckout"]')
            checkOutBtn.click()
            time.sleep(2)  
        informationBtn = self.driver.find_element(By.XPATH,'//*[@id="headingTwo"]/h4/a')
        informationBtn.click()
        time.sleep(2)
        addressInput = self.driver.find_element(By.ID,"txtAddress")
        addressInput.clear()
        addressInput.send_keys('KTX khu A')
        time.sleep(2)
        assert self.driver.current_url == 'https://mybk.hcmut.edu.vn/bookstore/checkout'

    def test_9(self): #done
        self.driver.get("https://mybk.hcmut.edu.vn/bookstore/product/2")
        quantityInput = self.driver.find_element(By.XPATH,'//*[@id="txtQuantity"]')
        quantityInput.clear()
        quantityInput.send_keys(1)
        time.sleep(2)
        addToCartBtn = self.driver.find_element(By.ID,'bntAddToCart')
        addToCartBtn.click()
        time.sleep(2)
        self.driver.get("https://mybk.hcmut.edu.vn/bookstore/cart")
        time.sleep(2)
        self.driver.get("https://mybk.hcmut.edu.vn/bookstore/product/2")
        quantityInput = self.driver.find_element(By.XPATH,'//*[@id="txtQuantity"]')
        quantityInput.clear()
        quantityInput.send_keys(1)
        time.sleep(2)
        addToCartBtn = self.driver.find_element(By.ID,'bntAddToCart')
        addToCartBtn.click()
        time.sleep(2)
        self.driver.get("https://mybk.hcmut.edu.vn/bookstore/cart")
        time.sleep(2)
        while self.driver.current_url != 'https://mybk.hcmut.edu.vn/bookstore/checkout':
            self.driver.get("https://mybk.hcmut.edu.vn/bookstore/cart")
            time.sleep(2)
            checkOutBtn = self.driver.find_element(By.XPATH,'//*[@id="bntCheckout"]')
            checkOutBtn.click()
            time.sleep(2) 
        informationBtn = self.driver.find_element(By.XPATH,'//*[@id="headingTwo"]/h4/a')
        informationBtn.click()
        time.sleep(2)
        addressInput = self.driver.find_element(By.ID,"txtAddress")
        addressInput.clear()
        addressInput.send_keys('KTX khu A')
        time.sleep(2)
        assert self.driver.current_url == 'https://mybk.hcmut.edu.vn/bookstore/checkout'


    def test_10(self): 
        self.driver.get("https://mybk.hcmut.edu.vn/bookstore/product/2")
        quantityInput = self.driver.find_element(By.XPATH,'//*[@id="txtQuantity"]')
        quantityInput.clear()
        quantityInput.send_keys(1)
        time.sleep(2)
        addToCartBtn = self.driver.find_element(By.ID,'bntAddToCart')
        addToCartBtn.click()
        time.sleep(2)
        self.driver.get("https://mybk.hcmut.edu.vn/bookstore/cart")
        time.sleep(2)
        while self.driver.current_url != 'https://mybk.hcmut.edu.vn/bookstore/checkout':
            self.driver.get("https://mybk.hcmut.edu.vn/bookstore/cart")
            time.sleep(2)
            checkOutBtn = self.driver.find_element(By.XPATH,'//*[@id="bntCheckout"]')
            checkOutBtn.click()
            time.sleep(2) 
        informationBtn = self.driver.find_element(By.XPATH,'//*[@id="headingTwo"]/h4/a')
        informationBtn.click()
        time.sleep(2)
        addressInput = self.driver.find_element(By.ID,"txtAddress")
        addressInput.clear()
        time.sleep(2)
        detailBtn = self.driver.find_element(By.XPATH,'//*[@id="headingFive"]/h4/a')
        detailBtn .click()
        time.sleep(1)
        confirmBtn = self.driver.find_element(By.XPATH,'//*[@id="bntOrder"]/span')
        confirmBtn.click()
        time.sleep(2)
        assert self.driver.find_element(By.XPATH,'//*[@id="swal2-content"]')



    def test_11(self): #done
        self.driver.get("https://mybk.hcmut.edu.vn/bookstore/product/2")
        quantityInput = self.driver.find_element(By.XPATH,'//*[@id="txtQuantity"]')
        quantityInput.clear()
        quantityInput.send_keys('a')
        time.sleep(2)
        addToCartBtn = self.driver.find_element(By.ID,'bntAddToCart')
        addToCartBtn.click()
        time.sleep(3)
        assert self.driver.find_element(By.XPATH,'//*[@id="swal2-content"]')

    def test_12(self): #done
        self.driver.get("https://mybk.hcmut.edu.vn/bookstore/product/2")
        quantityInput = self.driver.find_element(By.XPATH,'//*[@id="txtQuantity"]')
        quantityInput.clear()
        quantityInput.send_keys(-1)
        time.sleep(2)
        addToCartBtn = self.driver.find_element(By.ID,'bntAddToCart')
        addToCartBtn.click()
        time.sleep(3)
        assert self.driver.find_element(By.XPATH,'//*[@id="swal2-content"]')

    def test_13(self): #done
        self.driver.get("https://mybk.hcmut.edu.vn/bookstore/product/2")
        quantityInput = self.driver.find_element(By.XPATH,'//*[@id="txtQuantity"]')
        quantityInput.clear()
        quantityInput.send_keys(6)
        time.sleep(2)
        addToCartBtn = self.driver.find_element(By.ID,'bntAddToCart')
        addToCartBtn.click()
        time.sleep(3)
        assert self.driver.find_element(By.XPATH,'//*[@id="swal2-content"]')

    def tearDown(self):
        self.driver.get("https://mybk.hcmut.edu.vn/my/homeSSO.action")
        logoutBtn = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/a[1]")
        logoutBtn.click()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()