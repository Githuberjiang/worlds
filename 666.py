s = "微波炉 a microwave oven"
l = s.split(" ", maxsplit=1)
import xlrd
book = xlrd.open_workbook("工作簿1.xlsx")
sheet = book.sheet_by_index(0)
for i in range(sheet.nrows):
    a= sheet.row_values(i)
    # for j in a:
    #     print(not j)
    #     if not j:
    #         try:
    #             a = a.remove(j)
    #         except:
    #             pass
    print(a)
