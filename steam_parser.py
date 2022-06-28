import requests as requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# ------------------------------------------------------------------------------- #


def pars():
    games = {}  # название: ссылка
    session = requests.Session()
    url = 'https://store.steampowered.com/search/?sort_by=Price_ASC&specials=1'
    headers = {"user-agent": UserAgent().chrome, "Accept-Language": "ru"}
    r = session.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    all_games = soup.find_all('span', attrs={'class': 'title'})
    sale = soup.find_all('div', attrs={'class': 'col search_discount responsive_secondrow'})
    links = soup.find_all('a', attrs={'class': "search_result_row ds_collapse_flag"})
    for i in range(len(all_games)):
        # print(f"{i.text} - {j.text.strip()}")
        discount = sale[i].text.strip()
        if discount == '-100%':
            games[all_games[i].text] = links[i].attrs['href']
    return games


# -------------------------------------------------------------------------------#

