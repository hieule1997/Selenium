from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import xlrd, xlwt
from xlutils.copy import copy
import getpass
import json
import urllib
# file_location = "/home/hieu/Desktop/srcIMG.xlsx"
# wb = xlrd.open_workbook(file_location,"rb")
# sheetOut = wb.get_sheet(0)
# # wwb = copy(wb)
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("user-data-dir=C:\\Users\\"+getpass.getuser()+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default")  # this is the directory for the cookies
driver = webdriver.Chrome('chromedriver')
driver.get("https://www.instagram.com/hyunmi212/")
# driver.set_preference('browser.download.folderList', 2) # custom location
# driver.set_preference('browser.download.manager.showWhenStarting', False)
# driver.set_preference('browser.download.dir', '/tmp')
# driver.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')
# singup = driver.find_element_by_class_name("_0mzm-")
# singup.click()
# username = driver.find_element_by_id("email")
# password = driver.find_element_by_name("pass")
# username.clear()
# password.clear()
# username.send_keys(0397086311)
# password.send_keys(1997@hieule)
list_img = driver.find_elements_by_class_name("FFVAD")
list_path = []
for img in list_img:
    imgpath = img.get_attribute("src")
    list_path.append(imgpath)
    # driver.get(imgpath)
# try:
#     for img_url in list_path:
#         req = urllib2.Request(img_url)
#         raw_img =  .urlopen(req).read()
#         f = open(download_path+searchtext.replace(" ", "_")+"/"+str(downloaded_img_count)+"."+img_type, "wb")
#         f.write(raw_img)
#         f.close
#         downloaded_img_count += 1
# except Exception as e:
#     print ("Download failed:", e)
# finally:
#     print

print(list_path)
driver.close()