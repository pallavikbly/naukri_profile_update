from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
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
    driver.get("https://www.naukri.com/")
    time.sleep(3)

    
    driver.get("https://www.naukri.com/mnjuser/login")

    #driver.find_element(By.LINK_TEXT, "Login").click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//input[@placeholder="Enter your active Email ID / Username"]').send_keys(EMAIL)
    driver.find_element(By.XPATH, '//input[@placeholder="Enter your password"]').send_keys(PASSWORD)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)

    driver.get("https://www.naukri.com/mnjuser/profile")
    time.sleep(5)

    key_skill_tab = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/span/div/div/div/div/div/div[2]/div[1]/div/div/ul/li[4]')
    key_skill_tab.click()
    time.sleep(3)

    edit_btn = driver.find_element(By.XPATH, '//*[@id="lazyKeySkills"]/div/div/div[1]/span[2]')
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", edit_btn)
    edit_btn.click()
    time.sleep(2)

    save_btn = driver.find_element(By.XPATH, '//*[@id="saveKeySkills"]')
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", save_btn)
    save_btn.click()
    time.sleep(3)

    print("✅ Naukri profile updated successfully!")

except Exception as e:
    print("❌ Something went wrong:", e)

finally:
    driver.quit()
