from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os


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

    # Find where the element that contains all of the reviews
    reviewsElement = WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.XPATH, 'FillThisIn')))
    
    # Then find all of the reviews by using the class name found in all of the individual reviews
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

except TimeoutException:
    print("Failed to load search bar at www.google.com")
finally:
    browser.quit()


