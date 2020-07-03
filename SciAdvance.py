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

# tg bot
import telegram
bot = telegram.Bot(token="XXX:XXXXXX")


# 主函数
if __name__ == "__main__":
    # 每天早上八点推送
    faSongShiJian = 10
    print("*软件启动")

    url = "http://www.cas.cn/syky/"
    #　获取网页内容 打个断点看一下能不能获取到
    content = requests.get(url)
    # 转换编码
    content = content.content.decode(encoding = "utf-8")
    # 提取信息 用xpath！
    html = etree.HTML(content)
    title = html.xpath("//title/text()")
    singelNewsTitle = html.xpath("//div[@id=\"content\"]//li/a/@title")
    singelNewsTime = html.xpath("//div[@id=\"content\"]//li/span/text()")
    singelNewsHref = html.xpath("//div[@id=\"content\"]//li/a/@href")

    i = 0
    news = ""
    while i < len(singelNewsTitle):
        news += singelNewsTitle[i] + "\t" + singelNewsTime[i] + "\n " + url + singelNewsHref[i] + "\n \n"
        i+=1

    #发送者邮箱
    sender = "XXX@qq.com"
    # 下面这一串密码很重要，注意保护··· 要不然坏人就可以用你的账号发邮件
    pwd = "XXX"
    # 当前时间
    Nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # 准备好发送的邮件文本内容
    sendMessage = ("时间：%s \n内容：\n\n%s" % (Nowtime, news))
    # 调用MiMEText()，转化为mime的blabla...就是文本格式了
    message = MIMEText(sendMessage, "plain", 'utf-8')
    # 发送人的标识
    message['From'] = "科研进展"
    # 邮件主题
    message["Subject"] = "科研进展"
    # smtp.qq.com是qq的smtp服务器
    smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
    # 登录账号
    smtpObj.login(sender, pwd)
    # 填写收件人信息：邮箱、昵称、
    receivers = ['XXX@qq.com']
    # 利用下列格式添加新用户：
    # receivers += [xxx@xx.com]
    
    message['To'] = "收信人"
    # for uniUser in receivers:
    # 调用函数发送邮件，传入发送者、接收者、以及mimetext类型的信息内容，使用try语句，这样避免出现意料之外的错误，程序不会直接终止
    try:
        smtpObj.sendmail(sender, receivers, message.as_string())
    except smtplib.SMTPException as e:
        # 当出现smtplib.SMTPException时的报错信息
        print("Error：无法发送邮件.Case:%s" % e)
        # break

    bot.send_message(chat_id="1244458851", text=sendMessage)
    print("*成功发送一封")

    # 无限循环：循环体内加一个sleep函数，这样的话不会频繁访问服务器被封IP
    while True:
        now_time = datetime.datetime.now()
        if not (now_time.hour == faSongShiJian):
            # 休息58s
            time.sleep(58)
            continue
        # 需要分析的网页
        url = "http://www.cas.cn/syky/"
        #　获取网页内容 打个断点看一下能不能获取到
        content = requests.get(url)
        # 转换编码
        content = content.content.decode(encoding = "utf-8")
        # 提取信息 用xpath！
        html = etree.HTML(content)
        title = html.xpath("//title/text()")
        singelNewsTitle = html.xpath("//div[@id=\"content\"]//li/a/@title")
        singelNewsTime = html.xpath("//div[@id=\"content\"]//li/span/text()")
        singelNewsHref = html.xpath("//div[@id=\"content\"]//li/a/@href")

        i = 0
        news = ""
        while i < len(singelNewsTitle):
            news += singelNewsTitle[i] + "\t" + singelNewsTime[i] + "\n " + url + singelNewsHref[i] + "\n \n"
            i+=1

        #发送者邮箱
        sender = "XXXXX@qq.com"
        # 下面这一串密码很重要，注意保护··· 要不然坏人就可以用你的账号发邮件
        pwd = "XXXXXX"
        # 当前时间
        Nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        # 准备好发送的邮件文本内容
        sendMessage = ("时间：%s \n内容：\n\n%s" % (Nowtime, news))
        # 调用MiMEText()，转化为mime的blabla...就是文本格式了
        message = MIMEText(sendMessage, "plain", 'utf-8')
        # 发送人的标识
        message['From'] = "科研进展"
        # 邮件主题
        message["Subject"] = "科研进展"
        # smtp.qq.com是qq的smtp服务器
        smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
        # 登录账号
        smtpObj.login(sender, pwd)
        # 填写收件人信息：邮箱、昵称、
        receivers = ['XXX@qq.com']
        # 利用下列格式添加新用户：
        # receivers += [xxx@xx.com]
        
        message['To'] = "收信人"
        # for uniUser in receivers:
        # 调用函数发送邮件，传入发送者、接收者、以及mimetext类型的信息内容，使用try语句，这样避免出现意料之外的错误，程序不会直接终止
        try:
            smtpObj.sendmail(sender, receivers, message.as_string())
        except smtplib.SMTPException as e:
            # 当出现smtplib.SMTPException时的报错信息
            print("Error：无法发送邮件.Case:%s" % e)
            # break

        bot.send_message(chat_id="1244458851", text=sendMessage)
        print("*成功发送一封")
        time.sleep(1*60*60)
    # 一旦发生错误退出无限循环，软件终止
    print("*发生错误，软件终止")