from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
class LoginPage:
    def __init__(self,driver:WebDriver):
        self.driver = driver

    emailId = (By.XPATH,"//input[@id='email']")
    password = (By.XPATH,"//input[@id='password']")
    login_button = (By.XPATH,"//button[@id='login-btn']")
    def login(self,email_id:str,password:str):
        self.driver.find_element(*self.emailId).send_keys(email_id)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def navigateTo(self,url:str):
        self.driver.get(url)


