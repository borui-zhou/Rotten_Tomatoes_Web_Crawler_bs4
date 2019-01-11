import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.p import urlopen
from bs4 import BeautifulSoup
from lxml import html
import requests
from selenium import webdriver
import json
from movie_item import *
import pymongo
from pymongo import MongoClient
from selenium.webdriver.common.action_chains import ActionChains
import datetime
# import pickle

#MongoDB setup
client = MongoClient()
client = MongoClient("localhost", 27017)
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
movie_items = db["movie_items"]



def get_movie_info(movie_url):
    #Get all individual movie urls from the list view of all the movies

    #initiate a movie object with default values
    movie_item = Movie_item("", "0.0", 0, 0, 0, "", "","", 0, [], "0",0)

    # start selenium driver
    driver = webdriver.Firefox(executable_path=r'/Users/matrix/Documents/Development/RottenTomatoesCrawler/geckodriver')
    driver.get(movie_url)

    soup = BeautifulSoup(driver.page_source, "lxml")

    # Find all movie info
    all_critics = soup.find("div", {"id": "all-critics-numbers"})
    if all_critics is not None:
        all_critics_2 = all_critics.find("div", {"id": "scoreStats"})
        all_critics_info = all_critics_2.findAll("span", {"class": ''})

        # ScoreStats
        movie_item.tomatometer = int(all_critics.find("a", {"id": 'tomato_meter_link'}).text.strip().replace("%", ""))
        movie_item.rating = all_critics_2.find("div", { "class" : 'superPageFontColor' }).text.split("\n")[2].strip().replace("/10", "")
        movie_item.fresh = int(all_critics_info[1].text)
        movie_item.rotten = int(all_critics_info[2].text)

        genres = []
        directors = []

        """General Movie Information"""
        movie_info = soup.find("ul", {"class": 'content-meta info'})
        movie_info_list = movie_info.findAll("div")

        for i in range(0, len(movie_info_list)):

            # Genres
            if "Genre:" in str(movie_info_list[i]):
                list_of_genres = movie_info_list[i + 1].text.split(",")

                for j in list_of_genres:
                    genre = str(j.strip())
                    genres.append(genre)
                movie_item.genre = genres

            # Directors
            if "Directed By:" in str(movie_info_list[i]):
                list_of_movie_directors = movie_info_list[i + 1].text.strip().split(",")

                for j in list_of_movie_directors:
                    genre = str(j.strip())
                    directors.append(genre)
                movie_item.director = directors

            # Release Date
            if "In Theaters:" in str(movie_info_list[i]):
                # Relase Date and Type
                release_info = movie_info_list[i + 1].text.strip().split("\n")

                # Year in Theatres
                string_of_release_date = str(release_info[0].replace(",", ""))
                movie_item.in_theater_year = datetime.datetime.strptime(string_of_release_date, '%b %d %Y').strftime(
                    '%Y')

            # Runtime
            if "Runtime:" in str(movie_info_list[i]):
                movie_item.runtime = movie_info_list[i + 1].text.strip().split()[0]

            # Studio
            if "Studio:" in str(movie_info_list[i]):
                studio = str(movie_info_list[i + 1].text.strip())
                movie_item.studio = studio

            # Cast name & number
            cast_info = soup.find("div", {"class": 'castSection '})
            if cast_info is None:
                movie_item.number_of_cast = 0
            else:
                cast = []
                number_of_cast = 0

                for i in cast_info.findAll("a", {"class": 'unstyled articleLink'}):
                    cast_name = i.text.strip()
                    if cast_name == "View All":
                        continue
                    else:
                        cast.append(cast_name)
                        number_of_cast += 1
                movie_item.cast = cast
                movie_item.number_of_cast = number_of_cast

    #convert to json
    movie_item_dict = movie_item.asdict()

    # result = movie_items.delete_many({})
    result = movie_items.insert_one(movie_item_dict)
    driver.quit()

def main_scraper():

    base_url = 'https://www.rottentomatoes.com'

    with open('movie_urls.txt') as data_file:
        data = json.load(data_file)

    for title in data:
        if str(title) != '/m/null':
            add_on = data[str(title)]
            movie_url = base_url + add_on
            get_movie_info(movie_url)

# main_scraper()

def draw_pie_chart(labels, values,title):
    fig1, ax1 = plt.subplots()
    total = [100]
    title = plt.title(title)
    title.set_ha("left")
    plt.gca().axis("equal")
    pie = plt.pie(values, autopct='%1.1f%%', startangle=90)
    plt.legend(labels, bbox_to_anchor=(1, 0.5), loc="center right", fontsize=10,
               bbox_transform=plt.gcf().transFigure)
    plt.subplots_adjust(left=0.0, bottom=0.1, right=0.45)

    ax1.axis('equal')
    plt.tight_layout()
    plt.show()
    
cursor = movie_items.find({})

# x = []
# y = []

# for document in cursor:
#       print(document)

for movie_item in cursor:
    for cast in movie_item['cast']:
        x.append(cast)
print(len(x))
print(Counter(x))
