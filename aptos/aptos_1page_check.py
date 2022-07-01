import time
from sys import platform
from selenium import webdriver


if platform == "linux" or platform == "linux2":
	chrome_driver_path = "./chromedriver"
elif platform == "darwin":
	chrome_driver_path = "./mac/chromedriver"
elif platform == "win32":
	chrome_driver_path = "chromedriver.exe"


driver = webdriver.Chrome(executable_path = chrome_driver_path)

ips = []

driver.maximize_window(),
driver.get('https://www.nodex.run/aptos_test/')
driver.execute_script("document.getElementById('darkmode').click();")
driver.execute_script("document.body.style.zoom='70%'")

while(True):
	for i in range(len(ips)):
		driver.find_element_by_id('node_ip').send_keys(ips[i])
		driver.execute_script("document.getElementById('node_check').click();")
		time.sleep(10)
		driver.find_element_by_id('node_ip').clear()




