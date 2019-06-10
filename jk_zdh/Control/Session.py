import requests
class Login():
    def sessions(self):
        try:
            self.Requests=requests.session()
        except Exception as e:
            print("sessions方法错误原因："+str(e))
        else:
            return self.Requests
