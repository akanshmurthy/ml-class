import pandas as pd
import numpy as np

df = pd.read_csv('tweets.csv')
target = df['is_there_an_emotion_directed_at_a_brand_or_product']
text = df['tweet_text']

fixed_text = text[pd.notnull(text)]
fixed_target = target[pd.notnull(text)]

from sklearn.feature_extraction.text import CountVectorizer

count_vect = CountVectorizer()
count_vect.fit(fixed_text)

# turns the text into a sparse matrix
counts = count_vect.transform(fixed_text)
#print(counts.shape)
print(fixed_text[0:2])
print(counts[0:2])

# some other fun things to try
#print(fixed_text[0])
#print(count_vect.transform(["cerulean"]))
