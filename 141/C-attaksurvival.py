#-*- coding:utf-8 -*-

n, k, q = map(int, input().split())
a_li = [int(input()) for i in range(q)]

b_li = [0]*n #加点用のリスト[0,0,0,0....]を容易
for i in range(q):
    b_li[a_li[i]-1] += 1 #a_li[i]番の人のに対応する位置のb_li[]に1点追加

# pt_li = [] #所持点数のリストを作る
# for i in range(n): #pt_liリストの後ろにk点を追加
#     pt_li.append(k)
#
#print(pt_li)
#
# for t in range(q): #t回目について
#     for u in range(n): #u人に対して
#         pt_li[u] -= 1 #とりあえずマイナス1
#     pt_li[a_li[t]-1] += 1
#
#
# #print(pt_li)
#
#
# for v in range(n):
#     if pt_li[v] <= -1:
#         pt_li[v] = 0
#
# #print(pt_li)
#
# for s in range(n):
#      if pt_li[s] == 0:
#          print("No")
#      else:
#          print("Yes")

for t in range(n):
    pt_li = k -q + b_li[t] #最終的なポイントは k点からq回1を引いて、加点する。
    if pt_li > 0:
        print("Yes")
    else:
        print("No")
