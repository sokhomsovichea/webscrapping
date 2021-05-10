# from termcolor import colored
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import requests
# import gspread

# # connect to spreadsheet
# gc = gspread.service_account(filename='credentials.json')
# sh = gc.open('Quill Automation').worksheet("B2")

# DefinitionCol = "B"
# ParaphrasedCol = "C"
# StartRow = 2
# numberofDefinition = 3
# DefinitionCol = ord(DefinitionCol)-64
# ParaphrasedCol = ord(ParaphrasedCol)-64

# # using selenium to do the automation
# Path = '/home/vichea/Downloads/chromedriver_linux64/chromedriver'

# driver = webdriver.Chrome(Path)

# #  XPath
# para_button = '//*[@id="InputBottomQuillControl"]/div/div/div/div[2]/div/div/div/div/button'  #paraphrase button
# input_box = '//*[@id="inputText"]'  #input field


# # create text file for starting row number
# from os import path
# if (path.exists("StartingRow.txt")):
#     print(colored('File Existed', 'yellow'))
# else:
#     f = open("StartingRow.txt", "w")
#     f.write(str(StartRow))
#     f.close()
#     print(colored('File Created', 'green'))
# with open('StartingRow.txt', 'r') as reader:
#     StartRow = int(reader.read())

# driver.get('https://quillbot.com/')

# try:
#     for j in range(3):
#         content = sh.cell(StartRow+j, DefinitionCol)
#         content = str(content).split("'")[1]

#         driver.find_element_by_xpath(input_box).send_keys(content)   #input text
#         driver.find_element_by_xpath(para_button).click()   #auto click the button
#         print('$')

#         # getting the output
#         result = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.CLASS_NAME, "first-sentence-half"))
#         )
#         print(result.text)
#         sh.update_cell(StartRow+j, ParaphrasedCol, result.text)
#         driver.find_element_by_id('inputText').clear()

#         f = open('StartingRow.txt', 'w')
#         f.write(str((StartRow+j)+1))
#         f.close

# finally:
#     driver.quit()

# driver.quit()
# print(colored('Finished', 'green'))
from os import path
et = 0
if (path.exists("ExecutionTimes.txt")):
    print(path)
else:
    f = open("ExecutionTimes.txt", "w")
    f.write(str((et)+1))
    f.close()

with open("ExecutionTimes.txt", "r") as reader:
    et = int(reader.read())

f = open("ExecutionTimes.txt", "w")
f.write(str((et)+1))
f.close()