from bs4 import BeautifulSoup
import requests

url_site = "https://klubsadprof.ru"
res_spisok_tovar_url = "https://klubsadprof.ru/catalog/rozy/chayno_gibridnye/roza_ogyust_renuar_auguste_renoir/"

def cat_name(url, url_site):
    # Use a breakpoint in the code line below to debug your script.
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    h1 = soup.find('h1', class_='product-detail-title').text
    print(h1.strip())
    article =soup.find('div', class_='product-detail-prop').text
    print(article.strip().replace('Артикул:', '').strip())
    content = soup.find('div', class_='product-description-cover')
    content =content.find('div', class_='tab-active')
    #print(content)
    img = soup.find('div', class_='swiper-wrapper')
    img = img.findAll('img')
    for i in img:
        print(url_site + i.get("src"))
    price = soup.find('span', class_='product-item-price')
    print(price.text.replace(' ₽', ''))




cat_name(res_spisok_tovar_url, url_site)

