ls=[0,1]

def fabseries(n):
    if n<=len(ls):
        return ls[n-1]
    else:
        temp=fabseries(n-1)+fabseries(n-2)
        ls.append(temp)
        return temp

n=int(input())
print(fabseries(n))
print("series=",ls)