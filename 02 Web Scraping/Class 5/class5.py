from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.get('https://realpython.github.io/fake-jobs/')

driver.quit()