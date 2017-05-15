# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

from textblob import TextBlob, Word

def read():
    url = './yelp.csv'

    yelp = pd.read_csv(url)

    yelp_best_worst = yelp[(yelp.stars ==5) | (yelp.stars==1)]

    X = yelp_best_worst.text

    y = yelp_best_worst.stars

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

    vect = CountVectorizer(ngram_range=(1, 2), lowercase=False, stop_words='english', max_features=100, min_df=3)

    X_train_dtm = vect.fit_transform(X_train)
    X_test_dtm = vect.transform(X_test)

    nb = MultinomialNB()

    nb.fit(X_train_dtm, y_train)

    y_pred_class = nb.predict(X_test_dtm)

    print 'Accuracy: ', metrics.accuracy_score(y_test, y_pred_class)
    #print vect.get_feature_names()[-50:]

    print yelp_best_worst.text[0]

    review = TextBlob(yelp_best_worst.text[0])

    reviews_1 = TextBlob(u'我是一只小罩子,从小也不骑.来了来')

    print review.sentences
    print reviews_1.sentences

if __name__ == '__main__':
    read()
