# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


import pandas as pd
import numpy as np
import jsonlines

pd.set_option('display.max_columns', 23)  # 设置显示的最大列数参数为a
pd.set_option('display.width', 1500)  # 设置显示的宽度为500，防止输出内容被换行
pd.set_option('max_colwidth', 200)  # 设置显示列值的宽度为100
pd.set_option('display.max_rows', None)  # 设置显示的行宽为全部，将所有行显示出来

xueyemianyi = pd.read_excel('D:\\NLP\\数据处理\\xueyemianyi\\xueyemianyi.xlsx')
print(len(xueyemianyi))  # 37577

after_xueyemianyi = xueyemianyi.drop_duplicates()

after_xueyemianyi.to_excel('D:\\NLP\\数据处理\\xueyemianyi\\after_xueyemianyi.xlsx', encoding='utf8', index=False)


after_xueyemianyi = pd.read_excel('D:\\NLP\\数据处理\\xueyemianyi\\after_xueyemianyi.xlsx')
print(len(after_xueyemianyi))  # 37503，重复74条

"""
药敏史相关
"""

# 1.出现敏的情况
min = after_xueyemianyi[after_xueyemianyi['现病史'].str.contains('敏',na=True)]
print(len(min))  #11762

# 2.敏中出现药敏的情况
yaomin = after_xueyemianyi[after_xueyemianyi['现病史'].str.contains('药敏',na=True)]
print(len(yaomin)) # 现病史中有243条
yaomin = min[min['现病史'].str.contains('药敏',na=True)]
print(len(yaomin)) # 敏中也有243条

# 3.出现药物过敏的情况
yaowuguomin = after_xueyemianyi[after_xueyemianyi['现病史'].str.contains('药物过敏',na=True)]
print(len(yaowuguomin)) # 8970
yaowuguomin = min[min['现病史'].str.contains('药物过敏',na=True)]
print(len(yaowuguomin)) # 8970

# 4.不存在敏的情况
wumin = after_xueyemianyi[~after_xueyemianyi['现病史'].str.contains('敏',na=True)]
print(wumin['现病史'].value_counts())
print(len(wumin)) # 25741

# 5.