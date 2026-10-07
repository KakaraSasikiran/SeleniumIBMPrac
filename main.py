from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
driver.get("https://www.google.com")
driver.implicitly_wait(10)
parent = driver.current_window_handle
print(parent)

actions = ActionChains(driver)
ele = driver.find_element(By.LINK_TEXT,"About")
actions.key_down(Keys.CONTROL).click(ele).key_up(Keys.CONTROL).perform()
child = driver.window_handles
print(child)
for tab in child:
    if tab!=parent:
        driver.switch_to.window(tab)
        break
