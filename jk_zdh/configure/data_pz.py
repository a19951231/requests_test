# -*- coding:utf-8 -*-
import yaml
from configure.log_configure import logging

def Data(File_name,value):
    try:
        with open("../Data/"+File_name, 'r', encoding="utf-8") as file:  # 这样写法比较好，就算我们文件不close，也不会说读取不了或释放不了
            data=yaml.load(file)# 然后使用yaml.load()方法读取file这个文件并且给予data
    except NotImplementedError as e:
        logging.error("读取data数据错误原因%r"%str(e))
    else:
        return data[value]

if __name__ == '__main__':
    print(Data("jk.yaml","wageConfig"))