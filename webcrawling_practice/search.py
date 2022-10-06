from bs4 import BeautifulSoup
import requests

def _search(keyword_input):
    
    base_url = "https://search.naver.com/search.naver?where=view&sm=tab__jum&query="

    keyword = keyword_input

    search_url = base_url + keyword

    r = requests.get(search_url)

    soup = BeautifulSoup(r.text, "html.parser")

    items = soup.select(".api_txt_lines.total_tit")

    article = []
    
    for rank_num, item in enumerate(items, 1):
        article.append(f"{rank_num} : {item.text}")
        
    return article
