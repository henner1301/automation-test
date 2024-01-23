from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()  


driver.get("https://gavani.vn/")

# Nhap du lieu tim kiem
search_input = driver.find_element(By.XPATH, "//input[@name='q']")
search_input.send_keys("áo sơ mi")


search_input.send_keys(Keys.RETURN)


driver.implicitly_wait(10)  


if driver.find_elements(By.TAG_NAME, "h1"):
    h1_element = driver.find_element(By.TAG_NAME, "h1")
    if h1_element.text == "Nhập từ khóa để tìm kiếm":
        print("No search results found.")
      
        if driver.find_elements(By.TAG_NAME, "h2"):
            h2_element = driver.find_element(By.TAG_NAME, "h2")
            print("Kết quả tìm kiếm: ", h2_element.text)
    else:
        print("H1 heading text: ", h1_element.text)

else:
    print("No search results found.")


time.sleep(10)

driver.quit()