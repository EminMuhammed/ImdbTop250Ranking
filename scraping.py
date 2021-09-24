import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_url(url):
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "lxml")
    return soup


mainpageurl_list = ["https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&ref_=adv_prv",
                    "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=51&ref_=adv_nxt",
                    "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=101&ref_=adv_nxt",
                    "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=151&ref_=adv_nxt",
                    "https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=201&ref_=adv_nxt"]


def scrape_movie_url(mainpageurl_list):
    movies_url_list = []
    for ln in mainpageurl_list:
        print(ln)
        soup = get_url(ln)
        movie_column = soup.find("div", attrs={"class": "lister-list"})
        movies_tags = movie_column.find_all("div", attrs={"class": "lister-item mode-advanced"})
        for i in movies_tags:
            print("https://www.imdb.com" + i.a.get("href").split("?")[0] + "ratings/?ref_=tt_ov_rt")
            movies_url_list.append("https://www.imdb.com" + i.a.get("href").split("?")[0] + "ratings/?ref_=tt_ov_rt")

    return movies_url_list


movies_url_list = scrape_movie_url(mainpageurl_list)


def get_values(movies_url_list):
    liste = []
    for ln in movies_url_list:
        print(ln)
        soup = get_url(ln)
        table = soup.find("table", attrs={"cellpadding": "0"})
        tr = table.find_all("tr")
        tr = tr[1:]

        votes_list = []
        for value in tr:
            votes_list.append(value.find("div", attrs={"class": "leftAligned"}).text.strip())

        rating = soup.find("span", attrs={"class": "ipl-rating-star__rating"}).text.strip()
        title = soup.find("h3", attrs={"itemprop": "name"}).text.strip()

        liste.append([ln, title, rating, votes_list[0], votes_list[1], votes_list[2], votes_list[3], votes_list[4],
                      votes_list[5], votes_list[6], votes_list[7], votes_list[8], votes_list[9]])

    return liste


top250 = get_values(movies_url_list)

df = pd.DataFrame(top250)
df.columns = ["url", "title", "rating", "10_points", "9_points", "8_points", "7_points", "6_points", "5_points",
              "4_points", "3_points", "2_points", "1_points"]

df.to_excel("imdb_top250.xlsx")
