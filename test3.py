
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


del a[(b1-1)*13+b2-1]
del a[(c1-1)*13+c2-1]
del a[(d1-1)*13+d2-1]
del a[(e1-1)*13+e2-1]
del a[(f1-1)*13+f2-1]

print(a)
print(h)
