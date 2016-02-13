g=[]
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
    
        
    
