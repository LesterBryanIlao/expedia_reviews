from configparser import ConfigParser
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

parser = ConfigParser()
parser.read('project.config')

google_driver = parser.get('webdriver', 'driver_file_path')

service = Service(google_driver)
chrome_options = Options()
chrome_options.add_argument("--headless")

# driver = webdriver.Chrome(service=service, options=chrome_options)
driver = webdriver.Chrome(service=service)
driver.delete_all_cookies()

driver.get('https://www.expedia.com/Hotel-Search?adults=2&d1=2023-08-06&d2=2023-08-11&destination=Philippines&endDate=2023-08-11&flexibility=0_DAY&regionId=145&rooms=1&semdtl=&sort=RECOMMENDED&startDate=2023-08-06&theme=&useRewards=false&userIntent=')
driver.maximize_window()
sleep(10)

show_more_button = None
start = time.time()

while True and (time.time() - start < 120):
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	sleep(5)

	show_more_button = driver.find_element(By.CSS_SELECTOR, 'button.uitk-button.uitk-button-medium.uitk-button-secondary')

	if show_more_button is not None:
		show_more_button.click()
		sleep(5)
	else:
		break
#
# sleep(120)
#
# going_to_button = driver.find_element(By.XPATH, '//*[@id="destination_form_field-menu"]/div/div/div[1]/button')
# # going_to_button = driver.find_element(By.CSS_SELECTOR, 'button[data-stid="destination_form_field-menu-trigger"]')
# going_to_button.click()
#
# sleep(2)
# actions = ActionChains(driver)
# going_to_input = driver.find_element(By.XPATH, '//*[@id="destination_form_field"]')
# # going_to_input = driver.find_element(By.CSS_SELECTOR, 'input[data-stid="destination_form_field-menu-input"]')
# actions.click(going_to_input).send_keys('Philippines').send_keys(Keys.ENTER).perform()
#
# sleep(2)
# search_button = driver.find_element(By.XPATH, '//*[@id="search_button"]')
# search_button.click()
#
# sleep(60)