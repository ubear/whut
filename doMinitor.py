#!/usr/bin/python
# coding:utf-8
import login163
import requests
from bs4 import BeautifulSoup

url="http://www.whut.edu.cn/2015web/tzgg/"
response = requests.get(url).text

soup = BeautifulSoup(response,"html5lib")
ul = soup.find_all('ul', attrs={"class":"normal_list2"})
lis = ul[0].find_all("li")
li_tag = lis[0]

file_path="/home/chyoo/learning/shaotao/.shaotao"
list_file = open(file_path)
items = list_file.readlines()

if len(items) == 0:
    for item in lis:
        list_file.write(item.find("a").get("href") + "\t" + item.find("strong").text + "\n")
    list_file.close()
else:
    for item in items:
        tags = item.split("\t")
        if len(tags) != 2:
            login163.send_mail(login163.mailto_list, "error", "item length is not two.")
        elif tags[0] != li_tag.find("a").get("href") or tags[1].strip("\n") !=  li_tag.find("strong").text:
            login163.send_mail(["951004642@qq.com"], "new", "wu han li gong.")
            list_file.close()
            new_file = open(file_path, 'w')
            for item in lis:
                new_file.write(item.find("a").get("href") + "\t" + item.find("strong").text + "\n")
            new_file.close()
            print "send email"
        else:
            print "not to send email"
        break
