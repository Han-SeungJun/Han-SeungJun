from bs4 import BeautifulSoup
import requests

base_url = "https://search.naver.com/search.naver?where=view&sm=tab__jum&query="

article = []

def _search(keyword_input):
    article = []
    
    r = requests.get(base_url + keyword_input)

    soup = BeautifulSoup(r.text, "html.parser")

    items = soup.select(".api_txt_lines.total_tit")
    
    for rank_num, item in enumerate(items, 1):
        article.append(f"{rank_num} : {item.text}")
        
    return article


def _search2(keyword_input):
    article = []
    
    r = requests.get(base_url + keyword_input)

    soup = BeautifulSoup(r.text, "html.parser")

    items = soup.select(".total_wrap.api_ani_send")

    for rank_num, item in enumerate(items, 1):

        ad = item.select_one(".link_ad")
        if ad:
            # if advertisement, then skip.
            continue

        blog_title = item.select_one(".sub_txt.sub_name").text

        post_title = item.select_one(".api_txt_lines.total_tit._cross_trigger")
        
        article.append(f"<{rank_num}>\n[{blog_title}]\n{post_title.text}\n{post_title['href']}\n")
    
    return article
