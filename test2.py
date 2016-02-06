a=[]
for i in range(1,5):
    for j in range(1,14):
        a+=[[i,j]]


b1=int(input())
b2=int(input())
c1=int(input())
c2=int(input())
d1=int(input())#left:mark
d2=int(input())#right:number
e1=int(input())
e2=int(input())
f1=int(input())
f2=int(input())

b=[b1,b2]
c=[c1,c2]
d=[d1,d2]#1:spade,2:clover,3:heart,4:diamond
e=[e1,e2]
f=[f1,f2]

g=[b,c,d,e,f]

h=[]
for ss in range(5):
    h+=[[g[ss][1],g[ss][0]]]
h.sort()


def yaku(h):
    if h[0][0]==1 and h[1][0]==10 and h[2][0]==11 and h[3][0]==12 and h[4][0]==13 and h[0][1]==h[1][1]==h[2][1]==h[3][1]==h[4][1]:
         return loyal



#probability
def prob(a):
    if a==loyal:
        return 100-3/2598960
    elif a==straighrt:
        return 

