N, K = map(int, input().split())

ans = 0

# for i in range(N):
#     for j in range(i + 1, N):
#         for k in range(j + 1, N):
#             if i + j + k == K:
#                 ans += 1

# 3枚のカード全てを全探索すると
# 計算量が爆増する。
# 1 <= N <= 3000のため
# 正直な全探索は
# 3000 ^ 3 で 27,000,000,000 (270億通り)
# 4GHzのCPUだと
# 探索完了まで1分以上かかる

# そこで、計算量の削減を工夫する。
# ※このようなテクニックを覚えることが、競プロのテクニックとなる。

# 仕様から、3枚のカードの合計が目標値に一致するか調べたいが
# ここで2枚のカードの合計値が決まると
# 3枚目のカードは決まる
# ということに着目する

# そのため、実際に回すループは
# カード2枚分となり
# 1秒以内の計算量で済む。

# ループ書き直し
for x in range(1, N+1):
    for y in range(1, N+1):
        z = K - x - y
        if 1 <= z <= N:   # zの範囲が条件を満たしている。
            ans += 1
print(ans)