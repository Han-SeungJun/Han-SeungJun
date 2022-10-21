from symbol import encoding_decl
import streamlit as st
from streamlit_folium import st_folium
import folium
import pandas as pd
import numpy as np
from PIL import Image
import csv

path = "C:/Projects/Han-SeungJun/webcrawling_practice/beloved_church_address_mapping/"
csv_file = "beloved_church_maps.csv"
img_path = path + "informaion_banner/"
img_file1 = "beloved_church_information_banner.jpg"
img_file2 = "church_information.jpg"
img_file3 = "church_information2.jpg"

# 페이지 기본설정
st.set_page_config(
    page_icon="🌏",
    page_title="전세계 사랑하는 교회 위치",
    layout="wide",
)

st.header("사랑하는 교회 위치⛪")
st.subheader("서울, 국내 및 해외 지교회 위치를 알 수 있습니다.")
st.write("###### ")
st.write("###### (※ 버까시 및 아프리카 지교회의 위치 및 주소는 정확하지 않습니다.)")    

# 사랑하는 교회 주소 데이터프레임 불러오기
def read_dataframe():
    csv_list = []
    with open(path + csv_file, 'rt', encoding='utf-8') as f:
        read_csv = csv.reader(f)
        
        for line in read_csv:
            csv_list.append(line)

        df = pd.DataFrame(csv_list)
        df=df.rename(columns=df.iloc[0])
        df=df.drop(df.index[0])
    return df

df_address_data_csv = read_dataframe()
df_address_data_csv.drop(['위도', '경도'], axis = 1, inplace = True)

st.write("---")
st.write("#### 사랑하는 교회 리스트 보기")
df_address_data_csv
df_address_data_csv = read_dataframe()

# center(seoul_church_address) on render Folium map in streamlit
seoul_center = [df_address_data_csv["위도"][1], df_address_data_csv["경도"][1]]
my_map = folium.Map(location = seoul_center, zoom_start = 16)

# legend_txt = '<span style="color: {col};">{txt}</span>'

# group0 = folium.FeatureGroup(name='<span style="color: {col};">{txt}</span>'

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
            
#             fg = folium.FeatureGroup(name= legend_txt.format(txt= txt, col= color))
#             my_map.add_child(fg)
    except ValueError as e:
        continue

# my_map.add_child(folium.map.LayerControl('topleft', collapsed= True))

st.write("---")
st.write("#### 사랑하는 교회 위치 찾아보기")
st.write("###### (※ 핀을 터치하면 주소와 전화번호를 알 수 있습니다.)")
st_data = st_folium(my_map, width = 1080)

st.write("---")
try:
    image1 = Image.open(img_path + img_file1)
    st.image(image1)

    image2 = Image.open(img_path + img_file2)
    st.image(image2)

    image3 = Image.open(img_path + img_file3)
    st.image(image3, caption='사랑하는 교회 소개')
except FileNotFoundError as e:
    st.exception("이미지 파일을 불러오는데 실패했습니다.")

st.sidebar.markdown("※ 관련 링크")
st.sidebar.markdown("[사랑하는 교회 다음카페](https://cafe.daum.net/Bigchurch)")
st.sidebar.markdown("[교회 공식 홈페이지](http://www.belovedc.com/)")
st.sidebar.markdown("[교회 공식 블로그](https://blog.naver.com/belovedc)")
st.sidebar.markdown("[천국의 도서관(서점)](https://www.gfcbook.com:14070/shop/main/index.php)")
st.sidebar.markdown("[교회 공식 유튜브 채널](https://www.youtube.com/c/gfctvmedia)")
st.sidebar.markdown("[개발 소스코드 보기](https://github.com/Han-SeungJun/Han-SeungJun/tree/main/webcrawling_practice/beloved_church_address_mapping/)")
st.text("개발자 : Han-SeungJun")
