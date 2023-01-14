import pprint

H, W, N = map(int, input().split())

l = [[0 for i in range(W+2)] for j in range(H+2)]
sum = [[0 for i in range(W+2)] for j in range(H+2)]

# pprint.pprint(l)
for i in range(N):
    a, b, c, d = map(int, input().split())
    l[a][b] += 1
    l[c+1][d+1] += 1
    l[a][d+1] -= 1
    l[c+1][b] -= 1

for i in range(H+1):
    for j in range(W+1):
        sum[i][j] = sum[i][j-1] + l[i][j]

for j in range(W+1):
    for i in range(H+1):
        sum[i][j] = sum[i-1][j] + sum[i][j]

sum.pop(0)
sum.pop(H)
for i in range(H):
    sum[i].pop(0)
    sum[i].pop(W)
    print(*sum[i])
# pprint.pprint(sum)