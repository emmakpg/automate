f = open("resp.txt","r")

payload = f.readlines()

#print(payload[2])
tid=[]
clref=[]
for item in payload:

    #n= payload[item].rfind('TransactionId')
    n = item[74:106]
    m = item[153:176]
    tid.append(n)
    clref.append(m)

#print(tid)

print(payload[1].rfind('nce'))

f.close


#writing transactionsID to tidl.txt
f = open("tidl.txt","w+")

for items in tid:
        f.write('%s\n' %items)
f.close

#writing clientreference to clref.txt
f = open("clref.txt","w+")

for items in clref:
        f.write('%s\n' %items)
f.close