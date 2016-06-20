from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# create a new Chrome session (R.I.P: starting with version 47 Firefox is no longer supported)
driver = webdriver.Chrome()
driver.maximize_window()

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
lists = driver.find_elements_by_class_name("_Rm")

# get the number of elements found
print ("Found " + str(len(lists)) + "searches:")

# iterate through each element and print the text that is
# name of the search
i = 0
for listitem in lists:
    print (listitem)
    i = i + 1
    if (i > 10):
        break

# close the browser window
driver.quit()