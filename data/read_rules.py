# -*- coding: utf-8 -*-

def read():

    book = open_workbook('rules.xlsx')

    sheets = book.sheets()

    sheet = sheets[5]

if __name__ == '__main__':
    rules = read()
    print rules
