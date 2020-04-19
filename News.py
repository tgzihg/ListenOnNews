# requests库
import requests
# xpath
from lxml import etree
# 时间——每隔10s采集一次
import time
import datetime
# 发邮件用的两个python模块
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 主函数
if __name__ == "__main__":
    # 每天早上八点推送
    time.sleep(10*60)
    faSongShiJian = 8
    print("*软件启动")
    # 无限循环：循环体内加一个sleep函数，这样的话不会频繁访问服务器被封IP
    while True:
        now_time = datetime.datetime.now()
        if not (now_time.hour == faSongShiJian):
            # 休息58s
            time.sleep(58)
            continue
        # 需要分析的网页
        url = "http://today.hit.edu.cn"
        #　获取网页内容 打个断点看一下能不能获取到
        content = requests.get(url)
        # 转换编码
        content = content.content.decode(encoding = "utf-8")
        # 提取信息 用xpath！
        html = etree.HTML(content)
        title = html.xpath("//title/text()")
        #print("网站标题：",end="")
        #print(title)
        #print("公告：")
        # 经过漫长时间的摸索··终于找到了合适的xpath提取表达式
        NewsList = html.xpath("//div[@class=\"view-content\"][1]//li/span/a")
        AutorList = html.xpath("//div[@class=\"view-content\"][1]//li/div/span/a")
        DateList = html.xpath("//div[@class=\"view-content\"][1]//li/div/span/text()")
        hrefList = html.xpath("//div[@class=\"view-content\"][1]//li/span/a/@href")
        while ' ' in DateList:
            DateList.remove(' ')
        #print("[0]最新公告：")
        ZuiXin = ""
        index = 0
        while True:
            #print(NewsList[index].text)
            ZuiXin += '[' + str(index+1) + ']' + NewsList[index].text + " --- " + AutorList[index].text + ':'+ DateList[index] + '\n' + url + hrefList[index] + '\n'
            index+=1
            if index==10:
                break
        #print("[1]院系公告：")
        YuanXi = ""
        while True:
            #print(NewsList[index].text)
            YuanXi += '[' + str(index+1) + ']' + NewsList[index].text + " --- " + AutorList[index].text + ':'+ DateList[index] + '\n' + url + hrefList[index] + '\n'
            index+=1
            if index==20:
                break
        
        #print("[2]部处公告：")
        BuChu = ""
        while True:
            #print(NewsList[index].text)
            BuChu += '[' + str(index+1) + ']' + NewsList[index].text + " --- " + AutorList[index].text + ':'+ DateList[index] + '\n' + url + hrefList[index] + '\n'
            index+=1
            if index==30:
                break
        
        # 看到了么？这样就可以把新闻提取出来
        # 这个只是原始数据，你可以把这些信息进一步处理，比如发邮件（每天给你发一次，然后不会错过每日新闻）
        # 发邮件也就用到了Python的其它模块
        
        # 如果你想发邮件的话，就套用这个模板吧，这个东西不需要记忆，填空题。
        # 现在看一下如果写错了密码会怎么样
        
        #发送者邮箱
        sender = "xxx@qq.com"
        # 下面这一串密码很重要，注意保护··· 要不然坏人就可以用你的账号发邮件
        pwd = "xxx"
        # 当前时间
        Nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 准备好发送的邮件文本内容
        sendMessage = ("今日:%s\n最新公告：\n%s\n院系公告：\n%s\n部处公告\n%s" % (Nowtime,ZuiXin,YuanXi,BuChu))
        # 调用MiMEText()，转化为mime的blabla...就是文本格式了
        message = MIMEText(sendMessage, "plain", 'utf-8')
        # 发送人的标识
        message['From'] = "今日哈工大"
        # 邮件主题
        message["Subject"] = "今日哈工大推送"
        # smtp.qq.com是qq的smtp服务器
        smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
        # 登录账号
        smtpObj.login(sender, pwd)
        # 填写收件人信息：邮箱、昵称、
        receivers = ['xxx@qq.com','xxx@qq.com']
        receivers += ['xxx@qq.com']
        # 利用下列格式添加新用户：
        # receivers += [xxx@xx.com]
        
        message['To'] = "收信人"
        # for uniUser in receivers:
        # 调用函数发送邮件，传入发送者、接收者、以及mimetext类型的信息内容，使用try语句，这样避免出现意料之外的错误，程序不会直接终止
        try:
            smtpObj.sendmail(sender, receivers, message.as_string())
        except smtplib.SMTPException as e:
            # 当出现smtplib.SMTPException时的报错信息
            #print("Error：无法发送邮件.Case:%s" % e)
            break
        print("*成功发送一封")
        time.sleep(1*60*60)
    # 一旦发生错误退出无限循环，软件终止
    print("*发生错误，软件终止")