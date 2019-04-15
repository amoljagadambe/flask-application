import os
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# code to read the xlsx File
filepath = os.path.abspath(os.path.dirname(__name__))
sheetname = 'commonwordswithIPA'
filename = filepath + '/application/resources/recommender/files/AccentGURU.xlsx'
df = pd.read_excel(filename, sheet_name=sheetname)
df = df[['word', 'category', 'word_s1', 'word_s2', 'word_s3', 'word_s4', 'phase', 'primary_syllable_stress']]
df.set_index('word', inplace=True)
df['bag_of_words'] = ''
columns = df.columns
for index, row in df.iterrows():
    data = ''
    for col in columns:
        df[col] = df[col].astype(str)
        df[col] = df[col].map(lambda x: x.lower())
        data = data + row[col] + ' '
        row['bag_of_words'] = data

df.drop(columns=[col for col in df.columns if col != 'bag_of_words'], inplace=True)
count = CountVectorizer()
count_matrix = count.fit_transform(df['bag_of_words'])
indices = pd.Series(df.index)

def recommendations(words):
    recommended_words = []
    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    # gettin the index of the words that matches the word
    idx = indices[indices == words].index[0]
    # creating a Series with the similarity scores in descending order
    score_series = pd.Series(cosine_sim[idx]).sort_values(ascending=False)
    # getting the indexes of the 10 most similar words
    top_10_indexes = list(score_series.iloc[1:6].index)
    # populating the list with the words of the best matching words
    for i in top_10_indexes:
        recommended_words.append(list(df.index)[i])

    return recommended_words

