from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = 'https://www.365scores.com/football/league/laliga-11/standings'
path = r'C:\Users\alone\OneDrive\Desktop\cde-b2\Practice\02 Web Scraping\Class 3\chromedriver-win64\chromedriver.exe'
service = Service(path)
service.start()

driver = webdriver.Chrome(path)
driver.get(website)

driver.find_element_by_xpath("//a[@data-ng-click=\"vm.setTabType('League Table & Team Averages')\"]").click()
time.sleep(111)