from symbol import encoding_decl
import streamlit as st
from streamlit_folium import st_folium
import folium
import pandas as pd
import numpy as np
from PIL import Image
# import csv

path = "https://github.com/Han-SeungJun/Han-SeungJun/blob/main/webcrawling_practice/beloved_church_address_mapping/"
csv_file = "beloved_church_maps.csv"
img_path = "https://github.com/Han-SeungJun/Han-SeungJun/tree/main/webcrawling_practice/beloved_church_address_mapping/information_banner"
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

df_address_data = pd.DataFrame([['서울', '서울 송파구 위례성대로22길 27-22 111', '02-586-3079', 37.5073473, 127.1312745],
                                ['남양주', '경기 남양주시 지금동 391-84 2층', '031-566-3079', 37.6150376, 127.1614092],
                                ['부천', '경기도 부천시 부흥로303번길 50, 한양프라자 6층 (중동 1128-2)', '032) 611-3079', 37.4967433, 126.7761009],
                                ['수원', '경기 수원시 장안구 송원로 39 월드타워 6층 수원 사랑하는교회', '031-258-3079', 37.2991413, 127.0067546],
                                ['안산', '경기 안산시 단원구 광덕서로 44 이노프라자 B1', '031-414-3079', 37.3085081, 126.8271859],
                                ['안양', '경기 안양시 만안구 안양로329번길 108 안양월드 2층(정문쪽)', '031) 429-3072', 37.40128929999999, 126.9131233],
                                ['용인', '기도 용인시 처인구 금령로135 (마평동734-5) 희성빌딩 3층', '031-332-3079', 37.2354127, 127.2114284],
                                ['의정부', '경기 의정부시 능곡로 13 ', '031-855-3079 ', 37.7397114, 127.0579593],
                                ['인천', '인천 남동구 남동대로733번길 17 ', '032) 521-1925 ', 37.4477933, 126.7061117],
                                ['일산', '경기도 고양시 일산서구 주엽동 136 2층 사랑하는교회', '031-906-3079', 37.6714756, 126.7566985],
                                ['화성', '경기 화성시 향남읍 평3길 19 회춘플라자 6층', '031)353-0691', 37.1314198, 126.9082135],
                                ['강릉', '강원도 강릉시 율곡로 2745', '033-644-3079', 37.7517605, 128.9051511],
                                ['경주', '경북 경주시 금성로 278 연안빌딩 4층', '(054)773-3079, 070-8832-3079', 35.8423129, 129.2072872],
                                ['광주', '광주 서구 상무시민로 133-9 2,3층', '062)375-3079', 35.1559423, 126.8535421],
                                ['구미', '경북 구미시 인동26길 28 사랑하는교회 3층', '054) 476-3079', 36.0947935, 128.427053],
                                ['대구', '대구 동구 메디밸리로 5-25 대림빌딩 4층 사랑하는교회', ' 053) 961-3079', 35.8618831, 128.6888256],
                                ['대전', '대전 동구 대전로 742, 5층', '042) 487-3079', 36.3262701, 127.4358016],
                                ['목포', '전남 목포시 비파로 31 인암빌딩 4층', '061-282-3079', 34.8015481, 126.4275037],
                                ['부산', '부산 수영구 장대골로 35 사랑하는교회', '051) 505-3093', 35.1591163, 129.1096423],
                                ['서산', '충남 서산시 인지면 무학로 1712 ', '041) 668-3079', 36.755588, 126.427387],
                                ['순천', '전남 순천시 유동1길 29-10 (구 그랑비아또)', '061-722-3079 ', 34.9546323, 127.5181421],
                                ['안동', '경북 안동시 은행나무로 103 2층', '054-841-3079', 36.5683112, 128.6955471],
                                ['양산', '경남 양산시 양산역로 103 6층', '055-383-3079 ', 35.3385114, 129.0291253],
                                ['울산', '울산 중구 함월16길 69 ', '052-287-3079', 35.5797718, 129.3120944],
                                ['원주', '강원 원주시 남원로 597  5층', '033)745-3079', 37.3368856, 127.9500146],
                                ['익산', '전북 익산시 하나로10길 75-9 토성빌딩 3층', '063-833-3079', 35.9624081, 126.9891128],
                                ['전주', '전북 전주시 덕진구 백제대로 820 사랑하는교회', '063-275-3079', 35.8481301, 127.1581744],
                                ['제주', '제주특별자치도 제주시 과원북4길 5  장수한의원 4층', '064-744-3079', 33.481358, 126.4825858],
                                ['제천', '충북 제천시 용두대로 119 2층', '043-643-3079', 37.1411648, 128.2010486],
                                ['창원', '용지로 169번길 13 라이크빌 10층 (용호동)', '055-238-3079', 35.2304347, 128.6809395],
                                ['천안', '천안시 동남구 신촌4로 25 (3층)', '041-577-3079', 36.7885955, 127.124364],
                                ['청주', '충북 청주시 흥덕구 복대동 2835, 호인리더스빌딩 7층', '043-274-3079', 36.606494, 127.4901967],
                                ['춘천', '강원 춘천시 금강로 106 운교프라자 4층', '033-241-3079', 37.8763025, 127.7309246],
                                ['통영', '경상남도 통영시 광도면 죽림2로 49-31', '055-643-3079', 34.8815688, 128.4182461],
                                ['평택', '경기 평택시 평택로 180 3층(우측)', '031-654-3079', 37.0010023, 127.0779933],
                                ['포항', '경북 포항시 북구 장량로 254 정동빌딩 4층', '054-244-3079', 36.082061, 129.4083161],
                                ['뉴욕', '47-14 Glenwood St, Little Neck, NY 11362', '+1-347-470-0086', 40.770956, -73.732466],
                                ['버까시', 'Ktr. Pelayanan Pajak Pratama Bekasi Utara, Jl. KH. Noer Ali, Kayuringin Jaya, Bekasi, Jawa Barat 인도네시아', '(주소 부정확) 62-21-8896-4296', -6.2475344, 106.9800423],
                                ['벤쿠버', '640 Clarkson St New Westminster, BC\\xa0V3M 1C8', '778-870-3079', 49.2031645, -122.9091357],
                                ['시드니', '223 Victoria Rd.  Rydalmere. NSW  2116', '0411-253-854', -33.810126, 151.0302609],
                                ['아틀란타', '3741 Venture Dr. 350, Duluth, GA 30096', '404-308-9155', 33.9551458, -84.13649269999999],
                                ['오사카', 'Osakasi naniwagu motomachi3chome 9-24', '06-6633-3934, 090-3357-1530', 34.6602337, 135.4974586],
                                ['프랑크푸르트', 'Farmstraße 118, 64546, Mörfelden-Walldorf (3층)', '+49 06105-717076', 50.0144384, 8.5848862],
                                ['마라바', 'malaba, Uganda', ' 대략적 위치', 1.373333, 32.290275],
                                ['코초게', 'kochoge, Uganda', ' 대략적 위치', 0.7833334, 34.2000008],
                                ['음발레', 'Mbale, Uganda', ' 대략적 위치', 1.0784436, 34.1810057],
                                ['부티루', 'Butiru, Uganda', ' 대략적 위치', 0.8212320999999999, 34.2949409],
                                ['이두디', 'Idudi town, Uganda', ' 대략적 위치', 0.6248207, 33.6278057],
                                ['마나프와', 'Manafwa, Uganda', ' 대략적 위치', 0.9063599, 34.28660910000001],
                                ['부다디리', 'Budadiri, Uganda', ' 대략적 위치', 1.1711177, 34.33242440000001],
                                ['르와보바', 'Lwabagabo, Uganda', ' 대략적 위치', 0.5333334, 31.39999959999999],
                                ['마틴디', 'Masindi, Uganda', ' 대략적 위치', 1.6873134, 31.7138458],
                                ['메리키티', 'merikit, Uganda', ' 대략적 위치', 1.373333, 32.290275],
                                ['부케데아', 'bukedea, Uganda', ' 대략적 위치', 1.347685, 34.0432575],
                                ['부겜베', 'bugembe, Uganda', ' 대략적 위치', 0.465467, 33.2391334],
                                ['나우요', 'Nauyo, Uganda', ' 대략적 위치', 1.0467289, 34.1825417],
                                ['우비라/송고', 'uvira, Congo', ' 대략적 위치', -3.3728836, 29.1448793],
                                ['키리바 부타호', 'kiliba Butaho, Congo', ' 대략적 위치', -3.2322903, 29.1652303],
                                ['키리바 무센가', np.nan, ' 대략적 위치', np.nan, np.nan],
                                ['루겐게', 'Lukenge, Congo', ' 대략적 위치', -6.2439938, 23.4448063],
                                ['카센가', 'kasenga, Congo', ' 대략적 위치', -10.62279, 26.758289],
                                ['부카부', 'bukavu, Congo', ' 대략적 위치', -2.5123017, 28.8480284],
                                ['오락', np.nan, ' 대략적 위치', np.nan, np.nan],
                                ['산자', 'Sangha, Congo', ' 대략적 위치', 1.4662328, 15.4068079],
                                ['카툰가', 'Katanga, Congo', ' 대략적 위치', -8.8851145, 26.419389],
                                ['카렘베렘베', np.nan, ' 대략적 위치', np.nan, np.nan],
                                ['세베레', 'severe, Congo', ' 대략적 위치', -4.038333, 21.758664],
                                ['나무닌디', np.nan, ' 대략적 위치', np.nan, np.nan],
                                ['카본도지', np.nan, ' 대략적 위치', np.nan, np.nan],
                                ['카툰구루1', 'Katunguru, Congo', ' 대략적 위치', -0.1486334, 30.0650793],
                                ['카레레', np.nan, ' 대략적 위치', np.nan, np.nan],
                                ['바라카', 'Baraka, Congo', ' 대략적 위치', -4.0998638, 29.0935525],
                                ['무롱그웨/말린데', np.nan, ' 대략적 위치', np.nan, np.nan],
                                ['마토보라', np.nan, ' 대략적 위치', np.nan, np.nan],
                                ['피지 센터', np.nan, ' 대략적 위치', np.nan, np.nan],
                                ['비타리로', 'bitari, Congo', ' 대략적 위치', -4.416666999999999, 16.866667],
                                ['미부라', np.nan, ' 대략적 위치', np.nan, np.nan],
                                ['루람보', np.nan, ' 대략적 위치', np.nan, np.nan],
                                ['카엔게/카시카', 'Kasika, Congo', ' 대략적 위치', -2.927778, 28.531389],
                                ['카베지', 'Kabezi, Burundi', ' 대략적 위치', -3.5215271, 29.3598782],
                                ['카뇨샤', 'Kanyosha, Burundi', ' 대략적 위치', -3.4309203, 29.4063234],
                                ['부테레레', 'Buterere, Burundi', ' 대략적 위치', -3.331253, 29.3308425],
                                ['차라마', 'carama, Burundi', ' 대략적 위치', -3.3196452, 29.38718009999999],
                                ['가세니', 'Gasenyi, Burundi', ' 대략적 위치', -3.033333, 29.633333],
                                ['키분게레', 'Kibungere, Burundi', ' 대략적 위치', -3.4421855, 29.973612],
                                ['보고라', 'Bogora, Burundi', ' 대략적 위치', -3.373056, 29.918886],
                                ['야비시가', 'Bisiga, Burundi', ' 대략적 위치', -2.4851142, 30.4641423],
                                ['가타라', 'Gatara, Burundi', ' 대략적 위치', -2.9986697, 29.6615055],
                                ['마통고', 'Matongo, Burundi', ' 대략적 위치', -3.0832329, 29.6080092],
                                ['카얀자', 'Kayanza, Burundi', ' 대략적 위치', -2.9234745, 29.6277775],
                                ['체루', 'Ceru, Burundi', ' 대략적 위치', -2.456408, 30.101914],
                                ['기쿠요', 'Gikuyo, Burundi', ' 대략적 위치', -2.6147685, 30.0730845],
                                ['미공고', 'Migongo, Burundi', ' 대략적 위치', -4.2097833, 29.8771808],
                                ['양잘락', np.nan, ' 대략적 위치', np.nan, np.nan],
                                ['야비기나', np.nan, ' 대략적 위치', np.nan, np.nan],
                                ['무양게', 'Muyange, Burundi', ' 대략적 위치', -4.306900700000001, 29.6848173],
                                ['키데레게', 'Kiderege, Burundi', ' 대략적 위치', -4.235613799999999, 29.6463537],
                                ['부헤카', 'Buheka, Burundi', ' 대략적 위치', -4.2125678, 29.6232657],
                                ['무게라마', 'Mugerama, Burundi', ' 대략적 위치', -4.3114892, 29.598937],
                                ['마캄바', 'Makamba, Burundi', ' 대략적 위치', -4.1384805, 29.803397],
                                ['루타나', 'Rutana, Burundi', ' 대략적 위치', -3.9285639, 29.9898766],
                                ['카요고로', 'Kayogoro, Burundi', ' 대략적 위치', -4.118373, 29.9486133],
                                ['키바고', 'Kibago, Burundi', ' 대략적 위치', -4.2986883, 29.9046594],
                                ['치비토케', 'Cibitoke, Burundi', ' 대략적 위치', -2.9107321, 29.1262613],
                                ['루게레게레', np.nan, ' 대략적 위치', np.nan, np.nan],
                                ['은다바', 'Ndaba, Burundi', ' 대략적 위치', -3.373056, 29.918886],
                                ['우타쿠라', np.nan, ' 대략적 위치', np.nan, np.nan],
                                ['키빔바', 'Kibimba, Burundi', ' 대략적 위치', -3.1285538, 30.6960895],
                                ['키부예', 'Kibuye, Burundi', ' 대략적 위치', -3.6647231, 29.9793177],
                                ['루게레로', 'Rugerero, Burundi', ' 대략적 위치', -3.1506093, 30.7256943],
                                ['가세니', 'Gasenyi, Burundi', ' 대략적 위치', -3.033333, 29.633333],
                                ['람무부라', np.nan, ' 대략적 위치', np.nan, np.nan],
                                ['가퉁구웨', 'Gatungurwe, Burundi', ' 대략적 위치', -3.1880185, 30.5849776],
                                ['마쉬가', 'Mashiga, Burundi', ' 대략적 위치', -2.9640153, 30.6073107],
                                ['무훼자', 'Muhweza, Burundi', ' 대략적 위치', -3.1401251, 30.6245994],
                                ['루준구', np.nan, ' 대략적 위치', np.nan, np.nan],
                                ['사스웨', 'Saswe, Burundi', ' 대략적 위치', -2.9710581, 30.5758163],
                                ['부반자', 'Bubanza, Burundi', ' 대략적 위치', -3.083444, 29.3941596],
                                ['무진다', 'Muzinda, Burundi', ' 대략적 위치', -3.2619682, 29.4179214],
                                ['키라사', 'Kirasa, Gitunda, Burundi', ' 대략적 위치', -3.6056797, 29.3879792],
                                ['마람봐', 'Maramvya, Burundi', ' 대략적 위치', -3.55, 29.966667],
                                ['얌파라하라', np.nan, ' 대략적 위치', np.nan, np.nan],
                                ['키그와티', 'Kigwati, Burundi', ' 대략적 위치', -3.2, 29.366667],
                                ['루코바', 'Rukoba, Burundi', ' 대략적 위치', -3.4029522, 29.9153169],
                                ['무송게', 'Musonge, Burundi', ' 대략적 위치', -3.040887, 29.6406136],
                                ['카부예', 'Kabuye, Burundi', ' 대략적 위치', -3.672728599999999, 30.27025],
                                ['비리지', np.nan, ' 대략적 위치', np.nan, np.nan],
                                ['치부기자', 'Civugiza, Burundi', ' 대략적 위치', -2.994453, 29.7995473],
                                ['무세마', 'Musema, Burundi', ' 대략적 위치', -3.0762993, 29.6699172],
                                ['키바부', 'Kibavu, Burundi', ' 대략적 위치', -3.0524403, 29.6351298],
                                ['방가', 'Banga, Burundi', ' 대략적 위치', -3.373056, 29.918886],
                                ['부라라나', 'Burarana, Burundi', ' 대략적 위치', -3.997099999999999, 29.6925852],
                                ['고로', np.nan, ' 대략적 위치', np.nan, np.nan],
                                ['가홈보', 'Gahombo, Burundi', ' 대략적 위치', -3.016667, 29.766667],
                                ['키룬도', 'Kirundo, Burundi', ' 대략적 위치', -2.5595774, 30.0896313],
                                ['미타카', 'Mitakataka, Burundi', ' 대략적 위치', -3.1539012, 29.3661121],
                                ['무쿠바노', 'Mukubano, Burundi', ' 대략적 위치', -4.2631587, 29.677501],
                                ['카지라바게니', 'Kazirabageni, Burundi', ' 대략적 위치', -4.2678571, 29.6249965],
                                ['무게마', 'Mugerama, Burundi', ' 대략적 위치', -4.3114892, 29.598937],
                                ['윔비로', np.nan, ' 대략적 위치', np.nan, np.nan],
                                ['무툰투', 'Mutuntu Ngomante, Burundi', ' 대략적 위치', -3.7467485, 30.3724545],
                                ['카봉가', 'Kabonga, Burundi', ' 대략적 위치', -4.405544600000001, 29.6704901],
                                ['무쿤구', 'Mukungu, Burundi', ' 대략적 위치', -4.217956099999999, 29.5483357],
                                ['옌그웨', np.nan, ' 대략적 위치', np.nan, np.nan],
                                ['야카지', np.nan, ' 대략적 위치', np.nan, np.nan],
                                ['키보가', 'Kivoga, Burundi', ' 대략적 위치', -3.259948000000001, 29.418619],
                                ['부케예', 'Bukeye, Burundi', ' 대략적 위치', -3.2022369, 29.6267347],
                                ['마반다', 'Mabanda, Burundi', ' 대략적 위치', -4.2722928, 29.7831356],
                                ['기쿠라조', 'Gikurazo, Burundi', ' 대략적 위치', -4.3747927, 29.7854965],
                                ['무세뉘', 'Musenyi, Burundi', ' 대략적 위치', -3.1931795, 29.4054468],
                                ['부존디', 'Bujondi, Burundi', ' 대략적 위치', -3.373056, 29.918886],
                                ['펨바', 'Samumpemba Nyarusange, Burundi', ' 대략적 위치', -3.0578455, 29.4598081],
                                ['무게니', 'Mugeni, Burundi', ' 대략적 위치', -4.119606, 30.0527798],
                                ['무라니라', np.nan, ' 대략적 위치', np.nan, np.nan],
                                ['가소뤠', 'Gasorwe, Burundi', ' 대략적 위치', -2.8334814, 30.2281933],
                                ['기호마', 'Gihoma, Burundi', ' 대략적 위치', -3.4291783, 29.768549],
                                ['은고지', 'Ngozi, Burundi', ' 대략적 위치', -2.9107175, 29.8243599],
                                ['루투모', 'Rutumo, Burundi', ' 대략적 위치', -2.733333, 29.316667],
                                ['루몽게', 'Rumonge, Burundi', ' 대략적 위치', -3.9754049, 29.4388014],
                                ['춘다', 'Cunda, Burundi', ' 대략적 위치', -3.373056, 29.918886],
                                ['야카라', np.nan, ' 대략적 위치', np.nan, np.nan],
                                ['가테레니', np.nan, ' 대략적 위치', np.nan, np.nan],
                                ['야쿠구마', np.nan, ' 대략적 위치', np.nan, np.nan],
                                ['키보마', 'Kivoma, Burundi', ' 대략적 위치', -4.0655325, 29.8654849],
                                ['무숨바', 'Musumba, Burundi', ' 대략적 위치', -3.5473802, 30.353713],
                                ['야무사사', np.nan, ' 대략적 위치', np.nan, np.nan],
                                ['야비타카', np.nan, ' 대략적 위치', np.nan, np.nan]], columns = ["위치", "주소", "전화번호", "위도", "경도"])

# 사랑하는 교회 주소 데이터프레임 불러오기
# def read_dataframe():
#     csv_list = []
#     with open(path + csv_file, 'rt', encoding='utf-8') as f:
#         read_csv = csv.reader(f)
        
#         for line in read_csv:
#             csv_list.append(line)

#         df = pd.DataFrame(csv_list)
#         df=df.rename(columns=df.iloc[0])
#         df=df.drop(df.index[0])
#     return df

# df_address_data_csv = read_dataframe()
# df_address_data_csv = Path(path+csv_file).parents[1]
# st.file_uploader()
df_address_data_print = df_address_data.drop(['위도', '경도'], axis = 1, inplace = False)

st.write("---")
st.write("#### 사랑하는 교회 리스트 보기")
df_address_data_print
# df_address_data = read_dataframe()
# center(seoul_church_address) on render Folium map in streamlit
seoul_center = [df_address_data["위도"][0], df_address_data["경도"][0]]
my_map = folium.Map(location = seoul_center, zoom_start = 16)

# legend_txt = '<span style="color: {col};">{txt}</span>'

# group0 = folium.FeatureGroup(name='<span style="color: {col};">{txt}</span>'

for idx, rows in df_address_data.iterrows():
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
