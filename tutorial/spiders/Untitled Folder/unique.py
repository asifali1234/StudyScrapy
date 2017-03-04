list = open('new.txt', "r")
passwords = list.readlines()


k=1
t = open(''+str(k)+'.txt',"w")
print len(passwords)
q=[]
c=0
for word in passwords:
	q.append(word)
	t.write(word)
	c+=1
	if(c%15000==0):
		t.close()
		k+=1
		print c
		print k
		t = open(''+str(k)+'.txt',"w")

