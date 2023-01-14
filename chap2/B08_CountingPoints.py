W = 1501
H = 1501

N = int(input())

l = [[0 for i in range(W)] for j in range(H)]

for i in range(N):
    px, py = map(int, input().split())
    l[px][py] += 1

sum = [[0 for i in range(W)] for j in range(H)]

for i in range(1, H):
    for j in range(1, W):
        sum[i][j] = sum[i][j-1] + l[i][j]

for j in range(1, W):
    for i in range(1, H):
        sum[i][j] = sum[i-1][j] + sum[i][j]

Q = int(input())

for i in range(Q):
    a, b, c, d = map(int, input().split())
    print(sum[c][d] + sum[a-1][b-1] - sum[a-1][d] - sum[c][b-1])