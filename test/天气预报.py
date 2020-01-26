import requests,smtplib,schedule,time
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.header import Header

def weather():
    headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    url='http://www.weather.com.cn/weather/101210301.shtml'
    res=requests.get(url,headers=headers)
    res.encoding='utf-8'
    bsdata=BeautifulSoup(res.text,'html.parser')
    data1=bsdata.find(class_='tem').text
    data2=bsdata.find(class_='wea').text
    return data1,data2

def sendmail(data1,data2):  
    smpt_server='smtp.qq.com'#发信服务器
    username='1024220497@qq.com'
    password='uiklpfiokmgjbebg'
    to_addr=['ragnarjin@163.com']
    text='''今天的天气是：'''+data1+data2
    msg=MIMEText(text,'plain','utf-8')
    #实例化一个MIMEText邮件对象(构造了一个纯文本邮件)，该对象需要写进三个参数，分别是邮件正文，文本格式和编码.
    msg['From']=Header('somebody')
    msg['To']=Header(','.join(to_addr))
    subject='天气预报'
    msg['Subject']=Header(subject,'utf-8')
    #在等号的右边，是实例化了一个Header邮件头对象，该对象需要写入两个参数，分别是邮件主题和编码，然后赋值给等号左边的变量message['Subject']。
    try:
        server=smtplib.SMTP_SSL(smpt_server)
        #实例化一个smtplib模块里的SMTP类的对象，这样就可以调用SMTP对象的方法和属性了
        server.connect('smtp.qq.com',465)
        #连接服务器，第一个参数是服务器地址，第二个参数是SMTP端口号。
        server.login(username,password)
        #登录邮箱，第一个参数为邮箱账号，第二个参数为邮箱密码
        server.sendmail(username,to_addr,msg.as_string())
        server.quit()
        print('邮件发送成功')
    except smtplib.SMTPException:
        print('Error: 无法发送邮件')

def job():
    print('开始任务')
    data1,data2=weather()
    sendmail(data1,data2)
    print('任务完成')

schedule.every().day.at('09:13').do (job)
while True:
    schedule.run_pending()
    time.sleep(1)

# schedule.every(10).minutes.do(job)       #部署每10分钟执行一次job()函数的任务
# schedule.every().hour.do(job)            #部署每×小时执行一次job()函数的任务
# schedule.every().day.at("10:30").do(job) #部署在每天的10:30执行job()函数的任务
# schedule.every().monday.do(job)          #部署每个星期一执行job()函数的任务
# schedule.every().wednesday.at("13:15").do(job)#部署每周三的13：15执行函数的任务