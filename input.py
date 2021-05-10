from selenium import webdriver

Path = '/home/vichea/Downloads/chromedriver_linux64/chromedriver'

driver = webdriver.Chrome(Path)
driver.get('https://quillbot.com/')

#  XPath
para_button = '//*[@id="InputBottomQuillControl"]/div/div/div/div[2]/div/div/div/div/button'  #paraphrase button
input_box = '//*[@id="inputText"]'  #input field

# Execution
driver.find_element_by_xpath(input_box).send_keys('a flat piece of plastic or metal with a row of thin teeth along one side, used for making your hair neat; a smaller version of this worn by women in their hair to hold it in place or as a decoration')
driver.find_element_by_xpath(para_button).click()
print(driver.page_source)

