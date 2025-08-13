from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

start_location = "Teen Hath naka,Thane West, Maharashtra"   
destination_location = "91 Springboard, Vikhroli"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/maps")
time.sleep(4) 

directions_btn = driver.find_element(By.XPATH, "//button[@aria-label='Directions']")
directions_btn.click()
time.sleep(3)

start_box = driver.find_elements(By.XPATH, "//input[@aria-label='Choose starting point, or click on the map...']")[0]
start_box.send_keys(start_location)
time.sleep(1)

dest_box = driver.find_elements(By.XPATH, "//input[@aria-label='Choose destination, or click on the map...']")[0]
dest_box.send_keys(destination_location)
dest_box.send_keys(Keys.ENTER)
time.sleep(6)  

steps = driver.find_elements(By.XPATH, "//div[contains(@class, 'directions-mode-step') or contains(@class, 'section-directions-trip-description')]")
instructions = [s.text for s in steps if s.text.strip() != ""]

if instructions:
    pd.DataFrame({"driving instructions": instructions}).to_excel("sampleExcelsheet.xlsx", index=False)
else:
    print("No steps found")

driver.save_screenshot("sampleScreenshot.png")

print("Done! Saved sampleExcelsheet.xlsx and sampleScreenshot.png")

driver.quit()
