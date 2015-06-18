__author__ = 'lionel'
import xlrd

location = '/Users/lionel/Desktop/ExcelTest.xlsx'
data = xlrd.open_workbook(location)
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols
print('line number =', nrows)


def getExcelData(type):
    if (type == 'pie'):
        pieChart()
    if (type == 'barH'):
        None
    if (type == 'bar'):
        None

    dataList = [[0 for col in range(2)] for row in range(nrows)]
    for i in range(nrows):
        dataList[i] = table.row_values(i)

    return dataList


def pieChart():
    return None


def barChart():
    unmodifiedList = getExcelData('bar')
    labelList = ['I have no idea how to creat an empty list']
    valueList = [0]
    del labelList[0]
    del valueList[0]
    for i in range(len(unmodifiedList)-1):
        labelList.append(unmodifiedList[i][0])
    for i in range(len(unmodifiedList)-1):
        valueList.append(unmodifiedList[i][1])
    print(valueList)

barChart()