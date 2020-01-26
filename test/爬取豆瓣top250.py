import requests,openpyxl
from bs4 import BeautifulSoup
wb=openpyxl.Workbook()
sheet=wb.active
sheet.title='douban_top250'
row1=['序号','电影名称','评分','评语','链接']
sheet.append(row1)
headers={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch, br',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'no-cache',
'Connection':'keep-alive',
'Cookie':'bid=hbpVpwEz--0; douban-fav-remind=1; __yadk_uid=Ye0pjYT9OgW7rP6GQUZA6PB2SxNBjyVC; trc_cookie_storage=taboola%2520global%253Auser-id%3D68d459f6-2af3-45de-a5eb-56d8bfc55057-tuct46146c6; ll="108296"; __gads=ID=697b06b6ced477d7:T=1579062564:S=ALNI_MYzpZqZy0tvQRhYrqgdMHKDswpMwQ; ap_v=0,6.0; _pk_id.100001.4cf6=80c9c9ef4c58de82.1564462332.4.1579689487.1579593305.; _pk_ses.100001.4cf6=*; __utma=30149280.1108002386.1562399240.1579590944.1579689479.17; __utmb=30149280.0.10.1579689479; __utmc=30149280; __utmz=30149280.1579062628.15.8.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.1592443662.1564462332.1579590944.1579689479.4; __utmb=223695111.0.10.1579689479; __utmc=223695111; __utmz=223695111.1564462332.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
'Host':'movie.douban.com',
'Pragma':'no-cache',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}
for i in range(1):
    website='https://movie.douban.com/top250?start='+str(25*i)+'&filter='
    res=requests.get(website,headers=headers)
    #print(res.status_code)
    html=BeautifulSoup(res.text,'html.parser')
    #content=html.find('ol',class_='grid_view')
    info=html.find_all('li')
    for m in info:
        print(m.find('span',class_='title'))
