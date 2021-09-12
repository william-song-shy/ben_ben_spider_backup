import requests
import os
import datetime
a=datetime.datetime.utcnow()+datetime.timedelta(hours=8)
headers={"password":os.getenv("password")}
try:
    l=requests.get("https://bens.rotriw.com/api/backup/daily?year={}&month={}&day={}".format(a.year,a.month,a.day),headers=headers,timeout=300).json()
except requests.exceptions.RequestException as e:
    l=e
#print ('./'+a.strftime('%Y-%m-%d %H-%M')+'.txt')
if not os.path.exists("./backup_daily/"):
    os.mkdir("./backup_daily/")
fo=open('./backup_daily/'+(a-datetime.timedelta(days=1)).strftime('%Y-%m-%d')+'.txt','w',encoding="UTF-8")
fo.write(str(l))
fo.write("\n\n\n\n\n\n====================\n Update at{}".format(a.strftime('%Y-%m-%d %H-%M')))
fo.close()
