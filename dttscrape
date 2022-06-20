from fileinput import close
import time
from urllib import response
from xml.etree.ElementTree import Comment
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd



driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://digitalbss.mtn.com.gh/dttm-customer/")
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
#driver.close()

username = driver.find_element(By.ID,'username')
password = driver.find_element(By.ID,'password')
username.clear()
password.clear()

username.send_keys('username')
password.send_keys('password')
driver.find_element(By.ID,'submit').click()


time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div/section/section/div[3]/div[2]/div[1]/div/div[1]/div/div/div").click()
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/ul/li[2]").click()



df = pd.read_excel(r'tickets.xlsx')
tickets = df['Tickets'].tolist()
print (tickets)
complaint_list = []

for ticket in tickets:

    search_element = driver.find_element(By.NAME,"newComment")
    search_element.clear()
    search_element.send_keys(ticket)

    time.sleep(5)

    ticket_status = driver.find_element(By.XPATH, '/html/body/div[1]/section/section/div[3]/div[3]/div[2]/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div/span').text
    province = driver.find_element(By.XPATH, '/html/body/div[1]/section/section/div[3]/div[3]/div[2]/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div[5]/div/div[2]/p').text
    print(ticket_status)
    print(ticket_status == 'CLOSED' or 'RESOLVED')
    if ticket_status == 'CLOSED' or  ticket_status == 'RESOLVED':
        service_id = driver.find_element(By.XPATH, '/html/body/div[1]/section/section/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div/div/div[2]').text
        description = driver.find_element(By.XPATH, '/html/body/div[1]/section/section/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div/div/div[3]/div/div[2]/p').text
        comment =  driver.find_element(By.XPATH, '/html/body/div[1]/section/section/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div/div/div[5]/div/div').text
    else:
        service_id = driver.find_element(By.XPATH, '/html/body/div[1]/section/section/div[3]/div[3]/div[2]/div/div[5]/div/div/div/div/div/div[2]/h6').text
        description = driver.find_element(By.XPATH, '/html/body/div[1]/section/section/div[3]/div[3]/div[2]/div/div[5]/div/div/div/div/div/div[3]/div/div[2]').text
        comment =  driver.find_element(By.XPATH, '/html/body/div[1]/section/section/div[3]/div[3]/div[2]/div/div[5]/div/div/div/div/div/div[5]/div/div').text
   
       
    msisdn = service_id.split('-')[1]
    comment = comment.splitlines()

    complaint = {
        'Ticket' : ticket,
        'Status' : ticket_status,
        'Province' : province,
        'MSISDN' : msisdn,
        'Issue' : description,
        'Comment' : comment[-1],
        'Resolver': comment[-2]

    }

    complaint_list.append(complaint)


df_complaint = pd.DataFrame(complaint_list)

df_complaint.to_excel('complaint.xlsx')

print(df_complaint)

driver.close()


