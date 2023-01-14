import pprint

H, W = map(int, input().split())

field = [[0] * (W+1)]

for i in range(H):
    l = list(map(int, input().split()))
    l.insert(0, 0)
    field.append(l)

# この書き方で3時間ハマってしまった。やられた。。。
# twoDimensionalSum = [[0] * (W+1)] * (H+1)
twoDimensionalSum = [[0 for i in range(W+1)] for j in range(H+1)]
# pprint.pprint(twoDimensionalSum)
# pprint.pprint(field)

# print(twoDimensionalSum[0] == twoDimensionalSum[1])
# print(twoDimensionalSum[0] is twoDimensionalSum[1])

for i in range(1, H+1):
    for j in range(1, W+1):
        # print(f'i: {i}, j: {j}')
        # print(f'TDS: {twoDimensionalSum[i][j-1]}, field: {field[i][j]}')
        # print(field[i])
        twoDimensionalSum[i][j] = twoDimensionalSum[i][j-1] + field[i][j]
        # pprint.pprint(twoDimensionalSum)

# print("--------------------------------------")
for j in range(1, W+1):
    for i in range(1, H+1):
        # print(f'i: {i}, j: {j}')
        twoDimensionalSum[i][j] = twoDimensionalSum[i-1][j] + twoDimensionalSum[i][j]
        # pprint.pprint(twoDimensionalSum)

Q = int(input())

def some_func(a, b, c, d, plane):
    print(plane[c][d] + plane[a-1][b-1] - plane[a-1][d] - plane[c][b-1])

for i in range(Q):
    A, B, C, D = map(int, input().split())
    some_func(A, B, C, D, twoDimensionalSum)