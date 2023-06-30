'''
Created on 08-Dec-2022

@author: PoojaP10
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class LoginTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\Softwares\\chromedriver.exe")    
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        
    def test_login_valid(self):
        
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        
        user_name = self.driver.find_element(By.XPATH, "//input[@name ='username']")
        user_name.send_keys("Admin")
        password_field = self.driver.find_element(By.XPATH, "//input [@name='password']") 
        password_field.send_keys("admin123")
        
        ##VALIDATION of username and password
        assert user_name.get_attribute("value")=="Admin" , "wrong username"
        print("valid username")
        assert password_field.get_attribute("value")=="admin123" , "wrong password"
        print("valid password")
        
        ##login button
        login_btn = self.driver.find_element(By.XPATH, "//button [@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")
        login_btn.click()
        time.sleep(3)

        drp_dwn_btn = self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span")
        drp_dwn_btn.click()
        time.sleep(2)
        
        log_out = self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a")
        log_out.click()
        
    @classmethod
        
    def tearDownClass(self):
        
        self.driver.close()
        self.driver.quit()
        time.sleep(3)

        print('Testcase pass')

if __name__ == '__main__':
    unittest.main()









