# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("https://www.cricbuzz.com/")
#
# import time
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.get("https://www.cricbuzz.com/")
# time.sleep(5)



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.cricbuzz.com/")



