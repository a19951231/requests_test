from Control.Request_method import All_requests
from configure.mysql_parameter import Data_Mysql,Mysql
from configure.data_pz import Data
from configure.log_configure import logging
import time
from configure.Parameter import Parameter1
import unittest
import ddt
from Data.value_data import value,leak
from operation.Release_interface import Release_Interface

@ddt.ddt
class Test_jk(unittest.TestCase):
    def setUp(self):
        logging.info("======测试开始======")
    def tearDown(self):
        logging.info("======测试结束======")

    def test_10(self):
        refult=Release_Interface().login()
        logging.info(refult)
        print(refult)
        self.assertEqual(refult['statusCode'],'200')
        self.assertEqual(refult['msg'], "OK")
        self.assertEqual(refult['data']['access_token'],refult['data']['access_token'])

    @ddt.data(["'''基础模板创建失败接口0'''",value(0),value(0),value(0),value(0),value(0),value(0),value(0),value(0),value(0),
               value(0),value(0),value(0),value(0),value(0),value(0),value(0),"异常1"],["'''基础模板创建失败接口1'''",value(2),value(2),value(2),value(2),value(2),value(2),value(2),value(2),value(2),
               value(2),value(2),value(2),value(2),value(2),value(2),value(2),"异常2"])
    @ddt.unpack
    def test_11(self,a,b,c,d,e,f,g,h,i,j,k,l,n,m,o,p,q,to):
        time.sleep(0.5)
        a
        value=[b,c,d,e,f,g,h,i,j,k,l,n,m,o,p,q]
        refult=Release_Interface().foundation_template(value)
        logging.info(refult)
        print(refult)
        if to=="异常1":
            self.assertEqual(refult['httpCode'],201)
            self.assertEqual(refult['msg'],'模板保存失败')
        elif (to=="异常2"):
            self.assertEqual(refult['httpCode'], 201)
            self.assertEqual(refult['msg'], '模板保存失败')


if __name__ == '__main__':
    unittest.main()