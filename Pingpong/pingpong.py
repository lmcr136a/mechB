import numpy as np
import math

def mylen(n):
    return int(math.log10(n)) + 1 if n else 0

def ping(n): # 반드시 숫자의 자릿수를 넣어야 합니다.
    li1=[]
    if n<=1 :
        return [0,7]
    
    if n == 2 : 
        li1=[x*10**(n-2)+y*10**(n-1) for x,y in zip([i for i in range(0,10)], [7 for i in range(0,10)])]
        li1+=[y*10**(n-2)+x*10**(n-1) for x,y in zip([i for i in range(0,10)], [7 for i in range(0,10)])]

    else:
        l1=[i for i in range(10)]
        lix=[val for val in l1 for _ in range(len(ping(n-1)))]
        lix2=[i for i in range(10**(n-1))]
        liy2=[7 for i in range(0,10**(n-1))]
        li1+=[y+x*10**(n-1) for x,y in zip(lix, ping(n-1)*9**(n-1))]
        li1+=[y*10**(n-1)+x for x,y in zip(lix2, liy2)]
   
    
    li1+=[i*7 for i in range(0,10**(n)//7) ]   
    li1 = list(set(li1))
    li1.sort()
    return li1

# ord =1 val=7,   ord=2, val=0,,, val을 보여주는 함수
def pong(ord, num):
    if ord < 1:
        return 0
    elif ord==1:
        return 7    
    elif ord%2 >0:
        return pong(ord-1,num)+(ping(mylen(num))[ord]-ping(mylen(num))[ord-1])
    elif ord%2 ==0:
        return pong(ord-1,num)-(ping(mylen(num))[ord]-ping(mylen(num))[ord-1])


def clos(li, num):
    if num<=7:
        return 0
    elif ping(mylen(num))[np.abs(np.array(li)-num ).argmin()] < num :
        return np.abs(np.array(li)-num ).argmin()
    elif ping(mylen(num))[np.abs(np.array(li)-num ).argmin()] >= num:
        return np.abs(np.array(li)-num ).argmin() -1


def pingpong(num):
    n=clos(ping(mylen(num)),num)
    print('n=',n)
    if n%2 != 0:
        return pong(n,num)-num+ping(mylen(num))[n]
    else:
        return pong(n,num)+(num-ping(mylen(num))[n])


a=pingpong(199) # 
b=pingpong(1000) # 
c=pingpong(100) # 

print('\n\n', a,'\n',b,'\n',c)
 



 







