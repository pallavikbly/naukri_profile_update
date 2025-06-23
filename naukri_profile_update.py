from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Get credentials from GitHub secrets
EMAIL = os.getenv("NAUKRI_EMAIL")
PASSWORD = os.getenv("NAUKRI_PASSWORD")

# Configure headless browser for GitHub Actions
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    # Open Naukri login page
    driver.get("https://www.naukri.com/mnjuser/login")
    wait = WebDriverWait(driver, 15)

    # Fill login form
    wait.until(EC.visibility_of_element_located((By.ID, 'usernameField'))).send_keys(EMAIL)
    wait.until(EC.visibility_of_element_located((By.ID, 'passwordField'))).send_keys(PASSWORD)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))).click()
    print("✅ Logged in successfully.")
    
    # Navigate to profile
    time.sleep(5)
    driver.get("https://www.naukri.com/mnjuser/profile")
    time.sleep(5)

    # Click on 'Key Skills' tab
    key_skill_tab = wait.until(EC.element_to_be_clickable((
        By.XPATH, '//*[@id="root"]/div/div/span/div/div/div/div/div/div[2]/div[1]/div/div/ul/li[4]'
    )))
    key_skill_tab.click()
    time.sleep(3)

    # Click edit button
    edit_btn = wait.until(EC.element_to_be_clickable((
        By.XPATH, '//*[@id="lazyKeySkills"]/div/div/div[1]/span[2]'
    )))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", edit_btn)
    edit_btn.click()
    time.sleep(2)

    # Save the section to trigger update
    save_btn = wait.until(EC.element_to_be_clickable((By.ID, 'saveKeySkills')))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_btn)
    save_btn.click()
    time.sleep(3)

    print("✅ Naukri profile updated successfully!")

except Exception as e:
    print(f"❌ Something went wrong: {e}")

finally:
    driver.quit()
