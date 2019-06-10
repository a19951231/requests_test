# -*- coding:utf-8 -*-
import pymysql
from configure.log_configure import logging
from configure.data_pz import Data

class Mysql():
    def dy(self,sql_query):#读取mysql的mysql80的数据库里的kybzhh列表
        try:
            conn=pymysql.connect(host="localhost",user="root",password="123456",database="jk",charset="utf8")
            #连接数据库
            #创建一个游标
            cursor=conn.cursor()
            #使用execute()方法执行sql语句
            cursor.execute(sql_query)
            conn.commit()
            #打印全部数据给data
            data=cursor.fetchall()
        except Exception as e:
            logging.error("错误原因%s"%str(e))#打印日志
        else:
            if(self):
                return data#返回data数据
            else:
                cursor.close()#关闭游标
                conn.close()#关闭数据库
    def query(self,*args):
        try:
            data=Mysql().dy(args[0])
        except Exception as e:
            logging.error("错误原因%s"%str(e))#打印日志
        else:
            return data[args[1]][args[2]]

    def all_operate(self,*args):#添加或更新数据方法
        try:
            if args[0]==0:
                sql='insert into valued(value,bz) values("{}","{}")'.format(args[1],args[2])
                data=Mysql()
                a=data.dy(sql)
                return a
            elif(args[0]==1):
                sql1 = 'update valued set value="{}",bz="{}" where id={}'.format(args[1], args[2],args[3])
                data = Mysql()
                a = data.dy(sql1)
                return a
            elif(args[0]==2):
                sql='select * from {}'.format(args[1])
                data=Mysql()
                a=data.dy(sql)
                return a
            elif (args[0] == 3):
                sql = 'select * from valued'
                data = Mysql()
                a = data.dy(sql)
                return a[args[1]][args[2]]
        except Exception as e:
            logging.error("错误原因%s"%str(e))#打印日志


if __name__ == '__main__':
    data=Mysql().all_operate(3,0,1)
    #data=Mysql().query("select * from valued",0,1)
    print(data)

#学习python读取mysql数据网站：www.cnblogs.com/liubinsh/p/7568423.html
#https://www.cnblogs.com/dwenwen/articles/8259638.html