from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os
# ...import your database module here

conn = pymysql.connect(host='127.0.0.1',user='root', passwd = 'YourPasswordHere', db = 'mysql',
charset = 'utf8')
cur = conn.cursor()
cur.execute("USE scraperdb")
def store(agency, region, position, plantilla, postingDate, closingDate):
    # finish this mysql query
   cur.execute('INSERT INTO listings ....
   cur.connection.commit()

dirpath = os.getcwd()
filepath = dirpath + '/chromedriver'
print('Path to Driver: ' + filepath)
browser = webdriver.Chrome(executable_path = filepath)
browser.get('JobOpportunitiesListURLHere')

try:
    # Wait as long as required, or maximum of 5 sec for element to appear
    # If successful, retrieves the element
    element = WebDriverWait(browser,5).until(
        EC.presence_of_element_located((By.XPATH, 'FillThisIn')))

    element.click()

    # Find where the element that contains all of the listings
    listingsElement = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, 'FillThisIn')))
    
    # Then find all of the listings by using the class name found in all of the individual listings
    listings = listingsElement.find_elements(By.TAG_NAME, "tr") # get all of the rows in the table
    for row in listings:
        # Get the columns from the table row        
        agency = row.find_elements(By.TAG_NAME, "td")[0] #note: index starts from 0, so 0 is 1st column, 1 is 2nd column, 2 is 3rd column, etc
        print agency.text #prints text from the element

        region = row.find_elements(By.TAG_NAME, "td")[1]
        print region.text

        positionTitle = row.find_elements(By.TAG_NAME, "td")[2]
        print positionTitle.text

        plantilla = row.find_elements(By.TAG_NAME, "td")[3]
        print plantilla.text

        postingDate = row.find_elements(By.TAG_NAME, "td")[3]
        print postingDate.text

        closingDate = row.find_elements(By.TAG_NAME, "td")[4]
        print closingDate.text

        print "######################"
        # call your database insert function here

except TimeoutException:
    print("Failed to load")
finally:
    browser.quit()


