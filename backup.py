import requests
l=requests.get("http://bens.rotriw.com/ranklist?_contentOnly=1").json()
for i in l:
    print (i[0],i[1],i[2])
