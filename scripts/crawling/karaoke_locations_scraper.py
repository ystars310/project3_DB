"""
코드 수정해서 넣어둘 것
"""

# rockq
import requests
from bs4 import BeautifulSoup
import pandas as pd
rows = []
for page in range(1,18):
    url = f"https://www.rockq.co.kr/franchise/list?area=&area2=&area2&text=&page={page}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    soup.find_all("ul>li")
    fran_list = soup.select("#content >ul>li")
    
    for li in fran_list:
        info = li.find("div", class_="info")
        if not info:
            continue
        name = info.find("span", class_="tit").text.strip()
        tel = info.find("span", class_="tel").text.strip()
        addr = info.find("span", class_="txt").text.strip()
        rows.append({"name": name, "tel": tel, "address": addr})
rows
df = pd.DataFrame(rows)
df.to_csv("rockq.csv",index=False,encoding="cp949")

# 7starcoin
from scripts.crawling.melon_lyrics_selenium_scraper import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time, requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
# 크롬 드라이버 옵션 (필요하면 headless도 가능)
options = Options()
driver = webdriver.Edge(options=options)
driver.get("https://www.7starcoin.co.kr")
dfs=list()
n=31
for n in range(n, n+10):
    time.sleep(2)
    try:
        driver.switch_to.frame("main")
    except:
        pass
    tables = driver.find_elements(By.TAG_NAME, "table")
    rows = tables[0].find_elements(By.TAG_NAME, "tr")
    data = []
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        if cols:
            link = row.find_element(By.TAG_NAME, "a").get_attribute("href")
            data.append([col.text for col in cols]+[link])
    print(i)
    num_selector = driver.find_element(By.CLASS_NAME,"ppag")
    num_list = num_selector.find_elements(By.TAG_NAME,"a")
    
    select_num = [i.text==str(n) for i in num_list]
    select_num = int(np.where(select_num)[0])
    num_list[select_num].click()
    df = pd.DataFrame(data)
    dfs.append(df)
    print(df)

df = pd.concat(dfs,ignore_index=True)
df.to_csv("seven_star.csv",index=False,encoding="cp949")

df["address"]=""
df["phone_num"]=""
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36'
}

for idx, url in enumerate(df.loc[:,5]):
    response = requests.get(url, headers=headers)
    response.encoding = 'euc-kr' 
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', class_='ep_board7 bLine')
    address = None
    for tr in table.find_all('tr'):
        th = tr.find('th').get_text(strip=True)
        if th == '주소':
            address = tr.find('td').get_text(strip=True)
        if th == "전화번호":
            phone_num = tr.find('td').get_text(strip=True)
    df.loc[idx, "address"] = address
    df.loc[idx, "phone_num"] = phone_num

df
df.to_csv("seven_star.csv",index=False,encoding="cp949")
# angelscoin
import time, requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
dfs = list()
for page in range(1,6):
    url = f"https://www.angelscoin.co.kr/child/sub/spot/?ptype=&page={page}&code=spot"
    response = requests.get(url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find("table", class_="spot-bbs")

    data_list = []

    # 첫 번째 tr은 헤더이므로 제외하고 두 번째 tr부터 반복
    rows = table.find_all('tr')[1:]
    for row in rows:
        tds = row.find_all('td')
        if len(tds) < 2:
            continue
        # 매장명: 첫 번째 td 안 a 텍스트
        store_name = tds[0].find('a').get_text(strip=True)
        # 지역: 두 번째 td 텍스트
        region = tds[1].get_text(strip=True)
        # href: 첫 번째 td 안 a href 속성 (상대경로)
        href = tds[0].find('a')['href']
        
        data_list.append({
            "매장명": store_name,
            "지역": region,
            "href": href
        })

        df = pd.DataFrame(data_list)
        print(df)
        dfs.append(df)
df = pd.concat(dfs,ignore_index=True)
df = df.drop_duplicates()
df=df.reset_index(drop=True)
df.to_csv("angelscoin.csv",index=False,encoding="cp949")
df["address"] = ""

df2=df.copy()
from scripts.crawling.melon_lyrics_selenium_scraper import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time, requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
# 크롬 드라이버 옵션 (필요하면 headless도 가능)
options = Options()
driver = webdriver.Edge(options=options)

for idx, href in enumerate(df["href"]):
    url = f"https://www.angelscoin.co.kr/{href}"
    driver.get(url)
    time.sleep(1)
    table_element = driver.find_elements(By.CSS_SELECTOR, "table")[0]
    address = table_element.find_element(By.CSS_SELECTOR,"td").text
    print(idx, address)
    df.loc[idx,"address"] = address
df = df.merge(df2[["매장명","address"]], how="left")
df.to_csv("angelscoin.csv",index=False,encoding="cp949")
