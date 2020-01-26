import requests,openpyxl
from bs4 import BeautifulSoup
wb=openpyxl.Workbook()
sheet=wb.active
sheet.title='Jay_songs'
row1=['歌曲名称','所属专辑','歌曲时长','发售时间','歌曲链接']
sheet.append(row1)
res = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=62233968801549786&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=1665984359&loginUin=1024220497&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
# print(res.status_code)
res_music=res.json()#当爬虫用json时要用general里的网址！
list_music=res_music['data']['song']['list']
for i in list_music:
    row=[]
    name=i['name']
    row.append(name)
    album=i['album']['name']
    row.append(album)
    interval=str(i['interval'])+'秒'
    row.append(interval)
    time=i['time_public']
    row.append(time)
    link='https://y.qq.com/n/yqq/song/'+i['mid']+'.html'
    row.append(link)
    sheet.append(row)
wb.save('Jay_songs.xlsx')
print('done')
#第二次提交
    
    
