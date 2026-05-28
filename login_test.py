from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Launch browser

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open SauceDemo website

driver.get("https://www.saucedemo.com/")

# Maximize browser window

driver.maximize_window()

# Enter username

driver.find_element(By.ID, "user-name").send_keys("standard_user")

# Enter password

driver.find_element(By.ID, "password").send_keys("secret_sauce")

# Click login button

driver.find_element(By.ID, "login-button").click()

# Wait for loading

time.sleep(3)


# Validate login
if "inventory" in driver.current_url:
    print("TEST PASSED: Login Successful")
else:
    print("TEST FAILED")



# Wait before closing

time.sleep(2)

# Close browser

driver.quit()
