N = int(input())
A = list(map(int, input().split()))

ans = "No"

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if A[i] + A[j] + A[k] == 1000:
                ans = "Yes"
                break

# 多重ループの時に
# 重複排除して探索したいパターンを
# 記憶しているといいね

# range(N)となっているところ、
# range(len(A))と書いてしまいがち
# 配列の要素数が
# あらかじめ与えられる時には
# 素直にその値を使った方が
# コードが見やすいね

print(ans)