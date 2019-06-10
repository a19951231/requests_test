#请求方法封装模块
import requests
from selenium.common.exceptions import NoSuchElementException#导入此异常处理的包
from Control.Session import Login
sessions = Login().sessions()
class All_requests():
    def all_requests(self,*All_parameters):
        try:
            if All_parameters[0]=="get" and len(All_parameters)==3:
                self.req=sessions.request(All_parameters[0],All_parameters[1])
            elif (All_parameters[0]=="get" and len(All_parameters)==4):
                self.req=sessions.request(All_parameters[0],All_parameters[1],params=All_parameters[2])
            elif(All_parameters[0]=="get" and len(All_parameters)==5):
                self.req = sessions.request(All_parameters[0], All_parameters[1], params=All_parameters[2],headers=All_parameters[3])
            elif (All_parameters[0] == "get" and len(All_parameters) == 6):
                self.req = sessions.request(All_parameters[0], All_parameters[1], params=All_parameters[2],headers=All_parameters[3],verify=False)
            elif (All_parameters[0] == "post" and len(All_parameters)==3):
                self.req = sessions.request(All_parameters[0], All_parameters[1])
            elif (All_parameters[0]=="post" and len(All_parameters)==4):
                self.req=sessions.request(All_parameters[0],All_parameters[1],data=All_parameters[2])
            elif(All_parameters[0]=="post" and len(All_parameters)==5):
                self.req = sessions.request(All_parameters[0], All_parameters[1], data=All_parameters[2],headers=All_parameters[3])
            elif (All_parameters[0] == "post" and len(All_parameters) == 6):
                self.req = sessions.request(All_parameters[0], All_parameters[1],data=All_parameters[2],headers=All_parameters[3],files=All_parameters[4])
            elif (All_parameters[0] == "post" and len(All_parameters) == 7):
                self.req = sessions.request(All_parameters[0], All_parameters[1], data=All_parameters[2],headers=All_parameters[3],files=All_parameters[4],verify=False)
            elif (All_parameters[0] == "patch" and len(All_parameters)==3):
                self.req = sessions.request(All_parameters[0], All_parameters[1])
            elif (All_parameters[0]=="patch" and len(All_parameters)==4):
                self.req=sessions.request(All_parameters[0],All_parameters[1],data=All_parameters[2])
            elif(All_parameters[0]=="patch" and len(All_parameters)==5):
                self.req = sessions.request(All_parameters[0], All_parameters[1], data=All_parameters[2],headers=All_parameters[3])
            elif (All_parameters[0] == "patch" and len(All_parameters) == 6):
                self.req = sessions.request(All_parameters[0], All_parameters[1], data=All_parameters[2],headers=All_parameters[3],verify=False)
            elif (All_parameters[0] == "delete" and len(All_parameters)==3):
                self.req = sessions.request(All_parameters[0], All_parameters[1])
            elif (All_parameters[0]=="delete" and len(All_parameters)==4):
                self.req=sessions.request(All_parameters[0],All_parameters[1],data=All_parameters[2])
            elif(All_parameters[0]=="delete" and len(All_parameters)==5):
                self.req = sessions.request(All_parameters[0], All_parameters[1], data=All_parameters[2],headers=All_parameters[3])
            elif (All_parameters[0] == "delete" and len(All_parameters) == 6):
                self.req = sessions.request(All_parameters[0], All_parameters[1], data=All_parameters[2],headers=All_parameters[3],verify=False)
            else:
                print("你输入的格式错误或输入的参数个数超过5个！请重新更改正确的数据")
        except (NoSuchElementException, Exception) as e:
            print("{}错误原因"+str(e).format(All_parameters[0]))
        else:
            for i in All_parameters:
                if i=="json":
                    return self.req.json()
                elif(i=="status_code"):
                    return self.req.status_code
                elif(i=="text"):
                    return self.req.text
                elif(i=="content"):
                    return self.req.content
                elif(i=="content1"):
                    return self.req.content.decode()
                elif(i=="none"):
                    return self.req

if __name__ == '__main__':
    url="http://www.baidu.com"
    print(All_requests().all_requests("get",url,'none'))