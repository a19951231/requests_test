from lxml import etree
from configure.log_configure import logging

class Parameter1(object):
    def __init__(self):
        self.html=etree.parse("../Data/jk.html")
    def pt(self,*args):
        try:
            req=self.html.xpath('//ul[@keyword="{}"]/li/@{}'.format(args[0],args[1]))
        except Exception as log:
            logging.error("错误：%s"%str(log))
        else:
            return req[args[2]]

if __name__ == '__main__':
    a=Parameter1()
    print(a.pt("接口请求头信息",'key',2))