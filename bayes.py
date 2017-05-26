# -*- coding: utf-8 -*-

from sklearn import linear_model
from sklearn.externals import joblib
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import preprocessing
from sklearn import metrics
from sklearn.cross_validation import train_test_split

import scaler_s

import pandas as pd

# 0: 偏低 1: 正常 2: 高血压 3: 危险 4: 压差大
# 0: 糖尿病 1: 冠心病 2: 脑梗塞 3: 脑出血 4: 肾病 5:高血压

data = pd.read_csv('blood_pressure.csv')

X = data[['sex', 'age', 'disease', 'diastolic', 'systolic']]
Y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=1)

'''
enc = preprocessing.OneHotEncoder()

enc.fit(data[['sex', 'disease']].values)
print data[['sex', 'disease']]
print enc.transform(data[['sex', 'disease']].values).toarray()
print '<--------->'
'''
#print data[['sex', 'disease']]
#gnb = GaussianNB()
#gnb.fit(X, Y)

#clf = linear_model.BayesianRidge()

#clf.fit(X, Y)

scaler = preprocessing.StandardScaler(with_mean=True, with_std=True).fit(X)

#scaler_s.set_scaler(scaler)
#print scaler_s.get_scaler()

clf_1 = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(25, 2), random_state=1)
clf_1.fit(scaler.transform(X), Y)
y_pred_class = clf_1.predict(scaler.transform(X_test))
print metrics.accuracy_score(y_test, y_pred_class)

#print scaler.transform(X)
#print scaler.mean_

X = [[1, 20, 5, 102, 188], [1, 58, 2, 86, 142], [1, 58, 0, 86, 138], [1, 52, 4, 86, 134], [0, 52, 4, 86, 129]]

print scaler.transform(X)

print clf_1.predict(scaler.transform(X))

joblib.dump(clf_1, 'blood.pkl')
#joblib.dump(clf, 'blood.pkl')
#joblib.dump(gnb, 'blood.pkl')


#print data.target.values
#print data[['sex', 'age']]

#print clf.predict([[1, 20, 82, 112], [0, 20, 86, 148]])
