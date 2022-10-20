# mapping beloved churchs.

import pandas as pd
import numpy as np
import folium
import time
import googlemaps
from inform_crawl import *

from bs4 import BeautifulSoup
from tqdm import tqdm_notebook
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import InvalidSessionIdException

API_KEY = "" # gmaps API 키를 이곳에 넣기. 위도와 경도를 가져오기 위함.

# 네이버지도에서 사랑하는 교회 주소 가져오기
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("headless")

driver = webdriver.Chrome("C:/Projects/Han-SeungJun/webcrawling_practice\
    /beloved_church_address_mapping/driver_manager.exe", options=chrome_options)
driver.implicitly_wait(10)

beloved_church_url = "http://www.belovedc.com/"
driver.get(beloved_church_url)

driver.maximize_window()

church_seoul_map_css = "body > div.main > div.row3 > div > div.main-con-09 > a"
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, church_seoul_map_css))).click()
time.sleep(1)

address_container_list = []

# HTML 파싱하고 서울 본교회 주소 크롤링
address_container_list.append(inform_list_crawler(driver))

# 지교회 검색하기 위해 이동
driver.back()

menu_tab_css = "#gnb_menu5"
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, menu_tab_css))).click()
time.sleep(1)

# 전체 지교회 크롤링(macro)
show_detail_css = "body > div.main.branch_area > div.row1 > div > table:nth-child(4) > tbody > tr > th > a"

for table in range(3):
    for row in range(5):
        for column in range(5):
            css_var1 = table + 2
            css_var2 = row + 1
            css_var3 = column + 1
            area_search_css = css_selector_maker(css_var1, css_var2, css_var3)
            if css_var1 == 2 and css_var2 >= 3:
                # 직할지교회 파트 종료, 다음으로 넘어감 (웹 사이트가 table에 더 이상 없음) 
                continue
            elif css_var1 == 4 and css_var2 >= 2 and css_var3 >= 3:
                # 더이상 웹사이트가 없으므로 지교회 크롤링을 중단
                break
            else:
                try:
                    # 웹사이트가 존재할 경우, 수집 진행
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, str(area_search_css)))).click()
                    driver.switch_to.window(driver.window_handles[1])

                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, show_detail_css))).click()

                    time.sleep(2)
                    address_container_list.append(inform_list_crawler(driver))

                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                except TimeoutException as e:
                    isrunning = 0
                    print("Web crawling macro is terminated..")
                    driver.close()
                    print("web browser window is closed..")
                except InvalidSessionIdException as e:
                    pass
                  
# 주소에 불필요한 우편번호 등을 제거 (불규칙성 때문에 일일히 제거하였음)
address_container_list[2]["주소"] = address_container_list[2]["주소"].split(' | ')[1]
address_container_list[19]["주소"] = address_container_list[19]["주소"].split('|')[1]
address_container_list[22]["주소"] = address_container_list[22]["주소"].replace('50629 ', '')
address_container_list[27]["주소"] = address_container_list[27]["주소"].split('|')[1]
address_container_list[29]["주소"] = address_container_list[29]["주소"].replace('51436|', '').replace('|', ' ')
address_container_list[31]["주소"] = address_container_list[31]["주소"].split('| ')[1]

# 인도네시아 버까시 지교회 주소를 추가(크롤링하는 페이지에서 누락됨)
address_container_list[37]["주소"] = "Ktr. Pelayanan Pajak Pratama Bekasi Utara, Jl. KH. Noer Ali, Kayuringin Jaya, Bekasi, Jawa Barat 인도네시아"
address_container_list[37]["전화번호"] = "(주소 부정확) 62-21-8896-4296"

# 우간다 지교회 추가
positions = ["마라바", "코초게", "음발레", "부티루", "이두디", "마나프와", "부다디리",
            "르와보바", "마틴디", "메리키티", "부케데아","부겜베", "나우요"]

addresses = ["malaba", "kochoge", "Mbale", "Butiru", "Idudi town", "Manafwa", "Budadiri",
           "Lwabagabo", "Masindi", "merikit", "bukedea", "bugembe", "Nauyo"]
    
address_container_list.append(africa_local_church_crawler(address_container_list, positions, addresses, ", Uganda"))
address_container_list.pop()

# 콩고 지교회 추가
positions = ["우비라/송고", "키리바 부타호", "키리바 무센가", "루겐게", "카센가", "부카부", "오락", "산자",
             "카툰가", "카렘베렘베", "세베레", "나무닌디", "카본도지", "카툰구루1", "카레레", "바라카",
             "무롱그웨/말린데", "마토보라", "피지 센터", "비타리로", "미부라", "루람보", "카엔게/카시카"]

addresses = ["uvira", "kiliba Butaho", "", "Lukenge", "kasenga", "bukavu", "", "Sangha", "Katanga", "",
             "severe", "", "", "Katunguru", "", "Baraka", "", "", "", "bitari", "", "", "Kasika"]

address_container_list.append(africa_local_church_crawler(address_container_list, positions, addresses, ", Congo"))
address_container_list.pop()

# 부룬디 지교회 추가
positions = ["카베지", "카뇨샤", "부테레레", "차라마", "가세니", "키분게레", "보고라", "야비시가", "가타라", "마통고", "카얀자",
             "체루", "기쿠요", "미공고", "양잘락", "야비기나", "무양게", "키데레게", "부헤카", "무게라마", "마캄바", "루타나",
             "카요고로", "키바고", "치비토케", "루게레게레", "은다바", "우타쿠라", "키빔바", "키부예", "루게레로", "가세니",
             "람무부라", "가퉁구웨", "마쉬가", "무훼자", "루준구", "사스웨", "부반자", "무진다", "키라사", "마람봐", "얌파라하라",
             "키그와티", "루코바", "무송게", "카부예", "비리지", "치부기자", "무세마", "키바부", "방가", "부라라나", "고로",
             "가홈보", "키룬도", "미타카", "무쿠바노", "카지라바게니", "무게마", "윔비로", "무툰투", "카봉가", "무쿤구", "옌그웨",
             "야카지", "키보가", "부케예", "마반다", "기쿠라조", "무세뉘", "부존디", "펨바", "무게니", "무라니라", "가소뤠",
             "기호마", "은고지", "루투모", "루몽게", "춘다", "야카라", "가테레니", "야쿠구마", "키보마", "무숨바", "야무사사", "야비타카"]

addresses = ["Kabezi", "Kanyosha", "Buterere", "carama", "Gasenyi", "Kibungere", "Bogora", "Bisiga", "Gatara", "Matongo", "Kayanza",
             "Ceru", "Gikuyo", "Migongo", "", "", "Muyange", "Kiderege", "Buheka", "Mugerama", "Makamba", "Rutana", "Kayogoro",
             "Kibago", "Cibitoke", "", "Ndaba", "", "Kibimba", "Kibuye", "Rugerero", "Gasenyi", "", "Gatungurwe", "Mashiga",
             "Muhweza", "", "Saswe", "Bubanza", "Muzinda", "Kirasa, Gitunda", "Maramvya", "", "Kigwati", "Rukoba", "Musonge",
             "Kabuye", "", "Civugiza", "Musema", "Kibavu", "Banga", "Burarana", "", "Gahombo", "Kirundo", "Mitakataka", "Mukubano",
             "Kazirabageni", "Mugerama", "", "Mutuntu Ngomante", "Kabonga", "Mukungu", "", "", "Kivoga", "Bukeye", "Mabanda",
             "Gikurazo", "Musenyi", "Bujondi", "Samumpemba Nyarusange", "Mugeni", "", "Gasorwe", "Gihoma", "Ngozi", "Rutumo",
             "Rumonge", "Cunda", "", "", "", "Kivoma", "Musumba", "", ""]

address_container_list.append(africa_local_church_crawler(address_container_list, positions, addresses, ", Burundi"))
address_container_list.pop()

df_address_data = pd.DataFrame(address_container_list)

# 구글 지도를 이용한 매장의 위치 좌표반환
google_maps_key = API_KEY # 이곳에 google Cloud API키를 입력
gmaps = googlemaps.Client(google_maps_key)

df_address_data["위도"] = np.nan
df_address_data["경도"] = np.nan

# 위 gmapgeoAPI에서 불러온 location에서 위도 lat와 경도 lng만 추출하여 dataframe에 저장
# for idx, rows in tqdm_notebook(df_address_data.iterrows()):
for idx, rows in df_address_data.iterrows():
    if rows["주소"]:
        tmp = gmaps.geocode(rows["주소"], language="ko")
        if tmp:
            lat = tmp[0].get("geometry")["location"]["lat"]
            lng = tmp[0].get("geometry")["location"]["lng"]
            df_address_data.loc[idx, "위도"] = lat
            df_address_data.loc[idx, "경도"] = lng
        else:
            print(idx, rows["주소"])
            
df_address_data.to_csv("./beloved_church_maps.csv", sep = ',', encoding='utf-8')
df_address_data_csv = pd.read_csv("./beloved_church_maps.csv", encoding='utf-8', index_col = 0)

# Map 선언
seoul_center = [df_address_data_csv["위도"][0], df_address_data_csv["경도"][0]]
my_map = folium.Map(location = seoul_center, zoom_start = 11.5)

# Map 타일의 종류들
# tiles = "StamenToner"
# tiles = "http://mt0.google.com/vt/lyrs=m&hl=ko&x={x}&y={y}&z={z}" ==> Standard Road Map
# tiles = "http://mt0.google.com/vt/lyrs=p&hl=ko&x={x}&y={y}&z={z}" ==> Terrain Map
# tiles = "http://mt0.google.com/vt/lyrs=r&hl=ko&x={x}&y={y}&z={z}" ==> Somehow Altered Road Map
# tiles = "http://mt0.google.com/vt/lyrs=s&hl=ko&x={x}&y={y}&z={z}" ==> Satellite Only
# tiles = "http://mt0.google.com/vt/lyrs=y&hl=ko&x={x}&y={y}&z={z}" ==> Hybrid
# tiles = "http://mt0.google.com/vt/lyrs=h&hl=ko&x={x}&y={y}&z={z}"  ==> Roads Only

legend_txt = '<span style="color: {col};">{txt}</span>'

for idx, rows in df_address_data_csv.iterrows():
    if  rows["위치"] == "서울":
        icon = "home"
        color = "darkred"
        icon_color = "white"
        txt = "본교회"
    elif idx <= 10 and idx >= 1:
        icon = "plus-sign"
        color = "red"
        icon_color = "white"
        txt = "직할지교회"
    elif idx <= 41 and idx >= 36:
        icon = "cloud"
        color = "blue"
        icon_color = "white"
        txt = "해외지교회"
    elif idx > 41 and rows["주소"]:
        try:
            if not rows["주소"]:
                pass
            elif rows["주소"][-1] == "a":
                icon = "cloud"
                color = "purple"
                icon_color = "white"
                txt = "우간다"
            elif rows["주소"][-1] == "o":
                icon = "cloud"
                color = "darkgreen"
                icon_color = "white"
                txt = "콩고"
            elif rows["주소"][-1] == "i":
                icon = "cloud"
                color = "orange"
                icon_color = "white"
                txt = "부룬디"
        except TypeError as e:
            pass
    else:
        icon = "plus-sign"
        color = "pink"
        icon_color = "white"
        txt = "국내 지교회"
    
    try:
        # 지도마커 생성
            folium.Marker(
            location = [rows["위도"], rows["경도"]],
            popup = rows["주소"],
            tooltip = rows["위치"] + " 사랑하는교회 " + str(rows["전화번호"]),
            icon = folium.Icon(icon = icon, color = color, icon_color = icon_color)
            ).add_to(my_map)
            
            fg = folium.FeatureGroup(name= legend_txt.format(txt= txt, col= color))
            my_map.add_child(fg)
    except ValueError as e:
        continue
        
my_map.save("beloved church positions.html")
# folium.map.LayerControl('topleft', collapsed= False).add_to(my_map)
my_map.add_child(folium.map.LayerControl('topleft', collapsed= False))
my_map
