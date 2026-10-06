from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://projects.hackerearth.com/p4/index.html")
header = driver.find_element_by_css_selector(
    "h1[style='margin: 0px; font-size: 2rem; font-weight: bold; text-transform: uppercase;']").text