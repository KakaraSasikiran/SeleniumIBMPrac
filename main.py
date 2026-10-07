#Handling Multiple Tabs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.google.com")
parent = driver.current_window_handle
print(parent)
actions = ActionChains(driver)
ele = driver.find_element(By.LINK_TEXT,"About")
actions.key_down(Keys.CONTROL).click(ele).key_up(Keys.CONTROL).perform()
tabs = driver.window_handles
print(tabs)
for tab in tabs:
    if tab!=parent:
        driver.switch_to.window(tab)
        break


driver.find_element(By.LINK_TEXT,"News").click()


