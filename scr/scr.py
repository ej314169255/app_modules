import requests, time
from bs4 import BeautifulSoup
from tabulate import tabulate

## Определяем список ключевых слов:
KEYWORDS = ['дизайн', 'фото', 'web', 'python']

## Ваш код
headers = ['date','title','link']
def fn(params):
    url = 'https://habr.com/ru/search/'
    first_line = 'https://habr.com'
    query = {'target_type': 'posts', 'order': 'relevance'}
    rows = []
    for list_element in params:
        query.update({'q': list_element})
        response = requests.get(url, params = query)
        soup = BeautifulSoup(response.text, features="html.parser")
        news = soup.find_all('article', 'tm-articles-list__item')
        for el in news:
            time.sleep(1)
            date = el.find('time').text
            title = el.find('h2').text
            try:
                link = first_line + el.find('a', 'tm-title__link').get('href')
            except AttributeError:
                link = "no link"
            #rows.append({'date': date, 'title': title, 'link': link, 'phrase': list_element})
            rows.append([date,title,link])

    return rows
print(tabulate(fn(KEYWORDS), headers=headers, tablefmt="html"))