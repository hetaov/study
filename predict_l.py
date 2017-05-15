# -*- coding: utf-8 -*-

from sklearn.externals import joblib

if __name__ == '__main__':
    clf = joblib.load('blood.pkl')
    print clf.predict([[1, 20, 82, 112], [0, 20, 86, 148]])
