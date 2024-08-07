'''
word_cloud_pic.py - Used to read through the raw roster history sheet (dff word cloud.csv) and generate
a word cloud
'''


from matplotlib import pyplot as plt
import pandas as pd
from wordcloud import WordCloud, ImageColorGenerator
from collections import Counter
import numpy as np
from PIL import Image

team_owner = "Darren"
team_img_dict = {
    "Leslie": "Word Cloud/resources/mickey.jpg",
    "Elston": "Word Cloud/resources/kaep.jpg",
    "Johnny": "Word Cloud/resources/texans.jpg",
    "Nicholas":"Word Cloud/resources/texas.png",
    "Terence": "Word Cloud/resources/ea.png",
    "Henry": "Word Cloud/resources/sh.jpg",
    "Mags": "Word Cloud/resources/giants.jpg",
    "Christopher": "Word Cloud/resources/allen.jpg",
    "Johnathan Alexander": "Word Cloud/resources/rodgers.jpg",
    "Kelvin": "Word Cloud/resources/cards.jpg",
    "Eric": "Word Cloud/resources/colts.jpg",
    "Darren": "Word Cloud/resources/chargers.jpg",
}
fields = [team_owner]
data = pd.read_csv("Word Cloud/dff word cloud.csv", usecols = fields)
# print(data["Darren"].dropna().values)

text = data[team_owner].dropna().values
word_cloud_dict = Counter(text)

# Generate a word cloud image
mask = np.array(Image.open(team_img_dict[team_owner]))
wordcloud = WordCloud(width=1000, height=1000, background_color="white", mask=mask, mode="RGBA", max_font_size=45).generate_from_frequencies(word_cloud_dict)

# create coloring from image
image_colors = ImageColorGenerator(mask)
plt.figure(figsize=[7,7])
wordcloud.recolor(color_func=image_colors)
plt.imshow(wordcloud, interpolation='bilinear')
plt.tight_layout(pad=0)
plt.axis("off")

# store to file
plt.savefig(f"Word Cloud/resources/clouds/{team_owner}.png", format="png")

# plt.show()

