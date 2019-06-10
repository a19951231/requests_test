import re
from Data.mysql_pz import Mysql
from configure.log_configure import logging

class Data_Mysql(object):
    def read_mysql(self,*args):
        try:
            pat="'{}': '(.*?)', ".format(args[0])
            req=re.findall(pat,Mysql().all_operate(args[1],args[2],args[3]))
        except Exception as e:
            logging.error("错误原因%s" % str(e))  # 打印日志
        else:
            return req[0]

if __name__ == '__main__':
    print(Data_Mysql().read_mysql("createName",3,0,1))