T = int(input())
N = int(input())

time = [0] * (T + 2)

for i in range(N):
    L, R = map(int, input().split())
    time[L] += 1
    time[R] -= 1

sum_list = [0]

for i in range(T):
    s = sum_list[i] + time[i]
    sum_list.append(s)
sum_list.pop(0)

for i in sum_list:
    print(i)