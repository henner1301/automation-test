from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()


driver.get("https://gavani.vn/")


driver.find_element(By.LINK_TEXT, "Tài khoản").click()


wait = WebDriverWait(driver, 10)
create_account_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Đăng ký tại đây")))
create_account_link.click()

search_input = driver.find_element(By.XPATH, "//input[@name='customer[last_name]']")
search_input.send_keys("Trần")

search_input = driver.find_element(By.XPATH, "//input[@name='customer[first_name]']")
search_input.send_keys("Huy")

search_input = driver.find_element(By.XPATH, "//input[@name='customer[phone]']")
search_input.send_keys("0364052359")

search_input = driver.find_element(By.XPATH, "//input[@name='customer[email]']")
search_input.send_keys("tranhuy2359@gmail.com")

search_input = driver.find_element(By.XPATH, "//input[@name='customer[password]']")
search_input.send_keys("huy123456")
wait = WebDriverWait(driver, 10)


register_button = driver.find_element(By.XPATH, "//button[text()='Đăng ký']")
register_button.click()

wait = WebDriverWait(driver, 10)

wait.until(EC.url_contains("login"))  


print(driver.current_url) 



