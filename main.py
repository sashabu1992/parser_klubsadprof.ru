from bs4 import BeautifulSoup
import requests

url_site = "https://klubsadprof.ru"
url="https://klubsadprof.ru/catalog/rozy/"
kol_str = 11
kol_str = kol_str + 1


def cat_name(url):
    # Use a breakpoint in the code line below to debug your script.
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    category_name = soup.find('h1', class_='page--title').text
    category_name= category_name.strip()
    return category_name  # Press Ctrl+F8 to toggle the breakpoint.

category_name = cat_name(url);
print(category_name);


def caturl_str(url):
    url_str = []
    url_str.append(url)
    for i in range(2, kol_str):
        url_str_link="https://klubsadprof.ru/catalog/rozy/?PAGEN_2=" + str(i) +"#top_catalog"
        url_str.append(url_str_link)
    return url_str
url_str = caturl_str(url)


def spisok_url(url, url_site):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    tovar_url = soup.findAll('a', class_='bx_catalog_item_images')
    spisok_tovar_url = []
    for i in tovar_url:
      url_linjk_tovar = url_site + i.get("href")
      spisok_tovar_url.append(url_linjk_tovar)
    return spisok_tovar_url


res_spisok_tovar = []
for i in url_str:
    res_spisok_tovar = res_spisok_tovar + spisok_url(i, url_site)

print(res_spisok_tovar)





