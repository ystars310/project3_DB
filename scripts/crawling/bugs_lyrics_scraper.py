import requests, re, tqdm, os, time, random
import pandas as pd
import numpy as np 
from bs4 import BeautifulSoup

from scripts.crawling.utils import pre_processing

"""
제공 받은 데이터에 가사 컬럼을 생성하기 위해 
멜론 사이트의 가사정보를 크롤링하여 생성
"""

export_path = "export"
os.makedirs(export_path, exist_ok=True)

df=pd.read_excel("export/meta.xlsx")
df["bugs_song_id"]=np.nan
url = "https://music.bugs.co.kr/search/track"
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
]
headers = {
    "User-Agent":(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                   (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'),
    "Referer":'https://music.bugs.co.kr',
}

n=0
for idx, (song_name, artist_name) in enumerate(
    tqdm.tqdm(df[["song_name","artist_name"]].values[n:]),n):
    
    time.sleep(random.uniform(0.8, 2))

    headers = {
        "Referer": "https://music.bugs.co.kr",
        "User-Agent": random.choice(user_agents) 
    }
    query = f"{song_name.replace(" ","")} {artist_name.replace(" ","")}"
    query = re.sub(r'\([^)]*\)', '', query)
    params = {
        "q":query,
       "section": "",
        "searchGnbYn": "Y"
    }
    session = requests.Session()
    res = session.get(
        url, headers=headers, params=params)
    
    # 사이트 자단 시 sleep을 주어 차단 풀린 후 수집되게 구현
    while res.status_code == 406:
        time.sleep(600)
        res = session.get(
            url, headers=headers, params=params)
        print(res.status_code)

    soup = BeautifulSoup(res.text, "html.parser")
    inputs = soup.select("table.list > tbody >tr .btnActions")
    if len(inputs):
        song_id = inputs[0].get("artist_id")
        df.loc[idx,"bugs_song_id"] = song_id
        song_url=f"https://music.bugs.co.kr/track/{song_id}"
        song_res = requests.get(song_url, headers=headers)
        soup = BeautifulSoup(song_res.text, 'html.parser')
        lyric_div = soup.select_one(
            '#container > section.sectionPadding.contents.lyrics xmp')
        
        if not lyric_div is None:
            lyric_div = pre_processing(lyric_div)
            df.loc[idx,"lyric"] = lyric_div.text
            
    if idx % 50 ==0:
        df.to_csv(
            f"{export_path}/output_{idx}.csv",
            index=False, encoding="utf-8-sig")
