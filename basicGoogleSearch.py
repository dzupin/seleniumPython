from importlib import reload

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

# If Python 2.7 is used then:  UnicodeEncodeError 'ascii' codec can't encode character u'\u2014' in position 34: ordinal not in range(128)
# Default encoding need to be changed for Python2. However this is only possible when sys module is reloaded.
import sys
if sys.version[0] == '2':
    reload(sys)
    sys.setdefaultencoding('utf-8')
########################################################################################################################

# create a new Chrome session (Firefox R.I.P: starting with version 47 Firefox is no longer supported)
driver = webdriver.Chrome()
driver.maximize_window()
#driver.implicitly_wait(30)

# navigate to Google search page
driver.get("https://www.google.com")

# get the search textbox and prepare it for use (e.g. clean any text that may be there)
search_field = driver.find_element_by_id("lst-ib")
search_field.clear()

# enter search keyword and submit
search_field.send_keys("Selenium WebDriver Python")
search_field.submit()

# get the list of elements (html links of results) which are displayed after the search
# On received Google result page, each result html link is created with "_Rm" class name
resultStats = WebDriverWait(driver,30).until(expected_conditions.presence_of_element_located((By.ID, "resultStats")))
print (resultStats.text)
listResultLinks = driver.find_elements_by_class_name("_Rm")
listResultTitles = driver.find_elements_by_class_name("r")
listResultDetails = driver.find_elements_by_class_name("st")

# get the number of elements found
print ("Listing first " + str(len(listResultLinks)) + " searches:")

# iterate through each element and print the text that is
# name of the search
i=0
listResultLinksCollected = ""
for listItem in listResultLinks:
    i +=1
    print ("Link number " + str(i) + " : " + listItem.text)
    listResultLinksCollected = listResultLinksCollected + listItem.text + " : "

i=0
listResultTitlesCollected = ""
for listItem in listResultTitles:
    i += 1
    print ("Title number " + str(i) + " : "+ listItem.text)
    listResultTitlesCollected = listResultTitlesCollected + listItem.text + " "

i=0
listResultDetailsCollected = ""
for listItem in listResultDetails:
    i += 1
    print ("Details number " + str(i) + " : " + listItem.text)
    listResultDetailsCollected = listResultDetailsCollected + listItem.text + " "


print ("All collected Links: " + listResultLinksCollected)
print ("All collected Titles: " + listResultTitlesCollected)
print ("All collected Details: " + listResultDetailsCollected)

# close the browser window
driver.quit()