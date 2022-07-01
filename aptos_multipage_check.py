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

driver.maximize_window()

for i in range(len(ips)):
	driver.switch_to.window(driver.window_handles[i])
	driver.get('https://www.nodex.run/aptos_test/')
	
	driver.execute_script("document.getElementById('darkmode').click();")
	driver.find_element_by_id('node_ip').send_keys(ips[i])
	driver.find_element_by_id('node_check').click()
	driver.execute_script("document.body.style.zoom='70%'")
	driver.execute_script("window.open('');")



while(True):
	for i in range(len(ips)):
		driver.switch_to.window(driver.window_handles[i])
		driver.execute_script("document.getElementById('node_check').click();")
		time.sleep(10)



