from scripts.crawling.melon_lyrics_selenium_scraper import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, os
import pandas as pd

options = Options()
driver = webdriver.Edge()
driver.get("https://www.melon.com/chart/index.htm")

title = driver.find_element(By.CSS_SELECTOR, "input#top_search.ui-autocomplete-input")
title.clear()
title.send_keys("안녕하세요 러브홀릭" + Keys.ENTER)

table_element = driver.find_element(By.CSS_SELECTOR, "table")
target = table_element.find_elements(By.CSS_SELECTOR, "tbody .pd_none a")[0] 
js_code = target.get_attribute("href")
table_html = table_element.get_attribute('outerHTML')
table = pd.read_html(table_html)[0]
table["js"] = js_code
driver.execute_script(js_code)
table["link"] = driver.find_element(By.ID,"d_video_summary").text # 가사

driver.quit()
