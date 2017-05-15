# -*- coding: utf-8 -*-

import pandas as pd
 
l = pd.read_csv('./blood_presure.csv')

print [l.sex, l.age]

df = pd.DataFrame(l)

train_data_x = df[0:3]
train_data_y = df[4:]
#print df.describe()

print train_data_x
