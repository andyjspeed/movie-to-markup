from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Ask user for movie title
searchTerm = input("What is the movie title? ")
driver = webdriver.Firefox()  # or Firefox, etc.

# Empty Object for "Movie" Class to be passed

class Movie:
    def __init__(self, title, description, meta):
        self.title = ""
        self.description = ""
        self.meta = ""

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
# Find Title and Send to the Movie Object.
title = wait.until(
EC.presence_of_element_located((By.CSS_SELECTOR, "h2")))
Movie.title = title.text

# All the metadata pills pulled
meta_items = infobox.find_elements(By.CSS_SELECTOR, "li span")
# Taking just the first 4 and adding them together
labels = ["meta1", "meta2", "meta3", "meta4"]
meta = ""
for label, item in zip(labels, meta_items):
     meta += item.text + " |"
Movie.meta = meta

# Pull the description and send to Movie Object
desc = infobox.find_element(By.CSS_SELECTOR, "p").text
Movie.description = desc
time.sleep(2)
driver.quit()

# Print example before item creation
print(Movie.title)
print(Movie.meta)
print(Movie.description)

# Creation of .md file
with open(f"{Movie.title}.md", "w") as f:
    f.write(f"## {Movie.title}\n")
    f.write(f"{Movie.meta}\n\n")
    f.write(f"### Description\n\n")
    f.write(f"{Movie.description}\n\n")
    f.write(f"---\n")