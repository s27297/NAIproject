import pandas as pd
import nltk
from nltk.corpus import twitter_samples
import random
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.probability import FreqDist
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.classify import NaiveBayesClassifier
from sklearn.naive_bayes import MultinomialNB
import nltk.classify.util

nltk.download('twitter_samples')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('punkt_tab')


df=pd.read_csv('youtoxic_english_1000(2).csv',usecols=[2,15])
# podzial na texty i ich kasyfikacje
i=0
banedComments=[]
notBanedComments=[]
textsArray=df.drop("IsBaned",axis=1).to_numpy()
IsBanedArray=df["IsBaned"].to_numpy()

# funkcja do tworzenia arrayow z labelem true i zlabelem false
def add_to_array(text,index):
  # print(textsArray[index][0])
  if(text==True):
    banedComments.append(textsArray[index][0])
  else:
    notBanedComments.append(textsArray[index][0])
# tworzenie arrayow
for i in range(len(IsBanedArray)):
  add_to_array(IsBanedArray[i],i)

# robiwnie labelow i ich tasowanie
comments=banedComments+notBanedComments
labels = ['True'] * len(banedComments) + ['False'] * len(notBanedComments)
# comments
# Shuffle the dataset
combined = list(zip(comments, labels))
random.shuffle(combined)
comments, labels = zip(*combined)
# array to text i tokenizacja
sample_text = ','.join(comments)
tokens = word_tokenize(sample_text)

# usuwanie tokenów
stop_words = set(stopwords.words('english'))
def remove_stopwords(tokens):
    return [word for word in tokens if word.lower() not in stop_words]
filtered_tokens = remove_stopwords(tokens)
# stematyzacja i lematyzacja tokenow
# stemmer = PorterStemmer()
# lemmatizer = WordNetLemmatizer()

# stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]
# lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]



# Convert comments to TF-IDF vectors
vectorizer = TfidfVectorizer(max_features=10000, stop_words='english')
X = vectorizer.fit_transform(comments).toarray()

# Create feature sets for training and testing

X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.3, random_state=42)

# Train a Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train, y_train)


# definicja nowego textu(nie w training set)
def classiffy_sentence(text):

    print(text)
    # Preprocess the input text
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word.isalpha() and word not in stop_words]

    # Convert tokens back to a single string
    preprocessed_text = " ".join(tokens)
    # Transform the text to TF-IDF vector
    text_vector = vectorizer.transform([preprocessed_text]).toarray()
    # Predict the label using the classifier
    prediction = classifier.predict(text_vector)

    return prediction[0]
