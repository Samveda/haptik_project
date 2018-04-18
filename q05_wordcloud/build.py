import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt


def q05_wordcloud(dataframe):
    "write your solution here"
    text_wordcloud = dataframe.apply(lambda row: [word for word in row])
    new_l = []
    for row in text_wordcloud:
        for word in row:
            new_l.append(word)
    all_text = ' '.join(new_l)
    wordcloud = WordCloud(max_font_size=50).generate(all_text)
    plt.figure(figsize=(15, 15))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    return wordcloud.words_
