import time

a=[]
for i in range(1,5):
    for j in range(1,14):
        a+=[[i,j]]


#b1=int(input())
#b2=int(input())
#c1=int(input())
#c2=int(input())
#d1=int(input())#left:mark
#d2=int(input())#right:number
#e1=int(input())
#e2=int(input())
#f1=int(input())
#f2=int(input())#本番はこれを使う

#test用
b1=1
b2=13
c1=3
c2=4
d1=2
d2=7
e1=2
e2=11
f1=1
f2=8

b=[b1,b2]
c=[c1,c2]
d=[d1,d2]#1:spade,2:clover,3:heart,4:diamond
e=[e1,e2]
f=[f1,f2]

g=[b,c,d,e,f]

def yaku(g):
    h=[]
    for ss in range(5):
        h+=[[g[ss][1],g[ss][0]]]
    h.sort()
    i=[]
    j=[]
    for sss in range(5):
        i+=[h[sss][0]]
        j+=[h[sss][1]]
    k=[]
    l=[]
    k=[i.count(nn)for nn in range(1,14)]
    l=[j.count(nm)for nm in range(1,5)]
    m=k.count(0)
    if h[0][0]==1 and h[1][0]==10 and h[2][0]==11 and h[3][0]==12 and h[4][0]==13 and h[0][1]==h[1][1]==h[2][1]==h[3][1]==h[4][1]:
        return 1#ロイヤルストレートフラッシュ
    elif  h[4][0]-h[3][0]==h[3][0]-h[2][0]==h[2][0]-h[1][0]==h[1][0]-h[0][0]==1 and h[0][1]==h[1][1]==h[2][1]==h[3][1]==h[4][1]:
        return 2#ストレートフラッシュ
    elif max(k)==4:
        return 3#フォーカード
    elif max(k)==3:
        if 2 in k:
            return 4#フルハウス
        else:
            return 7#スリーカード
    elif max(l)==5:
        return 5#フラッシュ
    elif max(k)==1:
        if h[4][0]-h[3][0]==h[3][0]-h[2][0]==h[2][0]-h[1][0]==h[1][0]-h[0][0]==1:
            return 6
        elif h[0][0]==1 and h[1][0]==10 and h[2][0]==11 and h[3][0]==12 and h[4][0]==13:
            return 6#ストレート
        else:
            return 10#ノーペアー
    else:
        if m==10:
            return 8#ツーペア
        else:
            return 9#ワンペア


for i in range(5):
    ind = a.index(g[i])
    del a[ind]


t1=time.clock()
qqq=[]
for x1 in range(len(a)-4):
    for x2 in range(x1+1,len(a)-3):
        for x3 in range(x2+1,len(a)-2):
            for x4 in range(x3+1,len(a)-1):
                for x5 in range(x4+1,len(a)):
                    qqq+=[[a[x1],a[x2],a[x3],a[x4],a[x5]]]
    
yuki=[0]*10
for x6 in range(len(qqq)):
    yuki[yaku(qqq[x6])-1]+=1

#print("royalstraightflush=",yuki.count(1)*100/1533939,"%")
#print("straightflush=",yuki.count(2)*100/1533939,"%")
#print("fourcard=",yuki.count(3)*100/1533939,"%")
#print("fullcard=",yuki.count(4)*100/1533939,"%")
#print("flush=",yuki.count(5)*100/1533939,"%")
#print("straight=",yuki.count(6)*100/1533939,"%")
#print("threecard=",yuki.count(7)*100/1533939,"%")
#print("twopair=",yuki.count(8)*100/1533939,"%")
#print("onepair=",yuki.count(9)*100/1533939,"%")
#print("nopair=",yuki.count(10)*100/1533939,"%")

m1=[]
for mm in range(5):
    m1+=[[g[mm][1],g[mm][0]]]
    m1.sort()

import copy

n=[]
n1=[0]*10
n2=[0]*10
n3=[0]*10
n4=[0]*10
n=copy.deepcopy(m1)
for ggg in range(5):
    n=copy.deepcopy(m1)
    for ggh in range(47):
        n[ggg]=a[ggh]
        n1[yaku(n)-1]+=1

for ggi in range(len(n)-1):
    for ggj in range(ggi+1,len(n)):
        for ggk in range(46):
            n=copy.deepcopy(m1)
            for ggl in range(ggk+1,47):
                n[ggi]=a[ggk]
                n[ggj]=a[ggl]
                n2[yaku(n)-1]+=1

for ggn in range(4):
    for ggo in range(ggn+1,5):
        for ggp in range(45):
            for ggq in range(ggp+1,46):
                for ggr in range(ggq+1,47):
                        n=[a[ggp],a[ggq],a[ggr],m1[ggn],m1[ggo]]
                        n3[yaku(n)-1]+=1

for ggs in range(5):
    for ggw in range(44):
        for ggx in range(ggw+1,45):
            for ggy in range(ggx+1,46):
                for ggz in range(ggy+1,47):
                    n = [m1[ggs], a[ggw], a[ggx], a[ggy], a[ggz]]
                    n4[yaku(n)-1]+=1


t2=time.clock()
print(t2-t1)

