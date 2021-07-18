import requests
import os
import datetime
a=datetime.datetime.utcnow()+datetime.timedelta(hours=8)
l=requests.get("http://bens.rotriw.com/ranklist?_contentOnly=1").json()
#print ('./'+a.strftime('%Y-%m-%d %H-%M')+'.txt')
if not os.path.exists("./backup/"+a.strftime('%Y-%m-%d')+'/'):
    os.mkdir("./backup/"+a.strftime('%Y-%m-%d')+'/')
fo=open('./backup/'+a.strftime('%Y-%m-%d')+'/'+a.strftime('%Y-%m-%d %H-%M')+'.txt','w',encoding="UTF-8")
for i in l:
    fo.write (str(i[0])+' '+str(i[1])+' '+str(i[2])+'\n')
fo.close()
