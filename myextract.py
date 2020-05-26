from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import pandas as pd
from selenium.webdriver.support.ui import Select

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')

browser = webdriver.Chrome("E:/chromedriver", options=options) #put your own path of chromedriver

browser.get('https://www.topuniversities.com/university-rankings/world-university-rankings/2020')
time.sleep(5)

select = Select(browser.find_element_by_name('qs-rankings_length'))
select.select_by_index(2) #Use 0 for top 25.1 for top 50. 2 for top 100. 3 for 500. 4 for all
time.sleep(5)

soup = BeautifulSoup(browser.page_source)

unis = []
rank = []
country = []
for uni in soup.find_all('tbody')[0].find_all('tr') :
    try:
        rank.append(uni.find('span',class_='rank').text)
        unis.append(uni.find('a', class_='title').text)
        country.append(uni.find('td',class_='country').find('div',class_='td-wrap').text)
    except:
        continue

d = {'Rank':rank, 'University':unis, 'Country':country}
df = pd.DataFrame(data=d)
print(df)
