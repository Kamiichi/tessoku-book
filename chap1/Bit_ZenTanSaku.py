N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = "No"

for i in range(1, N+1):
    sum = 0
    for j in range(i+1, N):
        wari = (j - 1) ** 2
        if i // wari % 2 == 1:
            sum += 1
    if sum == K:
        ans = "Yes"

print(ans)