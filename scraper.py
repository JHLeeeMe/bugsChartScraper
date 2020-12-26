from multiprocessing import Pool
from dateutil.parser import parse
from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup


def get_date_list():
    url = 'https://music.bugs.co.kr/chart/track/day/total?chartdate=0'
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'lxml')

    curr_date = str(soup.find('time')).split('\n')[2].replace('\t', '').replace('\r', '')  # 현재 page의 date
    date_list = []
    while True:
        date_list.append(curr_date)
        curr_date = (parse(curr_date) + timedelta(days=1)).strftime('%Y.%m.%d')

        if curr_date == datetime.today().strftime('%Y.%m.%d'):
            date_list.append(curr_date)
            break
    return date_list[:-2]


def scrap(date):
    url = 'https://music.bugs.co.kr/chart/track/day/total?chartdate=' + date
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, "lxml")

    list_ranking = []
    list_title = []
    list_artists = []
    list_album = []

    tr_tags = soup.tbody.find_all('tr')
    for tr_tag in tr_tags:
        # ranking scrape
        sub_ranking = tr_tag.find(class_='ranking').find('strong').text
        list_ranking.append(sub_ranking)

        # title scrape
        title_tag = tr_tag.find('p', {'class': 'title'})
        if title_tag.find('a'):
            sub_title = title_tag.find('a').text
        else:
            sub_title = title_tag.find(class_=None).text
        list_title.append(sub_title)

        # artists scrape
        artist_tag = tr_tag.find('p', {'class': 'artist'})
        if artist_tag.find('a'):
            sub_artists = artist_tag.find('a').text
        else:
            sub_artists = artist_tag.find('span').text
        list_artists.append(sub_artists)

        # album scrape
        album_tag = tr_tag.find_all('td', {'class': 'left'})[1]
        sub_album = str(album_tag.text).replace('\n', '')
        list_album.append(sub_album)

    today = datetime.today().strftime('%Y%m%d')
    my_file_path = './resources/csv/bugsChartScrap_' + today + '.csv'
    print(date)

    with open(my_file_path, 'a') as f:
        for ranking, title, artists, album in zip(list_ranking, list_title, list_artists, list_album):
            f.write(ranking + '|' + title + '|' + artists + '|' + album + '|' + date + '\n')


if __name__ == '__main__':
    with Pool(processes=12) as p:
        p.map(scrap, get_date_list())
