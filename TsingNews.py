import requests
from lxml import etree
import time
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re

def SendEmail(sendMessage):
        sender = "xxx@qq.com"
        pwd = "xxx"
        message = MIMEText(sendMessage, "plain", 'utf-8')
        message['From'] = "今日清华"
        message["Subject"] = "今日清华推送"
        smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
        smtpObj.login(sender, pwd)
        receivers = ['xxx@qq.com']

        message['To'] = "收信人"
        try:
            smtpObj.sendmail(sender, receivers, message.as_string())
        except smtplib.SMTPException as e:
            print("Error：无法发送邮件.Case:%s" % e)
        print("*成功发送一次")

# 主函数
if __name__ == "__main__":
    print("*软件启动")
    faSongShiJian = 8
    while True:
        now_time = datetime.datetime.now()
        if not (now_time.hour == faSongShiJian):
           time.sleep(30 * 60)
           continue
        baseURL = "https://news.tsinghua.edu.cn/"
        url = "https://news.tsinghua.edu.cn/zhxw.htm"
        content = requests.get(url)
        content = content.content.decode(encoding = "utf-8")
        html = etree.HTML(content)
        title = html.xpath("//title/text()")
        NewsList = html.xpath("//li[@class=\"listl\"]/a/text()")
        DateList = html.xpath("//li[@class=\"listl\"]/span/text()")
        tempHrefList = html.xpath("//li[@class=\"listl\"]/a/@href")
        hrefList = []
        for tempHref in tempHrefList:
            if tempHref[:4] == "info":
                hrefList.append(baseURL + tempHref)
            else:
                hrefList.append(tempHref)
        XinWen = ""
        index = 0
        while True:
            XinWen += '[' + str(index+1) + ']' + DateList[index] + NewsList[index] + '\n' + hrefList[index] + '\n'
            index+=1
            if index==30:
                break
        Nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        sendMessage = ("发送时间:%s\n综合新闻：\n%s\n" % (Nowtime, XinWen))
        SendEmail(sendMessage)
        time.sleep(24*59*60)
    print("*发生错误，软件终止")
