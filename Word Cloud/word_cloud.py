'''
word_cloud.py - Used to create basic word clouds for each team based on historical team data


'''

from matplotlib import pyplot as plt
import pandas as pd
from wordcloud import WordCloud, ImageColorGenerator
from collections import Counter
import numpy as np
from PIL import Image


team_owners = ["Leslie", "Elston", "Johnny","Nicholas","Terence","Henry", 
               "Mags", "Christopher", "Johnathan Alexander", "Kelvin","Eric","Darren"]

# Create a word cloud for each team and save it
for team_owner in team_owners:
    
    fields = [team_owner]
    data = pd.read_csv("Word Cloud/dff word cloud.csv", usecols = fields)
    # print(data["Darren"].dropna().values)

    text = data[team_owner].dropna().values
    word_cloud_dict = Counter(text)
    wordcloud = WordCloud(width=4000, height=4000).generate_from_frequencies(word_cloud_dict)
    plt.figure(figsize=(20,10))
    plt.imshow(wordcloud)
    plt.tight_layout(pad=0)
    plt.axis("off")

    # store to file
    plt.savefig(f"Word Cloud/resources/clouds/{team_owner}_bt.png", format="png")
    # plt.show()



