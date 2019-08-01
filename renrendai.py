import csv
from selenium import webdriver

MAX_PAGE_NUM = 16

with open('renrendai.csv', 'w', encoding="utf-8") as table:
    csv_writer = csv.writer(table, delimiter='\t')
    csv_writer.writerow(['项目名称', '项目编号', '项目简介', '项目销售链接', '借款用途', '借款金额（元）', '借款期限', '年化利率',
                         '预计起息日', '还款方式', '还款方式说明', '项目状态', '募集开始时间', '还款保障措施', '还款来源',
                         '项目风险评估', '相关费用', '合同模板号', '出借人适当性管理提示', '借款方类型'])

driver = webdriver.Chrome()

for i in range(1, MAX_PAGE_NUM + 1):
    url = "https://dp.nifa.org.cn/HomePage?method=getOperateInfo&currentPage=" + str(i)

    driver.get(url)

    names = driver.find_elements_by_xpath('//div[@class="mouseover-charts"]//p')
    money_amounts = driver.find_elements_by_xpath('//tbody[@id="runinfotbody"]//tr//td[2]')
    projects_amounts = driver.find_elements_by_xpath('//tbody[@id="runinfotbody"]//tr//td[3]')
    borrowers_amounts = driver.find_elements_by_xpath('//tbody[@id="runinfotbody"]//tr//td[4]')
    lenders_amounts = driver.find_elements_by_xpath('//tbody[@id="runinfotbody"]//tr//td[5]')
    projects_default_rates = driver.find_elements_by_xpath('//tbody[@id="runinfotbody"]//tr//td[6]')
    money_default_rates = driver.find_elements_by_xpath('//tbody[@id="runinfotbody"]//tr//td[7]')

    num_page_items = len(names)
    with open('各平台运营信息.csv', 'a', encoding="utf-8") as table:
        for i in range(num_page_items):
            table.write(names[i].text + "\t" + money_amounts[i].text + "\t" + projects_amounts[i].text + "\t"
                        + borrowers_amounts[i].text + "\t" + lenders_amounts[i].text + "\t"
                        + projects_default_rates[i].text + "\t" + money_default_rates[i].text + "\n")

# Clean up (close browser once task is completed.)
driver.close()
