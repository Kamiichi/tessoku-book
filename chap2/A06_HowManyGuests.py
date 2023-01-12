N, Q = map(int ,input().split())
A = list(map(int, input().split()))

# 累積和を求める
def sum_list(list):
    sum_list = [0]
    for i in range(N):
        sum = sum_list[i] + list[i]
        sum_list.append(sum)
    # sum_list.pop(0)
    return sum_list

# print(*sum_list(A))
sum_list = sum_list(A)

for i in range(Q):
    l, r = map(int, input().split())
    print(sum_list[r] - sum_list[l-1]) # L日目からR日目までの累計来場者数を求めたいなら,累積和のリストを作りだし、R日目-(L-1)日目の累積和を求めれば良いちょ