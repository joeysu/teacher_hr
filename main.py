import os
import re
import requests

def main():
    url = 'http://www.jiaoshizhaopin.net/guangxi/nanning'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    
    r = requests.get(url, headers=headers)
    
    re_page_num = re.compile('<li><a  href=.*</a></li><li class="page_all">.*/(.*)页</li><div class="clear"></div>')
    m_page_num = re_page_num.findall(r.text)

    payload = {'page': '1'}
    parse_page(url, payload)
    return

if __name__ == '__main__':
    main()

    #url = 'http://www.jiaoshizhaopin.net/guangxi/nanning'
    #headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

    #r = requests.get(url, headers=headers)
    #print(r.url)

    #re_city = re.compile('<span class="district_name">(.*)</span>')
    #m_city = re_city.findall(r.text)

    #re_info = re.compile(r'<h2><a class="title" href="(.*)" target="_blank" title="(.*)">.*')
    #m_info = re_info.findall(r.text)

    #r_course = re.compile(r'<li><a title=".*" href="(.*)">(.*)（<span>(.*)</span>）</a></li>')
    #m_course = r_course.findall(r.text)

    #re_date = re.compile(r'<span class="date"><i></i>(.*)</span>')
    #m_date = re_date.findall(r.text)

    #re_loc = re.compile(r'<a target="_blank" title=".*" >(.*)</a>')
    #m_loc = re_loc.findall(r.text)

    #print()