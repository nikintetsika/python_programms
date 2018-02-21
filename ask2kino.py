import urllib2
import json
import datetime

cur_date=datetime.datetime.now()

kino_list = []
maxlen = 10

def compare_lists(l1,l2):
    s=0
    for i in l1:
        if i in l2:
            s += 1
    return s

while len(kino_list) < maxlen:
    i = int(input("Enter a number to create your list: "))
    kino_list.append(i)
    for i in kino_list:
        if kino_list.count(i) > 1:
            kino_list.remove(i)
    if i > 81 or i < 1 :
        print ("Your number is not right! Type another number!")
        break
    else:
        print (kino_list)
print ("Finally your list is:")



max = 0
numbers_suc = []
for i in range(31):
    cur_date= cur_date - datetime.timedelta(days=1)
    date_str= cur_date.strftime("%d-%m-%Y")
    url='http://applications.opap.gr/DrawsRestServices/kino/drawDate/%s.json'%date_str
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    data = response.read()
    data=json.loads(data)
    klhrwseis= data['draws']['draw']
    r=[]
    for k in klhrwseis:
        tmp=k["results"]
        r.append(compare_lists(kino_list,tmp))
    sum = 0
    for j in range(180):
	    if r[j]>3:
		    sum += 1
    numbers_suc.append(sum)
    if sum>max:
	    max = sum
	    bestday = cur_date
    print "The best day for the user was",bestday,"with",max,"right numbers!!!"
