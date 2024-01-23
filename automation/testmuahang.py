from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.get("https://gavani.vn/")


button = driver.find_element(By.CSS_SELECTOR, 'button.product-item-btn')
button.click()


time.sleep(5)


scroll_element = driver.find_element(By.CSS_SELECTOR, 'button.btn-main')
actions = ActionChains(driver)
actions.move_to_element(scroll_element).perform()

time.sleep(3)


buy_now_button = driver.find_element(By.CSS_SELECTOR, 'button.btn-main')
buy_now_button.click()

time.sleep(5)

search_input = driver.find_element(By.XPATH, "//input[@name='billing_address[full_name]']")
search_input.send_keys("Trần Ngọc Huy")

search_input = driver.find_element(By.XPATH, "//input[@name='checkout_user[email]']")
search_input.send_keys("tranhuy0766@gmail.com")

search_input = driver.find_element(By.XPATH, "//input[@name='billing_address[phone]']")
search_input.send_keys("0981700076")

search_input = driver.find_element(By.XPATH, "//input[@name='billing_address[address1]']")
search_input.send_keys("Hà Nội")


time.sleep(20)


# Các thao tác kiểm tra khác...

driver.quit()