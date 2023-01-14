H = 1502
W = 1502

l = [[0 for i in range(W)] for j in range(H)]
sum = [[0 for i in range(W)] for j in range(H)]

N = int(input())

for i in range(N):
    a, b, c, d = map(int, input().split())
    l[a][b] += 1
    l[c][d] += 1
    l[a][d] -= 1
    l[c][b] -= 1

for i in range(H):
    for j in range(W):
        sum[i][j] = sum[i][j-1] + l[i][j]

for j in range(W):
    for i in range(H):
        sum[i][j] = sum[i-1][j] + sum[i][j]

ans = 0
for i in range(H):
    for j in range(W):
        if sum[i][j] > 0:
            ans += 1

print(ans)