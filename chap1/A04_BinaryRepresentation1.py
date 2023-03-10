N = int(input())

ans = ""

for i in range(10)[::-1]:   # 逆ループの書き方、よく覚えておくこと
    wari = 2 ** i
    ans += str(N // wari % 2)

# 10桁の2進数表記を求めるという仕様なので
# 繰り返し回数は最大10回で良いと着目する。

# 各桁の重みで10進数を割って
# その答えの2の剰余を求める。
# 1桁ずつ求めていく

print(ans)