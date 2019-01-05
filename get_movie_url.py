import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from lxml import html
from selenium import webdriver
import json
import math


browse_urls = ['https://www.rottentomatoes.com/browse/dvd-streaming-all?minTomato=0&maxTomato=20&services=amazon;hbo_go;itunes;netflix_iw;vudu;amazon_prime;fandango_now&genres=1;2;4;5;6;8;9;10;11;13;18;14&sortBy=release',
            'https://www.rottentomatoes.com/browse/dvd-streaming-all?minTomato=20&maxTomato=40&services=amazon;hbo_go;itunes;netflix_iw;vudu;amazon_prime;fandango_now&genres=1;2;4;5;6;8;9;10;11;13;18;14&sortBy=release',
            'https://www.rottentomatoes.com/browse/dvd-streaming-all?minTomato=40&maxTomato=60&services=amazon;hbo_go;itunes;netflix_iw;vudu;amazon_prime;fandango_now&genres=1;2;4;5;6;8;9;10;11;13;18;14&sortBy=release',
            'https://www.rottentomatoes.com/browse/dvd-streaming-all?minTomato=60&maxTomato=80&services=amazon;hbo_go;itunes;netflix_iw;vudu;amazon_prime;fandango_now&genres=1;2;4;5;6;8;9;10;11;13;18;14&sortBy=release',
            'https://www.rottentomatoes.com/browse/dvd-streaming-all?minTomato=80&maxTomato=100&services=amazon;hbo_go;itunes;netflix_iw;vudu;amazon_prime;fandango_now&genres=1;2;4;5;6;8;9;10;11;13;18;14&sortBy=release']

def get_all_movie_urls():
    #Get all individual movie urls from the list view of all the movies
    movie_list = {}
    #save titles in another txt file for the word cloud
    titles = []

    for browse_url in browse_urls:
        # start selenium driver
        driver = webdriver.Firefox(executable_path=r'/Users/matrix/Documents/Development/RottenTomatoesCrawler/geckodriver')
        driver.get(browse_url)
        soup = BeautifulSoup(driver.page_source, "lxml")
        number_of_movies = int(soup.find('div', {'class': "main-column-item"}).text.split()[3])

        #number of times of clicking 'more'
        for i in range(0,math.ceil(number_of_movies/32)-1):
            if driver.find_element_by_css_selector('.btn.btn-secondary-rt.mb-load-btn') is None:
                continue
            else:
                driver.find_element_by_css_selector('.btn.btn-secondary-rt.mb-load-btn').click()

                #find all movies
                movies = soup.find('div', {'class': "mb-movies"})
                for movie in movies:
                    a = (movie.find('a'))
                    if a is not None:
                        #get movie links and titles
                        url = a.get('href')
                        title = movie.find('h3', {'class': "movieTitle"}).text
                        movie_list[title] = url
                        titles.append(title)

    #quit driver
    driver.quit()

    #save files
    with open('titles.txt', 'w') as file:
        json.dump(titles,file)
    with open('movie_urls.txt','w') as file:
        json.dump(movie_list,file, indent=4)

if __name__ == '__main__':
    get_all_movie_urls()