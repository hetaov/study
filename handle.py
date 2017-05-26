# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
from sklearn import linear_model
from sklearn import metrics
from sklearn.cross_validation import train_test_split
from sklearn import preprocessing

data = pd.read_csv('blood_pressure.csv')

disease = pd.get_dummies(data.disease, prefix='disease')

disease.drop(disease.columns[0], axis=1, inplace=True)

data = pd.concat([data, disease], axis=1)

features_cols = ['sex', 'age', 'disease_0', 'disease_1', 'disease_2','disease_3', 'diastolic', 'systolic']


X = data[features_cols]
y = data.target


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

#clf = linear_model.BayesianRidge()
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(25, 2), random_state=1)

#clf.fit(scaler.transform(X_train), y_train)

#print scaler.transform(X_train)

#y_pred_class = clf.predict(scaler.transform(X_test))
#y_pred_class = logreg.predict(X_test)
#print metrics.accuracy_score(y_test, y_pred_class)


enc = preprocessing.OneHotEncoder()
s = enc.fit_transform(data[['diastolic']])
#d = pd.get_dummies(s, prefix="diastolic")
cut_arr = pd.cut(X['systolic'], [0, 90, 130, 140, 150, 180, 250], labels=[0, 1, 2, 3, 4, 5])
cut_arr_diastolic = pd.cut(X['diastolic'], [0, 60, 80, 90, 120, 180], labels=[0, 1, 2, 3, 4])
cut_age = pd.cut(X['age'], [0, 55, 65, 80, 200], labels=[0, 1, 2, 3])
systolic = pd.get_dummies(cut_arr, prefix="systolic")
diastolic = pd.get_dummies(cut_arr_diastolic, prefix="diastolic")
sex = pd.get_dummies(X.sex, prefix="sex")
age = pd.get_dummies(cut_age, prefix="age")

train_data = pd.concat([sex, age, disease, diastolic, systolic], axis=1)

scaler = preprocessing.StandardScaler(with_mean=True, with_std=True).fit(train_data)

#print train_data

X_train, X_test, y_train, y_test = train_test_split(train_data, y, random_state=1)

clf.fit(scaler.transform(train_data), y)
y_pred_class = clf.predict(scaler.transform(X_test))
print metrics.accuracy_score(y_test, y_pred_class)

#my_data = [[1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0]]
#print clf.predict(scaler.transform(my_data))



'''
X_origin = [[1, 20, 5, 102, 188], [1, 58, 2, 86, 142], [1, 58, 0, 86, 138], [1, 52, 4, 86, 134], [0, 52, 4, 86, 129]]


X = pd.DataFrame(X_origin, columns=['sex', 'age', 'disease', 'diastolic', 'systolic'])

disease_pre = pd.get_dummies(X.disease, prefix='disease')
disease_pre.drop(disease.columns[0], axis=1, inplace=True)

X = pd.concat([X, disease_pre], axis=1)

pre_X = X[features_cols].values
'''

#print clf.predict(pre_X)

