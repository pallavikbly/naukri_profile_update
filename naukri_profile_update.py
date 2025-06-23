from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time
import traceback

# Load credentials from GitHub secrets (environment variables)
EMAIL = os.getenv("NAUKRI_EMAIL")
PASSWORD = os.getenv("NAUKRI_PASSWORD")

# Configure headless Chrome options
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Start WebDriver
driver = webdriver.Chrome(options=options)

try:
    print("🔄 Opening Naukri login page...")
    driver.get("https://www.naukri.com/mnjuser/login")
    time.sleep(5)  # Allow page to load

    print("🔐 Entering credentials...")
    driver.find_element(By.ID, "usernameField").send_keys(EMAIL)
    driver.find_element(By.ID, "passwordField").send_keys(PASSWORD)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)

    print("🔄 Navigating to profile page...")
    driver.get("https://www.naukri.com/mnjuser/profile")
    time.sleep(6)

    print("📂 Clicking on Key Skills tab...")
    key_skill_tab = driver.find_element(By.XPATH, '//li[contains(text(),"Key Skills")]')
    key_skill_tab.click()
    time.sleep(4)

    print("✏️ Clicking edit button...")
    edit_btn = driver.find_element(By.XPATH, '//*[@id="lazyKeySkills"]/div/div/div[1]/span[2]')
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", edit_btn)
    edit_btn.click()
    time.sleep(3)

    print("💾 Saving skills...")
    save_btn = driver.find_element(By.XPATH, '//*[@id="saveKeySkills"]')
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_btn)
    save_btn.click()
    time.sleep(3)

    print("✅ Naukri profile updated successfully!")

except Exception as e:
    print(f"❌ Exception occurred: {e}")
    traceback.print_exc()
    driver.save_screenshot("error.png")

finally:
    driver.quit()
