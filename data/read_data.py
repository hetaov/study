# -*- coding: utf-8 -*-

from xlrd import open_workbook


def read():

    book = open_workbook('ls.xlsx')

    sheets = book.sheets()

    sheet = sheets[5]

    #for sheet in sheets:
    print sheet.name

    result = []

    for row in range(sheet.nrows):
        row_data = []
        for column in range(sheet.ncols):
            row_data.append(sheet.cell_value(row, column))

        result.append(row_data)

    return result




if __name__ == "__main__":
    result = read()

    categories = [[], [], []]

    for row_index, row in enumerate(result):
        print u'第%s行' % row_index

        for col_index, col in enumerate(row):
            if col == u'':
                last = len(categories[col_index]) - 1
                print '%s:%s' % (result[0][col_index], categories[col_index][last])

            else:
                print '%s:%s' % (result[0][col_index], col)
                if col_index < 3:
                    categories[col_index].append(col)

    print categories
