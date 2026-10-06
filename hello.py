from selenium import  webdriver
from pages.login import LoginPage
from pages.events import EventsPage
from pages.HomeDashboard import HomeDashboard
driver = webdriver.Firefox()
driver.implicitly_wait(10)
event_page = EventsPage(driver)
login_page = LoginPage(driver)
home_dashboard = HomeDashboard(driver)
login_page.navigateTo("https://eventhub.rahulshettyacademy.com/login")
login_page.login("admin@gmail.com","Admin@12345")
home_dashboard.click_events()
event_page.click_add_new_event()
event_page.new_event("Hellos","desc","Sports","hello","sded","01-01-2027 01:01 AM","111","22","https://www.google.com")
