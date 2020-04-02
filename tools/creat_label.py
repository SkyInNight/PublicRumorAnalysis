# -*- coding: utf-8 -*-
import os

def file_travelling(path='.',topdown=False):
    # 1. 创建存贮文件路径和名称的字典
    files_path = {}
    for root,dirs,files in os.walk(path,topdown=topdown):
        for name in files:
            # 2. 将文件路径为关键字，文件名为值存入字典中
            files_path[os.path.join(root, name)] = name
    # 3. 返回字典
    return files_path

def creat_label(files_path):
    for file in files_path.keys():
        label_name = files_path[file].split('.')[0] + '_label.txt'
        line_num = 0
        with open(file,'r',encoding='utf8') as f:
            line_num = len(f.readlines())
        with open(".\\data\\new_data\\"+label_name,'a+',encoding='utf8') as f:
            for i in range(0,line_num):
                f.write("1\n")

if __name__ == '__main__':
    with open('label_virus_test.txt','a+',encoding='utf-8') as f:
        for i in range(0,600):
            f.write("1\n")
        for i in range(0,300):
            f.write("0\n")
    