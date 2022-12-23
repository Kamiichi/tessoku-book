A, B = map(int, input().split())

ans = "No"

for n in range(A, B+1): # A以上B以下の範囲を検索したい。Bに+1するのを忘れずにね。
    if 100 % n == 0:
        ans = "Yes"
        break

print(ans)