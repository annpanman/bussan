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

def yaku():
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
    k=[i.count(nn)for nn in range(13)]
    l=[j.count(nm)for nm in range(4)]
    m=k.count(0)
    if h[0][0]==1 and h[1][0]==10 and h[2][0]==11 and h[3][0]==12 and h[4][0]==13 and h[0][1]==h[1][1]==h[2][1]==h[3][1]==h[4][1]:
        return 1　#ロイヤルストレートフラッシュ
    elif  h[4][0]-h[3][0]==h[3][0]-h[2][0]==h[2][0]-h[1][0]==h[1][0]-h[0][0]==1 and h[0][1]==h[1][1]==h[2][1]==h[3][1]==h[4][1]:
        return 2　#ストレートフラッシュ
    elif max(k)==4:
        return　3　#フォーカード
    elif max(k)==3:
        if 2 in k:
            return 4 #フルハウス
        else:
            return 7 #スリーカード
    elif max(l)==5:
        return 5 #フラッシュ
    elif max(k)==1:
        if h[4][0]-h[3][0]==h[3][0]-h[2][0]==h[2][0]-h[1][0]==h[1][0]-h[0][0]==1:
            return 6
        elif h[0][0]==1 and h[1][0]==10 and h[2][0]==11 and h[3][0]==12 and h[4][0]==13:
            return 6 #ストレート
        else:
            return 10 #ノーペアー
    else:
        if m==10:
            return 8 #ツーペア
        else:
            return 9 #ワンペア

del a[(b1-1)*13+b2-1]
del a[(c1-1)*13+c2-1]
del a[(d1-1)*13+d2-1]
del a[(e1-1)*13+e2-1]
del a[(f1-1)*13+f2-1]

q=[]
for x1 in range(44):
    for x2 in range(x1,45):
        for x3 in range(x2,46):
            for x4 in range(x3,47):
                for x5 in range(x4,48):
                    q+=[[a[x1],a[x2],a[x3].a[x4],a[x5]]]
    
