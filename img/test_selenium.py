from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import xlrd, xlwt
from xlutils.copy import copy
driver = webdriver.Chrome('chromedriver')
driver.get("http://127.0.0.1:8000")
file_location = "/home/hieu/Desktop/test_selenium/tc_dangnhap.xlsx"
wb = xlrd.open_workbook(file_location,"rb")
# sheetOut = wb.get_sheet(0)
wwb = copy(wb)
sheetOut = wwb.get_sheet(0)
sheet = wb.sheet_by_index(0)
for rows in range(sheet.nrows-1):
	username = driver.find_element_by_name("username")
	password = driver.find_element_by_name("password")
	username.clear()
	password.clear()
	username.send_keys(sheet.cell_value(rows+1, 1))

	password.send_keys(str(int(sheet.cell_value(rows+1, 2))))
	btn_dangnhap = driver.find_element_by_class_name("submit")
	btn_dangnhap.click()
	if(len(driver.find_elements_by_class_name("right_col"))) > 0:
		print("login pass")
		driver.get("http://127.0.0.1:8000/logout/")
		sheetOut.write(rows+1, 3,'pass') 
	else:
		print("faill")
		sheetOut.write(rows+1, 3,'faill') 
	wwb.save('/home/hieu/Desktop/test_selenium/tc_dangnhap.xlsx')
driver.close()