from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
class HomeDashboard:
    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    events = (By.XPATH,"//a[@id='nav-events']")
    def click_events(self):
        self.driver.find_element(*self.events).click()
