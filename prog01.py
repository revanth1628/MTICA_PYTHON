def primeornot(num):
    if num<1:
        return 0
    if num==1 or num==2 or num==3:
        return num
    for i in range(2,num):
        if num%i==0:
            return 0
    return num
lst=[]
first=int(input('Enter the first number:'))
last=int(input('Enter the last number:'))
for i in range(first,last+1):
    if primeornot(i):
        lst.append(i)
print(*lst)
print(len(lst))
    
