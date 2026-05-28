from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Launch browser

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open website

driver.get("https://www.saucedemo.com/")

# Maximize browser

driver.maximize_window()

# Login

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Wait for loading

time.sleep(2)

# Add product to cart

driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

# Open cart

driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

# Wait

time.sleep(2)

# Validate cart

cart_item = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

if cart_item == "Sauce Labs Backpack":
  print("TEST PASSED: Product added to cart successfully")
else:
  print("TEST FAILED")

# Wait before closing

time.sleep(2)

# Close browser

driver.quit()
