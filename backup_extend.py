import requests
import os
import datetime
a=datetime.datetime.utcnow()+datetime.timedelta(hours=8)
l=requests.get("http://123.176.98.118:5000/api/backup/extend").json()
#print ('./'+a.strftime('%Y-%m-%d %H-%M')+'.txt')
if not os.path.exists("./backup_extend/"+a.strftime('%Y-%m-%d')+'/'):
    os.mkdir("./backup_extend/"+a.strftime('%Y-%m-%d')+'/')
fo=open('./backup_extend/'+a.strftime('%Y-%m-%d')+'/'+a.strftime('%Y-%m-%d %H-%M')+'.txt','w',encoding="UTF-8")
for i in l['top_50']:
    fo.write (str(i[0])+' '+str(i[1])+' '+str(i[2])+'\n')
fo.write("\n\n\n\n\n\n====================\nTotal benbens:{}\nTotal users:{}".format(l['num_benben'],l['num_user']))
fo.close()
