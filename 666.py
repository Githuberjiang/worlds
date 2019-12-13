s = "微波炉 a microwave oven"
l = s.split(" ", maxsplit=1)
import xlrd
book = xlrd.open_workbook("ch.xls")
sheet = book.sheet_by_index(0)
for i in range(sheet.nrows):
    a= sheet.cell(i,1).value.strip("\n")
    print(a)
