__author__ = 'lionel'
import xlrd
from BarChart import drawBarChart

Location = '/Users/lionel/Desktop/ExcelTest.xlsx'


# Set the excel file path using arugent passed from the command line
def location_setter(ExcelFileLocation):
    ExcelFileLocation = Location


Data = xlrd.open_workbook(Location)
Table = Data.sheets()[0]
Nrows = Table.nrows
Ncols = Table.ncols
print('line number =', Nrows)


def getExcelData():

    dataList = [[0 for col in range(2)] for row in range(Nrows)]
    for i in range(Nrows):
        dataList[i] = Table.row_values(i)

    return dataList


def pieChart():
    return None


def barChart():
    unmodifiedList = getExcelData()
    labelList = ['I have no idea how to creat an empty list']
    valueList = [0]
    del labelList[0]
    del valueList[0]
    for i in range(len(unmodifiedList)-1):
        labelList.append(unmodifiedList[i][0])
    for i in range(len(unmodifiedList)-1):
        valueList.append(unmodifiedList[i][1])

    drawBarChart(labelList,valueList,'test','x-label')


barChart()