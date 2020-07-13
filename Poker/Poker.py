import numpy as np

tx=open('poker.txt', 'r')
line=tx.readlines()
n=len(line)
li=[]
s1ar1=[]
s1ar2=[]
nalim1=[]
nalim2=[]


for j in range(n):
    li.append(np.hstack([line[j][0:14].strip(),line[j][15:29].strip()]))
    tmp=[]
    tmp2=[]
    for i in range(5):
        thing=li[j][0]
        thing2=li[j][1]
        if thing[3*i] == "T":
            tmp.append(10)
        elif thing[3*i] == "J":
            tmp.append(11)
        elif thing[3*i] == "Q":
            tmp.append(12)
        elif thing[3*i] == "K":
            tmp.append(13)
        elif thing[3*i] == "A":
            tmp.append(14)
        else : tmp.append(int(thing[3*i]))

        if thing2[3*i] == "T":
            tmp2.append(10)
        elif thing2[3*i] == "J":
            tmp2.append(11)
        elif thing2[3*i] == "Q":
            tmp2.append(12)
        elif thing2[3*i] == "K":
            tmp2.append(13)
        elif thing2[3*i] == "A":
            tmp2.append(14)
        else : tmp2.append(int(thing2[3*i]))
    s1ar2.append(tmp2)
    s1ar1.append(tmp)
    
nalim1=np.sort(s1ar1,axis=1)
nalim1=np.fliplr(nalim1)
nalim2=np.sort(s1ar2, axis=1)
nalim2=np.fliplr(nalim2)
s1ar2=np.reshape(s1ar2,(n,5))
s1ar1=np.reshape(s1ar1,(n,5))
# s1ar12 : number, n*10 matrix
# nalim12 : n*10

whoins1=[]
for i in range(n):
    count=0
    a=1
    while a:
        if nalim1[i][count]>nalim2[i][count]:
            whoins1.append(1)
            a=0
        elif nalim1[i][count]<nalim2[i][count]:
            whoins1.append(2)
            a=0
        else: count+=1

# #########################################state2 pair

ispair1=np.zeros((n,1))
ispair2=np.zeros((n,1))
pairnum1=np.zeros((n,5))
pairnum2=np.zeros((n,5))
pair1=np.zeros((n,1))
pair2=np.zeros((n,1))
pairscore1=np.zeros((n,1))
pairscore2=np.zeros((n,1))

for i in range(n):
    for j in range(5):
        num1=0
        num2=0
        count1=0
        count2=0
        while count1 <= 4:
            if s1ar1[i][j] == s1ar1[i][count1] and j!=count1 :
                ispair1[i][0]=1
                pair1[i][0]+=0.5
                num1=s1ar1[i][j]
            count1 +=1
        while count2 <= 4:
            if s1ar2[i][j] == s1ar2[i][count2] and j!=count2:
                ispair2[i]=1
                pair2[i]+=0.5
                num2=s1ar2[i][j]
            count2 +=1
        pairnum1[i][j]=num1
        pairnum2[i][j]=num2

pairnum1=np.sort(pairnum1,axis=1)
pairnum1=np.fliplr(pairnum1)
pairnum2=np.sort(pairnum2,axis=1)
pairnum2=np.fliplr(pairnum2)

for i in range(n):
    pairscore1[i]=pair1[i]+pairnum1[i][0]*0.01+pairnum1[i][3]*0.0001
    pairscore2[i]=pair2[i]+pairnum2[i][0]*0.01+pairnum2[i][3]*0.0001
    # Full House
    if pair1[i] ==4 :
        fir1=pairnum1[i][0]
        sec1=pairnum1[i][3]
        arr1=pairnum1[i].tolist()
        n11=arr1.count(fir1)
        n12=arr1.count(sec1)
        ind11=arr1.index(fir1)
        ind12=arr1.index(sec1)
        if n11>n12:
            pairscore1[i]=pair1[i]+pairnum1[i][ind11]*0.01+pairnum1[i][ind12]*0.0001
        else: 
            pairscore1[i]=pair1[i]+pairnum1[i][ind12]*0.01+pairnum1[i][ind11]*0.0001
    
    if pair2[i] ==4 :
        fir2=pairnum2[i][0]
        sec2=pairnum2[i][3]
        arr2=pairnum2[i].tolist()
        n21=arr2.count(fir2)
        n22=arr2.count(sec2)
        ind21=arr2.index(fir2)
        ind22=arr2.index(sec2)
        if n21>n22:
            pairscore2[i]=pair2[i]+pairnum2[i][ind21]*0.01+pairnum2[i][ind22]*0.0001
        else: 
            pairscore2[i]=pair2[i]+pairnum2[i][ind22]*0.01+pairnum2[i][ind21]*0.0001
        

# two pair -> score = 2. ~~
# same num 3 -> score = 3. ~~ (state4, Three of a Kind)
# two, three -> score = 4. ~~ (state7, Full House)
# same num 4 -> score = 6. ~~ (state8, Four of a Kind)


# #######################################consecutive value
def checkCons(l): 
    return sorted(l) == list(range(min(l), max(l)+1))

def conseLowNum(l):
    a=sorted(l)
    return a[0]

state5_1=np.zeros((n,1))
state5_2=np.zeros((n,1))
txt1=[]
txt2=[]

for i in range(n):
    if checkCons(s1ar1[i]) == True :
        state5_1[i]=conseLowNum(s1ar1[i])
    if checkCons(s1ar2[i]) == True :
        state5_2[i]=conseLowNum(s1ar2[i])
            ###################################
    tmp=[]
    tmp2=[]
    for j in range(5):
        thing=li[i][0]
        thing2=li[i][1]
        tmp.append(thing[3*j+1])
        tmp2.append(thing2[3*j+1])
    txt2.append(tmp2)
    txt1.append(tmp)
    
txt2=np.reshape(txt2,(n,5))
txt1=np.reshape(txt1,(n,5))
  
def checkTxt(txt):
    result6=[]
    for i in range(n):
        if all(txt[i] == 'H'):
            result6.append(1)
        elif all(txt[i] == 'D'):
            result6.append(1)
        elif all(txt[i] == 'C'):
            result6.append(1)
        elif all(txt[i] == 'S'):
            result6.append(1)
        else: result6.append(0)
    return result6

st61=checkTxt(txt1)
st62=checkTxt(txt2)




## SCORE ######## ####### ######## #######
# two pair -> score = 2. ~~
# same num 3 -> score = 3. ~~ (state4, Three of a Kind)
# two, three -> score = 4. ~~ (state7, Full House)
# same num 4 -> score = 6. ~~ (state8, Four of a Kind)
# if 34567 -> state5 = 3.0 ,, else 0 (state5, Straight)
##   whoins2
score1=np.zeros((n,1))
score2=np.zeros((n,1))

def scoring(ps, st6, st5):
    score=0
    if 2>ps>=1 and st6==0:
        score=20+ps
    elif 3>ps>=2 and st6==0 :
        score=30+ps
    elif 4>ps>=3 and st6==0 :
        score=40+ps
    elif 5>ps>=4 and st6==0 :
        score=70+ps
    elif 7>ps>=6 and st6==0 :
        score=80+ps
    elif st5 >0 and st6==0 :
        score=50+st5*0.1
    elif st6 >0 :
        score=60
    elif st5>0 and st6 ==1:
        score=90 + st5*0.1
    elif st5==10 and st6 ==1:
        score=100
    return score

countp1=0
countp2=0
for i in range(n):
    score1[i]=scoring(pairscore1[i], st61[i], state5_1[i])
    score2[i]=scoring(pairscore2[i], st62[i], state5_2[i])
    if score1[i]>score2[i] :
        countp1 +=1
    elif score1[i]<score2[i] :
        countp2+=1
    elif score1[i]==score2[i]:
        countp1 +=abs(whoins1[i]-2)
        countp2 += whoins1[i]-1


print('Player 1 win',countp1,'times')
print('Player 2 win',countp2,'times')

