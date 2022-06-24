from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
from first_methods import methods_cl
import time

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--headless")

chrome_driver_path = 'chromedriver3'

driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

m = methods_cl()
top = m.get_data()

for top_25 in top:

	id_1 = top_25[0]
	IIN = int(top_25[1])
	name_org = top_25[2]
	SumDohod = top_25[3]
	SumRashod = top_25[4]
	Dohod = top_25[5]

	print("ID: ",id_1)
	print("ИННЮЛ: ", IIN)
	print("НаимОрг: ", name_org)
	print("СумДоход: ", SumDohod)
	print("СумРасход: ",SumRashod)
	print("Доход: ", float(Dohod))

	try:
		driver.get('https://zachestnyibiznes.ru/lp/proverka_kontragenta')

		search = driver.find_element(By.XPATH, " //input[@id='query']")

		search.send_keys(IIN)
		search.send_keys(Keys.RETURN)

		time.sleep(3)

		source = driver.page_source
		source2 = str(source)

		source_bs = BeautifulSoup(source2, 'lxml')

		x = source_bs.select('div.m-t-25 br')[0].next_sibling.lstrip()
		print("ФИО директора: ", x)
		print("----------------------")

		time.sleep(7)

	except:
		print("ФИО директора не найдено.")
		print("----------------------")

driver.quit()
