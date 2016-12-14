#!/usr/bin/python
# coding:utf-8
import os
import email163
import requests
from bs4 import BeautifulSoup


st_email = ["xxxx"]
whut_url="http://www.whut.edu.cn/2015web/tzgg/"
file_name=".st.log"
file_path="."
full_file=file_path + os.path.sep + file_name


def store_news_list(full_file, news_list):
    with open(full_file, 'w') as f:
        for news in news_list:
            href = news.find('a').get('href')
            date = news.find('strong').text
            f.write(href + '\t' + date + '\n')


try:
    response = requests.get(whut_url).text
    try:
        soup = BeautifulSoup(response, "html5lib")
        ul = soup.find('ul', attrs={"class":"normal_list2"})
        news_list = ul.find_all('li')
        first_href = news_list[0].find('a').get('href')
        first_date = news_list[0].find('strong').text

        first = False
        if not os.path.exists(full_file):
            store_news_list(full_file, news_list)
            print "Status: Not need send email, no new item."
            first = True

        sended = False
        with open(full_file) as f:
            news_list_in_file = f.readlines()
            for item in news_list_in_file:
                items = item.split('\t')
                if items[0] != first_href or items[1].strip('\n') != first_date:
                    email163.send_mail(st_email, "New Item", whut_url + " have new items.")
                    print "Status: sended email."
                    sended = True
                else:
                    if not first:
                        print "Status: Not need send email, no new item."
                break

        if sended:
            store_news_list(full_file, news_list)

    except Exception, e:
        email163.send_mail(st_email, "Parse Error.", "Maybe your web page has changed, please check it.")
        print "Parse Error:" + str(e)
except Exception, e:
    email163.send_mail(st_email, "Network Error.", "Can not get web page. Please check your network.")
    print "Network Error:" + str(e)
