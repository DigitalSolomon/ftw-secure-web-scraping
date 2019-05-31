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
def store(id, date, stars, title, content):
    # finish this mysql query
   cur.execute('INSERT INTO reviews ....
   cur.connection.commit()

dirpath = os.getcwd()
filepath = dirpath + '/chromedriver'
print('Path to Driver: ' + filepath)
browser = webdriver.Chrome(executable_path = filepath)
browser.get('AmazonListingURLHere')

try:
    # Wait as long as required, or maximum of 5 sec for element to appear
    # If successful, retrieves the element
    element = WebDriverWait(browser,5).until(
         EC.presence_of_element_located((By.XPATH, 'FillThisIn')))

    element.click()

    element = WebDriverWait(browser,5).until(
         EC.presence_of_element_located((By.XPATH, 'FillThisIn')))

    element.click()

    reviewsElement = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, 'FillThisIn')))
    
    reviewChildren = reviewsElement.find_elements_by_class_name("FillThisIn")
    for review in reviewChildren:
        reviewId = review.get_attribute('id')
        date = review.find_element_by_class_name('review-date').get_attribute('innerHTML')
        stars = review.find_element_by_class_name('a-link-normal').get_attribute('title')
        title = review.find_element_by_xpath('.//div[2]/a[2]/span').get_attribute('innerHTML')
        reviewContent = review.find_element_by_xpath('.//div[4]/span/div/div[1]/span').get_attribute('innerHTML')
        print(reviewId)
        print(title)
        print(date)
        print(stars)
        print(reviewContent)
        print('#############')
        # call your database insert function here

except TimeoutException:
    print("Failed to load search bar at www.google.com")
finally:
    browser.quit()


