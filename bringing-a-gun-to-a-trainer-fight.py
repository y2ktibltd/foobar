#!/usr/bin/env python3
def solution(room,you,target,dist):
    graph=[[" " for i in range(room[0]+1)] for j in range(room[1]+1)]
    graph[you[1]][you[0]]="Y"
    graph[target[1]][target[0]]="T"
    for i in range(room[1]+1):
        print(graph[i])
    you_array=build_grid(room,you,dist)
#    target_array=build_grid(room,target,dist)

def build_grid(room,position,dist):
    tmp_ew=[[position[0],position[1]]]
    x1=2*position[0]
    x2=(room[0]-position[0])*2
    # Move WEST/EAST
    for i in range(1,dist,room[0]*2):
        tmp_ew.append([tmp_ew[-1][0]-x1,tmp_ew[-1][1]])
        tmp_ew.append([tmp_ew[-1][0]-x2,tmp_ew[-1][1]])

    x1=2*position[0]
    x2=(room[0]+position[0])*2
    tmp_ew.append([position[0]+x2,position[1]])
    for i in range(1,dist-room[0],room[0]*2):
        tmp_ew.append([tmp_ew[-1][0]+x1,tmp_ew[-1][1]])
        tmp_ew.append([tmp_ew[-1][0]+x2,tmp_ew[-1][1]])
    print(tmp_ew)        

    #Move SOUTH
    tmp_s=[]
    y1=2*position[1]
    y2=(room[1]-position[1])*2
    for i in range(int(len(tmp_ew)/2)):
        tmp_s.append([tmp_ew[i][1]-y2,tmp_ew[i][1]])
        tmp_s.append([tmp_ew[i][1]-y1,tmp_ew[i][1]])

    print(tmp_s)        








print(solution([3,2], [0,2], [2,0], 10))                     #12

#print(solution([3,2], [1,1], [2,1], 4))                     #7 
#print(solution([15,15], [1,1], [15,15], 4))                     #7 
#print(solution([300,275], [150,150], [185,100], 500))       #9
#print(solution([1250,1250], [0,0], [1250,1250], 10000))
