from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()  # or Firefox, etc.

driver.get("https://duckduckgo.com")

# Search for something with an infobox (e.g., a movie, person, or show)
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Mutt Movie")
search_box.send_keys(Keys.RETURN)

wait = WebDriverWait(driver, 10)

# Wait for the infobox to appear
infobox = wait.until(
EC.presence_of_element_located((By.CSS_SELECTOR, "[data-react-module-id='titles']"))
)

# Title
title = infobox.find_element(By.CSS_SELECTOR, "h2").text
print("Title:  ", title)

# All the metadata pills (rating, year, runtime, genre)
meta_items = infobox.find_elements(By.CSS_SELECTOR, "li span")
labels = ["", "Year", "Runtime", "Genre"]
for label, item in zip(labels, meta_items):
# Making space to put tags at the beginning of the doc
    if label == "":
        pass
    else:
        print(f"{label}:  ", item.text)

# Pull the description separately because it likes being a diva, I guess
desc = infobox.find_element(By.CSS_SELECTOR, "p").text
print("Description: " + desc)
time.sleep(2)
driver.quit()
