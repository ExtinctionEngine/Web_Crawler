from selenium import webdriver

# Open up a Firefox browser and navigate to web page.
driver = webdriver.Chrome()
driver.get("https://dp.nifa.org.cn/HomePage?method=getOperateInfo&currentPage=1")

# Extract lists of "buyers" and "prices" based on xpath
names = driver.find_elements_by_xpath('//tbody[@id="runinfotbody"]//tr//td[2]')

for name in names:
    print (name.text)

# Print out all of the buyers and prices on current page:
# num_page_items = len(buyers)
# for i in range(num_page_items):
#     print(buyers[i].text + ":" + prices[i].text)

# Clean up (close browser once task is completed.)
# driver.close()