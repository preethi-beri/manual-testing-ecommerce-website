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

# Open menu

driver.find_element(By.ID, "react-burger-menu-btn").click()

# Wait

time.sleep(2)

# Click logout

driver.find_element(By.ID, "logout_sidebar_link").click()

# Wait

time.sleep(2)

# Validate logout

if "saucedemo" in driver.current_url:
    print("TEST PASSED: Logout Successful")
else:
    print("TEST FAILED")

# Wait before closing

time.sleep(2)

# Close browser

driver.quit()
