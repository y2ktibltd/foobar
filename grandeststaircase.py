#!/usr/bin/env python3
def solution(n):
    res=[1]+[0 for i in range(n)]
    print(res)
    for i in range(1,n+1):
        for j in range(n,i-1,-1):
#            print(f"adding {j-i} to index {j}")
            res[j]+=res[j-i]
#            print("[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]")
#            print(res,"\n")
    return res[n]-1


print(solution(200)) # 487067745
print(solution(3)) # 1
