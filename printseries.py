def printseries(n):
    temp=[]
    for i in range(n+1):
        temp.append(i)
    return temp
inp=int(input("Enter the number :"))
ans=printseries(inp)
print(*ans)
print(sum(ans))
        
    
