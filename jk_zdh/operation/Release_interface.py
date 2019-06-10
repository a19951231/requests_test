from Control.Request_method import All_requests
from configure.mysql_parameter import Data_Mysql,Mysql
from configure.data_pz import Data
from configure.log_configure import logging
import time
from configure.Parameter import Parameter1

class Release_Interface(All_requests):
    def getTime(self):  # 定义一个获取时间的方法
        self.now = time.strftime("%Y%m%d%H%M%S")  # 重新定义一个获取时间方法，time.strftime("%Y-%m-%d %H_%M_%S")就是把时间定义为年/月/日/时/分/秒
        return self.now  # 返回获取的时间
    def login(self):#登录接口
        a=Parameter1()
        url=Data("data.yaml","url")
        data1="{\"credential\":{\"type\":\"PASSWORD\",\"value\":\"密码\"},\"username\":\"账号\",\"grant_type\":\"password\",\"scope\":\"\"}"
        header={
            "Content-Type":a.pt('heards', 'value', 0),
            "channel":a.pt('heards', 'value', 1),
        }
        a=All_requests.all_requests(self,"post",url+"system/serviceuser/basic/app/v2/nolog/loginByPassword",data1,header,"json")
        Mysql().all_operate(1,a["data"]["access_token"],"登录的token",1)
        return a
    def foundation_template(self,value):#基础模板创建的接口
        try:
            a=Parameter1()
            url = Data("data.yaml", "url")
            data1 = {
                "tempName": value[0],  # 模板名称
                "applyIndustry": value[1],  # 适用行业
                "applyCrowd": value[2],  # 适用人群
                "tempType": value[3],  # 模板类型
                "top": value[4],  # 是否在企业创建模板页面置顶，True是，False是否
                "fieldList": value[5],
                "tempLabel": value[6],  # 标签选择
                "roleType": value[7],
                "comCode": value[8],
                "comName": value[9],
                "enterpriseServices": value[10],  # 内容空
                "splitStrategy": value[11],
                "allocationStrategyCode": value[12],
                "allocationStrategyName": value[13],
                "elaborationOrder": value[14],
                "pageView": value[15],
            }
            header = {
            a.pt('heards', 'key', 3): a.pt('heards', 'value', 3),
            a.pt('heards', 'key', 1): a.pt('heards', 'value', 3),
            a.pt('heards', 'key', 2):Mysql().all_operate(3,0,1)
            }
            a=All_requests.all_requests(self,"post",url + "allocation/templateConfig/pc/v1/addTemplate",data1,header,"json")
        except NotImplementedError as e:
            logging.error("错误原因%s"%str(e))
        else:
            return a

if __name__ == '__main__':
    Release_Interface().login()
