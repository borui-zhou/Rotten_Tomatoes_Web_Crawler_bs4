## Purpose of the project
This is my first web crawler project. This project uses beautiful soup to parse the html, along with some other relevant libraries like requests, selenium, json, pymongo, etc. My intention is to scrape all movies on Rotten Tomatoes and perform some analyzations. While this project can achieve my goal, but it takes too long to parse all movie info since it goes through one movie url by one movie url. Scrapy would be a better tool to use to fulfill my purpose and that is what I'm going to do next. However, I still consider this project as a good practise for anyone who hasn't been exposed to web scraping before.
## Main components 
1. get_movie_url.py --> It scrapes all the movie url and store them in a txt file.
2. get_movie_info.py --> The main scraper, it gets all the movie info and store them into a local Mongodb Database.
3. movie_item.py --> Just a movie item class.
4. word_cloud.py --> Generate a word cloud of titles, a little something fun.<br>![Description](https://github.com/Regina77/Rotten_Tomatoes_Web_Crawler_bs4/title_word_cloud.png)
