#!/usr/bin/env python3
def solution(n,b):
#    print(int(sorted('10210210'),3))
    loop=True
    k=len(n)
#    print(k)
    old_n=[]
#    print(n,type(n))
    base='0123456789abcdef'
    while loop:
        old_n.append(n)
#        print(n,type(n))
#        print(f"length of n:{n} is {k}\nOld Answers list:",old_n)
        while len(n)<k:
#            print("adding leading 0's")
            n="0"+n
#        print("making X")
        x=int("".join(sorted(n, reverse=True)),b)
#        print("x",("".join(sorted(n, reverse=True)),b),x)
#        print("making Y")
        y=int("".join(sorted(n)),b)
#        print("y",("".join(sorted(n)),b),y)
        z=x-y
#        print("z",z)
#        z=int(str(z),b)
#        print(f"length of n:{n} {type(n)} is {k}\n,z:{z},{type(z)},\nOld Answers list:",old_n)
#        print(f"{x} - {y} = {z}")
        if z==0:return 1
        ra=[]
        while z>0:
            r=z%b
            ra.append(r)
            z=z//b
        nd=[]
        while ra:
            nd.append(base[ra.pop()])
        n="".join(nd)
#        print(n)
        if n in old_n:
            return len(old_n)-(old_n.index(n))

print(solution('1211',10))  #   1
print(solution('210022',3)) #   3
