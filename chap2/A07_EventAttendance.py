D = int(input())
N = int(input())

date = [0] * (D + 2)

for i in range(N):
    L, R = map(int, input().split())
    date[L] += 1
    date[R + 1] -= 1
date.pop(0)

sum_list = [0]

for i in range(D):
    s = sum_list[i] + date[i]
    sum_list.append(s)
sum_list.pop(0)

for i in sum_list:
    print(i)