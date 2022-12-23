N, X = map(int, input().split())

num = list(map(int, input().split()))

ans = "No"

for n in num:
    if n == X:
        ans = "Yes"
        break

print(ans)