import csv
from selenium import webdriver

MAX_PAGE_NUM = 16

with open('renrendai.csv', 'w', encoding="utf-8") as table:
    csv_writer = csv.writer(table, delimiter='\t')
    csv_writer.writerow(['项目名称', '项目编号', '项目简介', '项目销售链接', '借款用途', '借款金额（元）', '借款期限', '年化利率',
                         '预计起息日', '还款方式', '还款方式说明', '项目状态', '募集开始时间', '还款保障措施', '还款来源',
                         '项目风险评估', '相关费用', '合同模板号', '出借人适当性管理提示', '借款方类型', '姓名', '证件类型',
                         '证件号码', '工作性质', '其他借款信息', '借款人征信报告情况', '在本平台逾期次数', '在本平台逾期总金额（元）',
                         '借款人收入及负债情况'])

driver = webdriver.Chrome()

for i in range(1, MAX_PAGE_NUM + 1):

    url = 'https://dp.nifa.org.cn/HomePage?method=getTargetProjectInfo&sorganation=911101055548793445&stheonlyid=911101055548793445'\
          +str(2668602+i)+'&sdebtortypeb=01&sfullnames=911101055548793445'

    driver.get(url)

    project_name = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[1]/td[2]')
    project_number = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[2]/td[2]')
    project_intro = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[3]/td[2]')
    project_link = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[4]/td[2]')
    project_purpose = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[5]/td[2]')
    project_size = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[6]/td[2]')
    project_duration = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[7]/td[2]')
    project_APR = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[8]/td[2]')
    project_repay_start = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[9]/td[2]')
    project_repay_method = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[10]/td[2]')
    project_repay_details = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[11]/td[2]')
    project_status = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[12]/td[2]')
    project_raise_start = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[13]/td[2]')
    project_guarantee = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[14]/td[2]')
    project_repay_source = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[15]/td[2]')
    project_risk = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[16]/td[2]')
    project_expense = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[17]/td[2]')
    project_template_number = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[18]/td[2]')
    project_lender_notice = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[19]/td[2]')
    project_borrower_type = driver.find_element_by_xpath('//form/div/div[3]/div/div[1]/table[@class="table"]/tbody/tr[20]/td[2]')

    with open('renrendai.csv', 'a', encoding="utf-8") as table:
        table.write(project_name.text + "\t" + project_number.text + "\t" + project_intro.text + "\t"
                    + project_link.text + "\t" + project_purpose.text + "\t"
                    + project_size.text + "\t" + project_duration.text + "\t" + project_APR.text + "\t"
                    + project_repay_start.text + "\t" + project_repay_method.text + "\t" + project_repay_details.text + "\t"
                    + project_status.text + "\t" + project_raise_start.text + "\t" + project_guarantee.text + "\t"
                    + project_repay_source.text + "\t" + project_risk.text + "\t" + project_expense.text + "\t" + project_template_number.text + "\t"
                    + project_lender_notice.text + "\t" + project_borrower_type.text + "\n")

# Clean up (close browser once task is completed.)
driver.close()
