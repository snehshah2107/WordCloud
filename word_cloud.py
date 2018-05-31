from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
import sys
from nltk.corpus import stopwords
import numpy as np
from PIL import Image

def clean_data(data):
    """
    Takes filename as argument and process the file to clean the data
    count the frequency of each word in a dictionary
    returns the dictionary
    """
    with open(data,'r') as f:
        lines = [line.rstrip('\n') for line in f]
        word_count = Counter()

        for line in lines:
            word_count.update(line.split())

        stop_words = stopwords.words('english')
        stop_words.extend(("like", "I", "if", "i'm", "I'm", "The", "I've", "If", "would", "*","\\","me","nai","che","kai","k","j","ne","chu","na","tu","e"))
        for key in stop_words:
            del word_count[key]
        #print(word_count)

    return word_count

def generate_cloud(c):
    
    # Create the wordcloud object
    #wordcloud = WordCloud(width=480, height=480, margin=0).generate(c)
    troopermask = np.array(Image.open('trooper.png'))
    wordcloud=WordCloud(mask=troopermask, colormap="OrRd",mode="RGB")
    #wordcloud=WordCloud()
    wordcloud.generate_from_frequencies(frequencies=c)

    # Display the generated image:
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.margins(x=0, y=0)
    plt.show()

if __name__ =='__main__':
    c = clean_data(sys.argv[1])
    generate_cloud(c)