import time

import xlsxwriter
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fetchData():

    workbook = xlsxwriter.Workbook("TataShare.xlsx")
    worksheet = workbook.add_worksheet("firstSheet")

    worksheet.write(0, 0, "#")
    worksheet.write(0, 1, "Share Price")
    worksheet.write(0, 2, "Date and Time")
    worksheet.write(0, 3, "Up or Down")

    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'q')))
    search_box.send_keys("Tata Share Price")
    search_box.send_keys(Keys.RETURN)

    for index in range(10000):



        share_price = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="knowledge-finance-wholepage__entity-summary"]/div[3]/g-card-section/div/g-card-section/div[2]/div[1]/span[1]/span/span[1]')))
        date_time = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="knowledge-finance-wholepage__entity-summary"]/div[3]/g-card-section/div/g-card-section/div[2]/div[1]/div[1]/span[1]/span[2]')))
        up_down = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="knowledge-finance-wholepage__entity-summary"]/div[3]/g-card-section/div/g-card-section/div[2]/div[1]/span[2]/span[1]')))

        print(share_price.text)
        print(date_time.text)
        print(up_down.text)

        worksheet.write(index + 1, 0, str(index))
        worksheet.write(index + 1, 1, share_price.text)
        worksheet.write(index + 1, 2, date_time.text)
        worksheet.write(index + 1, 3, up_down.text)
        driver.refresh()
        time.sleep(5)

    workbook.close()


if __name__ == '__main__':
    fetchData()
