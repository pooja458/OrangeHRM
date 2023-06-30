'''
Created on 26-Apr-2023

@author: PoojaP10
'''
class HomePage():
    
    def __init__(self,driver):
        self.driver = driver
        
        self.welcome_link_id = "welcome"
        self.logout_link_linkTest = "Logout"
        
    def click_welcome(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()
        
    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_linkTest).click()
        
     
        