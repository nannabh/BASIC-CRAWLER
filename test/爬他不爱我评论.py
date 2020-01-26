import requests
from bs4 import BeautifulSoup
#爬热门评论
url='https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk=1665984359&loginUin=1024220497&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=1&topid=4830343&cmd=8&needmusiccrit=0&pagenum=0&pagesize=25&lasthotcommentid=&domain=qq.com&ct=24&cv=10101010'
res=requests.get(url)
#print(res.status_code)
hot_comments=res.json()
list_hotcomments=hot_comments['hot_comment']['commentlist']
with open ('karen_song_comments.txt','a',encoding='utf-8') as f:
    f.write('他不爱我热门评论'+'\n')
    for i in list_hotcomments:
        c=i['rootcommentcontent']
        f.write(c+'\n')
    f.write('\n'+'普通评论'+'\n')
url2='https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg'
commentid='song_4830343_304030732_1578155214'#最后一个评论的参数
for i in range(3):
    params={
    'g_tk':'1665984359',
    'loginUin':'1024220497',
    'hostUin':'0',
    'format':'json',
    'inCharset':'utf8',
    'outCharset':'GB2312',
    'notice':'0',
    'platform':'yqq.json',
    'needNewCode':'0',
    'cid':'205360772',
    'reqtype':'2',
    'biztype':'1',
    'topid':'4830343',
    'cmd':'8',
    'needmusiccrit':'0',
    'pagenum':str(i),
    'pagesize':'25',
    'lasthotcommentid':commentid,
    'domain':'qq.com',
    'ct':'24',
    'cv':'10101010'
    }
    res_comment=requests.get(url2,params=params)
    comment=res_comment.json()
    list_comments=comment['comment']['commentlist']
    with open ('karen_song_comments.txt','a',encoding='utf-8') as f:
        f.write('第'+str(i+1)+'页'+'\n')
        for com in list_comments:
            f.write(com['rootcommentcontent']+'\n')
    commentid=list_comments[24]['commentid']
print('done')


