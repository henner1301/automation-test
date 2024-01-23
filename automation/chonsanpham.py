from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Khởi tạo trình duyệt
driver = webdriver.Chrome()

# Mở trang chủ của trang web
driver.get("https://gavani.vn/")

# Định danh của sản phẩm (ví dụ: CSS selector)
product_locator = "CSS_SELECTOR_OF_PRODUCT"

# Tìm sản phẩm bằng định danh
product = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, product_locator))
)

# Ấn vào sản phẩm
product.click()

# Tiếp tục thực hiện các bước test khác trên trang sản phẩm

# Đóng trình duyệt
driver.quit()