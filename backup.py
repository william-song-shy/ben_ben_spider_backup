import requests
import datetime
a=datetime.datetime.now()
l=requests.get("http://bens.rotriw.com/ranklist?_contentOnly=1").json()
#print ('./'+a.strftime('%Y-%m-%d %H-%M')+'.txt')
fo=open('./backup/'+a.strftime('%Y-%m-%d %H-%M')+'.txt','w',encoding="UTF-8")
for i in l:
    fo.write (str(i[0])+' '+str(i[1])+' '+str(i[2])+'\n')
fo.close()
