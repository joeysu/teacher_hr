import re
import requests

class HR(object):

    def __init__(self, url, headers):
        self.url = url
        self.headers = headers
    
    def get_requests(self):
        return requests.get(url, headers=self.headers)

    def findall(self, pattern):
        return re.compile(pattern).findall(self.response.text)


class TeacherHR(HR):

    def __init__(self, url, headers, parse_type):
        super().__init__(url, headers)
        self.parse_type = parse_type
        self.params = {}

    def get_requests(self):
        return requests.get(url, headers=self.headers, params=self.params)

    def run(self):
        self.response = self.get_requests()
        self.iters = self.get_iters()

        for iter in range(self.iters):
            self.params['page'] = str(iter+1)
            self.response = self.get_requests()
            getattr(self, 'parse_{}'.format(self.parse_type))()
            getattr(self, 'process_{}'.format(self.parse_type))()

    def get_iters(self):
         return getattr(self, 'get_iters_{}'.format(self.parse_type))()

    def get_iters_0(self):
        return int(self.findall(r'href=.*</a></li><li class="page_all">.*/(.*)页</li><div class="clear"></div>')[0])

    def parse_0(self):
        self.city = self.findall(r'<span class="district_name">(.*)</span>')
        self.info = self.findall(r'<h2><a class="title" href="(.*)" target="_blank" title="(.*)">.*')
        self.course = self.findall(r'<li><a title=".*" href="(.*)">(.*)（<span>(.*)</span>）</a></li>')
        self.date = self.findall(r'<span class="date"><i></i>(.*)</span>')
        self.loc = self.findall(r'<a target="_blank" title=".*" >(.*)</a>')

    def process_0(self):
        print(self.date)

url = 'http://www.jiaoshizhaopin.net/guangxi/nanning'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
parse_type = 0

t_0 = TeacherHR(url, headers, parse_type)

t_0.run()