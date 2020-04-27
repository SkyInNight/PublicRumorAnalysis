# -*- coding: utf-8 -*-
import os


def combine_file(path_1, path_2, new_file_name):
    content_1 = None
    content_2 = None
    with open(path_1, 'r', encoding='utf-8') as f:
        content_1 = f.readlines()
    with open(path_2, 'r', encoding='utf-8') as f:
        content_2 = f.readlines()
    with open(new_file_name, 'a+', encoding='utf-8') as f:
        for i in range(0, len(content_1)):
            if i == len(content_1) - 1:
                f.write(content_1[i])
            f.write(content_1[i] + '\n')
        for i in range(0, len(content_2)):
            if i == len(content_2) - 1:
                f.write(content_2[i])
            f.write(content_2[i] + '\n')


if __name__ == '__main__':
    path_1 = r'.\\data\\new_data\\news&all_rumor.txt'
