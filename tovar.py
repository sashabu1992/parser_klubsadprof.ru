import csv

from bs4 import BeautifulSoup
import requests

url_site = "https://klubsadprof.ru"
res_spisok_tovar_url = "https://klubsadprof.ru/catalog/rozy/chayno_gibridnye/roza_ogyust_renuar_auguste_renoir/"
category_name = "asd"


def cat_name(url, url_site, category_name):
    # Use a breakpoint in the code line below to debug your script.
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    h1 = soup.find('h1', class_='product-detail-title').text
    print(h1.strip())
    article = soup.find('div', class_='product-detail-prop').text
    print(article.strip().replace('Артикул:', '').strip())
    content = soup.find('div', class_='product-description-cover')
    content = content.find('div', class_='tab-active')
    # print(content)
    img = soup.find('div', class_='swiper-wrapper')
    img = img.findAll('img')
    imgall = []
    for i in img:
        imgall.append(url_site + i.get("src"))
    price = soup.find('span', class_='product-item-price')
    price = price.text.replace(' ₽', '')
    category_name = "Каталог|" + category_name
    data = {'cat': category_name, 'img': imgall, 'title': h1, 'h1': h1, 'price': price,
            'content': content}
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
                         ))


data = cat_name(res_spisok_tovar_url, url_site, category_name)
write_csv(data)
