#intro to lists
mylist=[]
mylist.append(1)
mylist.append(20)
mylist.append(300)

print(mylist[0])
print(mylist[1])
print(mylist[2])

for x in mylist:
 print x

#testing out of range
#print(mylist[10])

list2=[1, 2, 3]

for x in list2:
 print x

list3=[2, 3, 4]

maxlist = list2 + list3

print(maxlist)
list4=[1, 2, 3]

print(list2+list4)
odd=[1,3,5]
even=[2,4,6]
print(odd + even)
