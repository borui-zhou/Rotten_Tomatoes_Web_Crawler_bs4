import io
from collections import Counter
from os import path
import requests
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import re
import numpy as np
from PIL import Image
import urllib

def generate_word_cloud(path_dir):
    # It is important to use io.open to correctly load the file as UTF-8
    text = io.open(path.join(path_dir, 'titles.txt')).read()

    text1 = re.sub(',', ' ', text)
    text2 = re.sub('\"', ' ', text1)
    text2 = text2.split()
    words = ""
    for word in text2:
        words += (word + " ")
    # print(Counter(text2))

    font_path = path.join(path_dir, 'Symbola.ttf')
    mask = np.array(Image.open(requests.get('http://png.clipart-library.com/images/1/blue-cloud-clouds-clip-art/cloud-clip-art-blue-clouds-background-png-5ab0d50c1e5541.7810380115215383161243.jpg', stream=True).raw))

    word_cloud = WordCloud(
            background_color='black',
            stopwords=STOPWORDS,
            max_words=200,
            mask=mask,
            scale=3
        ).generate(words)

    #plot the graph

    # Custom color scheme, uncomment code below to set custom color scheme
    # def grey_color_func(word, font_size, position,orientation,random_state=None, **kwargs):
    #     return("hsl(230,100%%, %d%%)" % np.random.randint(49,51))
    # word_cloud.recolor(color_func = grey_color_func)
    plt.figure(dpi=1200)
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.show()
    image_path = path_dir + '/title_word_cloud.png'
    word_cloud.to_file(image_path)

def main():
    path_dir = path.dirname('/Users/matrix/Documents/Development/RottenTomatoesCrawler/')
    generate_word_cloud(path_dir=path_dir)

main()