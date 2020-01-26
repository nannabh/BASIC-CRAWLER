import requests 
from bs4 import BeautifulSoup
res = requests.get('http://www.xiachufang.com/explore/')
html=BeautifulSoup(res.text,'html.parser')
food=html.find('div',class_='normal-recipe-list')
food_list=food.find_all('li')
dishinfo=[]
flist=[]
for i in food_list:
    name=i.find('p',class_='name').text.replace(" ", "").replace("\n", "")
    dishinfo.append(name)
    ing=i.find('p',class_='ing ellipsis').text.replace(" ", "").replace("\n", "")
    dishinfo.append(ing)
    web=i.find('p',class_='name').find('a')['href']
    web='http://www.xiachufang.com'+web
    dishinfo.append(web)
    flist.append(dishinfo)
    dishinfo=[]
for dish in flist:
    print('菜名：{}\n原料：{}\n网址：{}\n'.format(dish[0],dish[1],dish[2]))