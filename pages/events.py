from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select
class EventsPage:
    def __init__(self,driver:WebDriver):
        self.driver = driver

    add_new_event = (By.CSS_SELECTOR,"div[class='mt-12 flex justify-center'] button")
    def click_add_new_event(self):
        self.driver.find_element(*self.add_new_event).click()


    title = (By.XPATH,"//input[@id='event-title-input']")
    description = (By.XPATH,"//textarea[@placeholder='Describe the event…']")
    category = (By.CSS_SELECTOR,"select#category")
    city = (By.CSS_SELECTOR,"input#city")
    venue =(By.XPATH,"//input[@id='venue']")
    date = (By.XPATH,"//input[@id='event-date-&-time']")
    price = (By.XPATH,"//input[@id='price-($)']")
    total_seats = (By.CSS_SELECTOR,"input#total-seats")
    image_url = (By.XPATH,"//input[@id='image-url-(optional)']")
    add_event_button = (By.CSS_SELECTOR,"button#add-event-btn")

    def select_category(self,category:str):
        select = Select(self.driver.find_element(*self.category))
        select.select_by_visible_text(category)

    def new_event(self,title,description,category,city,venue,date,price,total_seats,image_url):
        self.driver.find_element(*self.title).send_keys(title)
        self.driver.find_element(*self.description).send_keys(description)
        # self.driver.find_element(*self.category).send_keys(category)
        self.select_category(category)
        self.driver.find_element(*self.city).send_keys(city)
        self.driver.find_element(*self.venue).send_keys(venue)
        self.driver.find_element(*self.date).send_keys(date)
        self.driver.find_element(*self.price).send_keys(price)
        self.driver.find_element(*self.total_seats).send_keys(total_seats)
        self.driver.find_element(*self.image_url).send_keys(image_url)
        self.driver.find_element(*self.add_event_button).click()