import requests
from bs4 import BeautifulSoup as Bs
from flask import make_response, jsonify

def scrap(users):
    ids = users['users']

    response = {}

    for userId in ids:

        url = "https://www.urionlinejudge.com.br/judge/pt/profile/" + userId

        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

        data = requests.get(url, headers=headers)

        soup = Bs(data.text, 'html.parser')

        pages = soup.find('div', id='table-info')
        pages = pages.text.split(' ')
        pages = int(pages[-1])

        tds = soup.find_all('td', class_='id')

        questions = set()
        avatar = soup.find('div', class_='pb-avatar').img['src']
        username = soup.find('div', class_='pb-username').p.a.text

        for td in tds:
            link = td.find('a')
            questions.add(link.text)

        url += '?page='

        for page in range(2,pages):
            print(page)
            data = requests.get(url + str(page), headers=headers)
            soup = Bs(data.text, 'html.parser')

            tds = soup.find_all('td', class_='id')

            for td in tds:
                link = td.find('a')
                questions.add(link.text)

        response[userId] = {
                'username': username,
                'avatar': avatar,
                'questoes': list(questions)
        }

        print('response: ', response)

    return jsonify(response)

def teste():
    a = {'teste': [1,2,3]}
    return jsonify(a)