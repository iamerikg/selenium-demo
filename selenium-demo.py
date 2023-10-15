from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Headless browser configuration
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')

# Path to ChromeDriver (ensure it's in the system PATH)
driver = webdriver.Chrome(options=options)

# Navigate to Google's homepage
driver.get("https://www.google.com")

# Find the search box by its name attribute value
search_box = driver.find_element("name", "q")

# Type a search query
search_box.send_keys("Selenium on AWS EC2")

# Press Enter
search_box.send_keys(Keys.RETURN)

# Wait for a few seconds to ensure the results are loaded
time.sleep(5)

# Print the title of the page
print("Page Title:", driver.title)

# Capture a screenshot (optional)
driver.save_screenshot("/path/to/screenshot.png")

# Close the browser
driver.quit()