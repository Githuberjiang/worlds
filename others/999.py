import xlrd
import xlutils
from xlutils import copy    #xlutils中导入copy

book=xlrd.open_workbook('ch.xls')
#先用xlrd打开一个excel
new_book=copy.copy(book)
#然后用xlutils里面的copy功能，复制一个excel
sheet=new_book.get_sheet(0)  #获取sheet页
sheet.write(3,3,'张三')  #修改第0行，第一列
# sheet.write(1,1,'小军')   #修改第一行，第一列
new_book.save('stu.xls')