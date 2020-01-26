import requests,openpyxl
wb=openpyxl.Workbook()
sheet=wb.active
sheet.title='zhangjiawei_articles'
row=['标题','赞同数','简要内容','链接']
sheet.append(row)
url='https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?include=data%5B*%5D.comment_count%2Csuggest_edit%2Cis_normal%2Cthumbnail_extra_info%2Cthumbnail%2Ccan_comment%2Ccomment_permission%2Cadmin_closed_comment%2Ccontent%2Cvoteup_count%2Ccreated%2Cupdated%2Cupvoted_followees%2Cvoting%2Creview_info%2Cis_labeled%2Clabel_info%3Bdata%5B*%5D.author.badge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=10&limit=10&sort_by=voteups'
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
res=requests.get(url,headers=headers)
content=res.json()
#print(res.status_code)
info=content['data']
for article in info:
    rows=[]
    title=article['title']
    num=article['voteup_count']
    cont=article['content']
    link=article['url']
    rows.append(title)
    rows.append(num)
    rows.append(cont)
    rows.append(link)
    sheet.append(rows)
wb.save('douban_wenzhang.xlsx')