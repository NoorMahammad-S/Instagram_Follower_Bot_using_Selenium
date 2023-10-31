from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

USERNAME = "Your user Name"
PASSWORD = "Password"
SIMILAR_ACCOUNT = "similar account"  #follwers from that account

chrome_path_driver = "chromedriver.exe" #you have to give chromedriver location
driver = webdriver.Chrome(executable_path=chrome_path_driver)


class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        user_name = self.driver.find_element(By.NAME, "username")
        user_name.send_keys(USERNAME)
        time.sleep(1)

        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)
        time.sleep(1)

        password.send_keys(Keys.ENTER)
        time.sleep(5)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/")
        time.sleep(3)


        modal = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

bot = InstaFollower(chrome_path_driver)
bot.login()
bot.find_followers()
bot.follow()
