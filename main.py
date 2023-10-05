from bs4 import BeautifulSoup
import requests
import csv

url_site = "https://klubsadprof.ru"
url="https://klubsadprof.ru/catalog/zemlyanika-sadovaya/"
kol_str = 5
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
        url_str_link=url + "?PAGEN_2=" + str(i) +"#top_catalog"
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



for i in res_spisok_tovar:
    def cat_name(url, url_site, category_name):
        # Use a breakpoint in the code line below to debug your script.
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        try:
            h1 = soup.find('h1', class_='product-detail-title').text
            print(h1.strip())
        except:
            h1="Заголовок"
        try:
            article = soup.find('div', class_='product-detail-prop').text
            article = article.strip().replace('Артикул:', '').strip()
            if "Наличие" in article:
                article = ""
        except:
            article = ""

        try:
            content = soup.find('div', class_='product-description-cover')
            content = content.find('div', class_='tab-active')
        except:
            content = ""
        # print(content)
        try:
            img = soup.find('div', class_='swiper-wrapper')
            img = img.findAll('img')
            imgall = []
            for i in img:
                imgall.append(url_site + i.get("src"))
        except:
            imgall = ""
        try:
            price = soup.find('span', class_='product-item-price')
            price = price.text.replace(' ₽', '')
        except:
            price = ""
        category_name = "Каталог|" + category_name
        data = {'cat': category_name, 'img': imgall, 'title': h1, 'h1': h1, 'price': price,
                'content': content ,'article':article}
        return data


    def write_csv(data):
        my_string = '|'.join(data['img']),
        my_string = str(my_string)
        my_string = my_string.replace("('","")
        my_string = my_string.replace("',)","")
        print(str(my_string))
        with open(category_name + '.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow((data['cat'],
                             data['title'],
                             data['h1'],
                             data['price'],
                             my_string,
                             data['content'],
                             data['article'],
                             ))


    data = cat_name(i, url_site, category_name)
    write_csv(data)



