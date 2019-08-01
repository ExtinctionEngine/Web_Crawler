import csv
from selenium import webdriver

MAX_PAGE_NUM = 5
MAX_PAGE_DIG = 3

# Buyers | Price
# name1    price1
# name2    price2

with open('results.csv','w') as f:
    f.write("Buyers,Price \n")

# Open up a Firefox browser and navigate to web page.
driver = webdriver.Firefox()

for i in range(1, MAX_PAGE_NUM +1):
    page_num = (MAX_PAGE_DIG - len(str(i))) * "0" + str(i)
    url = "http://econpy.pythonanywhere.com/ex/" + page_num + ".html"

    driver.get(url)

    # Extract lists of "buyers" and "prices" based on xpath
    buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
    prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

    # Print out all of the buyers and prices on current page:
    num_page_items = len(buyers)
    with open('results.csv', 'a') as f:
        for i in range(num_page_items):
            f.write(buyers[i].text + "," + prices[i].text + "\n")

# Clean up (close browser once task is completed.)
driver.close()