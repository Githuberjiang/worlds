import xlrd
from xlutils import copy  # xlutils中导入copy

book = xlrd.open_workbook("stu.xls")
sheet = book.sheet_by_index(0)
se = set()
for i in range(sheet.nrows):
    a = sheet.cell(i, 1).value.strip("\n")
    se.add(a)
    print(a)
print(len(se))

book1 = xlrd.open_workbook('stu.xls')
# 先用xlrd打开一个excel
new_book = copy.copy(book)
# 然后用xlutils里面的copy功能，复制一个excel
sheetr = new_book.get_sheet(0)  # 获取sheet页
n = 0
for i in se:
    sheetr.write(n, 3, i)  # 修改第0行，第一列
    n += 1
new_book.save('stu.xls')
