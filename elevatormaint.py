#!/usr/bin/env python2
def solution(l):
    l=sorted([list(int(i) for i in j.split(".")) for j in l])
    l=[".".join(list(str(i) for i in j)) for j in l]
    return l

print(solution(['2.0.0','2','1.2.2','1.2.0','2','1.2','1.15']))
#   1.2 , 1.2.0 , 1.2.2 , 1.15 , 2 , 2 , 2.0.0
#print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))
#    0.1 , 1.1.1 , 1.2 , 1.2.1 , 1.11 , 2 , 2.0 , 2.0.0
#print(solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]))
#    1.0 , 1.0.2 , 1.0.12 , 1.1.2 , 1.3.3
