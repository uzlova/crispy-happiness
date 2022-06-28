import requests as requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# ------------------------------------------------------------------------------- #


def pars():
    games = []
    session = requests.Session()
    url = 'https://store.steampowered.com/search/?sort_by=Price_ASC&specials=1'
    headers = {"user-agent": UserAgent().chrome, "Accept-Language": "ru"}
    r = session.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, "html.parser")
    all_games = soup.find_all('span', attrs={'class': 'title'})
    sale = soup.find_all('div', attrs={'class': 'col search_discount responsive_secondrow'})
    for i, j in zip(all_games, sale):
        # print(f"{i.text} - {j.text.strip()}")
        discount = j.text.strip()
        if discount == '-88%':
            games.append(i.text)
    return games


# -------------------------------------------------------------------------------#

