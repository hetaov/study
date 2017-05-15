# -*- coding: utf-8 -*-

from sklearn import linear_model
from sklearn.externals import joblib

# 0: 偏低 1: 正常 2: 偏高 3: 高血压 4: 危险 5: 压差大
X = [[1, 20, 80, 110],[0, 20, 80, 110], [1, 23, 82, 130], [1, 23, 82, 140], [1, 20, 80, 160], [1, 26, 80, 160]]

Y = [1, 1, 2, 3, 5, 4]

clf = linear_model.BayesianRidge()

clf.fit(X, Y)

joblib.dump(clf, 'blood.pkl')

#print clf.predict([[1, 20, 82, 112], [0, 20, 86, 148]])
