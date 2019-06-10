import logging.config
import logging
from os import path
import os
#log_file_path = path.join(os.path.dirname(__file__))#把文件路径打印出来
#print(log_file_path+"\log.conf")
#logging.config.fileConfig(log_file_path+str("/log.conf"))
#logging.config.fileConfig('resources/logging.conf')
#logging1= logging.getLogger()


CON_LOG='../configure/log.conf'#../是返回上一层，然后读取confing1这个路径里的log.conf文件
logging.config.fileConfig(CON_LOG)#然后使用config.fileConfig去读取这个文件
logging=logging.getLogger()#配置文件

