from bs4 import BeautifulSoup

# The function that appeded a list and crawled informations.
def inform_list_crawler(_driver):
    html = _driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    address_container = soup.find("div", "map_desc")

    position = soup.find("h3").text
    address = address_container.p.text.split("Tel. ")[0]
    tel = address_container.p.text.split("Tel. ")[1]

    each = {
            "위치":position, "주소":address, "전화번호":tel
    }
    return each
