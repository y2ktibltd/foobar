#!/usr/bin/env python2
from random import randint
def solution(m,f):
    m=int(m)
    f=int(f)
    gen=0
    while not m==f==1:
        gen+=1
        print("m",m,"f",f,"gen",gen)
        if f%2==0 and m%2==0:
            return "impossible"
        if f==0 or m==0:
            return "impossible"
        if m==f and m!=1:
            return "impossible"
        if f//m>2 and m!=1:
            print("f/m>1",gen)
            print(int(f/m))
            gen+=(f//m)-1
            f-=(f//m)*m
            continue
        if f>m:
            print("f>m",gen)
            f-=m
            continue
        if m//f>2 and f!=1:
            print("f/m>1",gen)
            print(int(m/f))
            gen+=(m//f)-1
            m-=(m//f)*f
            continue
        if m>f:
            print("m>f",gen)
            m-=f
            continue
    return str(gen)

print(solution('4', '7')) # 4
print(solution('2', '1')) # 1
print(solution('100', '3')) # 1
#print(solution(str(randint(1,pow(10,50))),str(randint(1,pow(10,50)))))
