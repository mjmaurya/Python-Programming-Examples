import math
def ifperfectsqr(n):
    s=int(math.sqrt(n))
    return s*s==n
def isfaoncii(n):
    return ifperfectsqr(5*n*n+4) or ifperfectsqr(5*n*n-4)

testcase=int(input())
for i in range(testcase):
    n=int(input())
    print(isfaoncii(n))
    