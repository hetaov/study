# -*- coding: utf-8 -*-

from sklearn.externals import joblib
from sklearn import preprocessing

import scaler_s
import pandas as pd

if __name__ == '__main__':
    clf = joblib.load('blood.pkl')

    data = pd.read_csv('blood_t.csv')

    X = data[['sex', 'age', 'disease', 'diastolic', 'systolic']].values

    scaler = preprocessing.StandardScaler(with_mean=False, with_std=False).fit(X)

    X = [[1, 20, 5, 12, 192], [1, 38, 5, 76, 139]]
    #print scaler_s.get_scaler()
    #scaler = preprocessing.StandardScaler(with_mean=False, with_std=False).fit(X)
    print clf.predict(scaler.transform(X))
