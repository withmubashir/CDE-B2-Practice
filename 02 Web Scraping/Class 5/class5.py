from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Set up Chrome options
options = Options()
options.add_argument("--start-maximized")  # Optional: open browser maximized

# Launch the Chrome browser (no need to provide chromedriver path)
driver = webdriver.Chrome(options=options)

# Open the website
driver.get("https://coinmarketcap.com")  # <-- Replace this with your actual target URL

# Scroll to the bottom of the page to load all content (if needed)
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Wait for new content to load
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Find the table by its class name (update if needed)
try:
    table = driver.find_element(By.CLASS_NAME, "cmc-table")
    rows = table.find_elements(By.TAG_NAME, "tr")

    print(rows[0].text.replace('\n', ' | '))  # Header row

    for row in rows[1:]:
        table_data = row.find_elements(By.TAG_NAME, "td")
        if len(table_data) >= 9:
            rank = table_data[1].text
            name = table_data[2].text
            hour_percent = table_data[3].text
            twentyFour_hour_percent = table_data[4].text
            seven_day_percent = table_data[5].text
            market_cap = table_data[6].text
            volume_24h = table_data[7].text
            c_supply = table_data[8].text
            print(rank, name, hour_percent, twentyFour_hour_percent, seven_day_percent, market_cap, volume_24h, c_supply)

except Exception as e:
    print("Error:", e)

# Close the browser
driver.quit()