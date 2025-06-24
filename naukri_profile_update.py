from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

EMAIL = os.getenv("NAUKRI_EMAIL")
PASSWORD = os.getenv("NAUKRI_PASSWORD")

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    print("🔄 Opening Naukri login page...")
    driver.get("https://www.naukri.com/mnjuser/login")

    wait = WebDriverWait(driver, 20)

    print("🔐 Entering credentials...")
    email_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="text" and @name="email"]')))
    password_input = driver.find_element(By.XPATH, '//input[@type="password" and @name="password"]')

    email_input.send_keys(EMAIL)
    password_input.send_keys(PASSWORD)

    submit_btn = driver.find_element(By.XPATH, '//button[@type="submit"]')
    submit_btn.click()

    print("⏳ Logging in...")
    time.sleep(5)

    print("📄 Opening profile...")
    driver.get("https://www.naukri.com/mnjuser/profile")
    time.sleep(5)

    print("🛠️ Clicking 'Key Skills' tab...")
    key_skill_tab = wait.until(EC.element_to_be_clickable((By.XPATH, '//li[contains(.,"Key Skills")]')))
    key_skill_tab.click()
    time.sleep(3)

    print("✏️ Clicking edit...")
    edit_btn = driver.find_element(By.XPATH, '//*[@id="lazyKeySkills"]//span[contains(text(),"edit") or contains(text(),"Edit")]')
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", edit_btn)
    edit_btn.click()
    time.sleep(2)

    print("💾 Saving changes...")
    save_btn = driver.find_element(By.ID, "saveKeySkills")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_btn)
    save_btn.click()
    time.sleep(3)

    print("✅ Naukri profile updated successfully!")

except Exception as e:
    print("❌ Exception occurred:", e)

finally:
    driver.quit()
