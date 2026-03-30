from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Ask user for movie title
searchTerm = input("What is the movie title? ")
driver = webdriver.Firefox()  # or Firefox, etc.

# TODO: Object for "Movie" Class to be passed

driver.get("https://duckduckgo.com")

# Search for something with an infobox (e.g., a movie, person, or show)
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys(searchTerm + " Movie")
search_box.send_keys(Keys.RETURN)

wait = WebDriverWait(driver, 10)

# Wait for the infobox to appear
infobox = wait.until(
EC.presence_of_element_located((By.CSS_SELECTOR, "[data-react-module-id='titles']"))
)
# TODO: Send Title to Movie Object
# Title
title = infobox.find_element(By.CSS_SELECTOR, "h2").text
print("Title:  ", title)

# TODO: Handle labels better; it differs each movie.
# TODO: Send Labels to Movie Object
# All the metadata pills (rating, year, runtime, genre)
meta_items = infobox.find_elements(By.CSS_SELECTOR, "li span")
labels = ["label1", "label2", "label3", "label4"]
for label, item in zip(labels, meta_items):
# Making space to put tags at the beginning of the doc
    print(f"{label}:  ", item.text)

# TODO: Send Description to Movie Object
# Pull the description separately because it likes being a diva, I guess
desc = infobox.find_element(By.CSS_SELECTOR, "p").text
print("Description: " + desc)
time.sleep(2)
driver.quit()
# TODO: New Object renamed the title

# TODO: Send newly titled Object to markdown: Title for the "file name.md", with the labels up top followed by Year and Runtime in normal paragraph and the description after a ### Description Header

# TODO: Save .md file to system