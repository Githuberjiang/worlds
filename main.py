# with open("初中词汇表.md", "r", encoding="utf-8") as f:
#     for i in f.readlines():
#         print(i)

import xlrd
import xlwt
import xlutils


import xlrd
import xlutils
from xlutils import copy
book=xlrd.open_workbook('stu.xls')


ch = xlwt.Workbook()
sheet = ch.add_sheet("初中词汇")
a = 0
with open("初中词汇表.md", "r", encoding="utf-8") as f:
    for i in f.readlines():
        if " " not in i:
            print(i,a)
        try:
            y1 = i.split(" ", maxsplit=1)[0]
            y2 = i.split(" ", maxsplit=1)[1]
            sheet.write(a, 0, y1)
            sheet.write(a, 1, y2)
            a += 1
        except:pass

ch.save("ch.xls")
