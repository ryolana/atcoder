# -*- coding: utf-8 -*-

S = input()
T = input()
#
# if S in T == True:
#     if T[0] == S[0]:
#         if T[len(S)-1] == S[len(S)-1]:
#             print('Yes')
# else:
#     print('No')

l = len(S)

for i in range(0,l):
    if S[i] == T[i]:
        i = i + 1
        if i == l: #lまで来たらYesを出して終了
            print('Yes')
            break
    else:
        print('No')
        break
