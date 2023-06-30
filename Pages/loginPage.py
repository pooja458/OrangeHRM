 '''
Created on 08-Dec-2022
@author: PoojaP10
'''
from selenium.webdriver.common.by import By

class LoginPage():
    def __init__(self,driver):
        self.driver = driver
        
        self.username_textbox_xpath = "//input[@name ='username']"
        self.password_textbox_xpath = "//input [@name='password']"
        self.login_button_xpath = "//button [@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']"
    
    def enter_username(self,username):
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).send_keys("username")
        
        
    def enter_password(self,password):
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).clear()
        self.driver.find_element(By.XPATH, self.password_textbox_xpath).send_keys("password")
        
    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()






























