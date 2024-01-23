from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch the web browser and open the URL
driver = webdriver.Chrome()
driver.get("https://gavani.vn/")

# Find the login button and click on it
login_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Đăng nhập"))
)
login_button.click()

email_field = driver.find_element(By.ID, "customer_email")
email_field.send_keys("tranhuy2359@gmail.com")

password_field = driver.find_element(By.ID, "customer_password")  
password_field.send_keys("huy123456")

login_button = driver.find_element(By.XPATH, "//button[text()='Đăng nhập']")
login_button.click()


driver.quit()