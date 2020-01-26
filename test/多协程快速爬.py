import gevent,requests,bs4,openpyxl
from gevent.queue import Queue
from gevent import monkey
monkey.patch_all()
wb=openpyxl.Workbook()
sheet=wb.active
sheet.title='cal'
row1=['食物名称','热量','详情链接']
sheet.append(row1)
url_list=[]
for i in range(1,4):
    for a in range(1,4):
        url='http://www.boohee.com/food/group/'+str(i)+'?page='+str(a)
        url_list.append(url)
work=Queue()
#创建队列对象，并赋值给work。
for url in url_list:
    work.put_nowait(url)
def crawler():
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    while not work.empty():
        url=work.get_nowait()
        res=requests.get(url,headers=headers)
        bs=bs4.BeautifulSoup(res.text,'html.parser')
        foods=bs.find_all('li',class_='item clearfix')
        for shiwu in foods:
            name=shiwu.find_all('a')[1]['title']
            #用find_all在<li class="item clearfix">标签下，提取出第2个<a>元素title属性的值，也就是食物名称。
            #ca=shiwu.find('div',class_='text-box pull-left').find('p').text[4:]
            ca=shiwu.find('p').text[3:]
            link='http://www.boohee.com'+shiwu.find_all('a')[1]['href']
            row=[name,ca,link]
            sheet.append(row)
# tasks_list=[]
# for x in range(5):
#     task=gevent.spawn(crawler)
#     tasks_list.append(task)
# gevent.joinall(tasks_list)
tasks_list = []
#创建空的任务列表
for x in range(5):
#相当于创建了5个爬虫
    task = gevent.spawn(crawler)
    #用gevent.spawn()函数创建执行crawler()函数的任务。
    tasks_list.append(task)
    #往任务列表添加任务。
gevent.joinall(tasks_list)
#用gevent.joinall方法，启动协程，执行任务列表里的所有任务，让爬虫开始爬取网站。
wb.save('foods cal.xlsx')