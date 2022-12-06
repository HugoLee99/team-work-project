import xlrd
#install xlrd 1.2.0 才能用
#导入需要读取Excel表格的路径，请确保路径正确

data = xlrd.open_workbook(r'C:\Users\31684\Desktop\roommates matching.xlsx ')

table = data.sheets()[1]
# 创建一个空列表，存储Excel的数据

tables = []


# 将excel表格内容导入到tables列表中

def import_excel(excel):
    for rown in range(excel.nrows):

        array = {'roommate1': '', 'roommate2': ''}

        array['roommate1'] = table.cell_value(rown, 0)

        array['roommate2'] = table.cell_value(rown, 1)
        # 将Excel表格中的时间格式转化

        tables.append(array)

if __name__ == '__main__':
    import_excel(table)
    for i in tables:
        print(i)
    print(type(tables[0]))
