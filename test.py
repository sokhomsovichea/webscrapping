from termcolor import colored
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import requests
import gspread
import schedule
import time


# connect to spreadsheet
gc = gspread.service_account(filename='credentials.json')
sh = gc.open('Quill Automation').worksheet("B2")

DefinitionCol = "B"
ParaphrasedCol = "C"
StartRow = 2
numberofDefinition = 3
DefinitionCol = ord(DefinitionCol)-64
ParaphrasedCol = ord(ParaphrasedCol)-64


#  XPath
para_button = '//*[@id="InputBottomQuillControl"]/div/div/div/div[2]/div/div/div/div/button'  #paraphrase button
input_box = '//*[@id="inputText"]'  #input field



def paraphrasing():

    # create text file for starting row number
    from os import path
    if (path.exists("StartingRow.txt")):
        print(colored('File Existed', 'yellow'))
    else:
        f = open("StartingRow.txt", "w")
        f.write(str(StartRow))
        f.close()
        print(colored('File Created', 'green'))
    with open('StartingRow.txt', 'r') as reader:
        StartRow = int(reader.read())

    # using selenium to do the automation
    Path = '/home/vichea/Downloads/chromedriver_linux64/chromedriver'
    driver = webdriver.Chrome(Path)

    driver.get('https://quillbot.com/')

    try:
        for j in range(3):
            content = sh.cell(StartRow+j, DefinitionCol)
            content = str(content).split("'")[1]

            driver.find_element_by_xpath(input_box).send_keys(content)   #input text
            driver.find_element_by_xpath(para_button).click()   #auto click the button

            # getting the output
            result = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "first-sentence-half"))
            )
            sh.update_cell(StartRow+j, ParaphrasedCol, result.text)
            driver.find_element_by_id('inputText').clear()

            f = open('StartingRow.txt', 'w')
            f.write(str((StartRow+j)+1))
            f.close

    finally:
        driver.delete_all_cookies()
        driver.quit()

schedule.every(10).seconds.do(paraphrasing)

while 1:
    schedule.run_pending()
    time.sleep(10)

print(colored('Finished', 'green'))
