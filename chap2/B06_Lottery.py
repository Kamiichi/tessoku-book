N = int(input())
lottery = list(map(int, input().split()))

win = [0]
for i in range(N):
    s = win[i] + lottery[i]
    win.append(s)

def judge(l, r):
    result = ""
    if (r - (l - 1)) == (win[r] - win[l - 1]) * 2:
        result = "draw"
    elif (r - (l - 1)) < (win[r] - win[l - 1]) * 2:
        result = "win"
    else:
        result = "lose"
    print(result)

Q = int(input())
for i in range(Q):
    L, R = map(int, input().split())
    judge(L, R)

# 上でACしたけど、教科書の方には当たり、ハズレのそれぞれの累積和を作ってごらんと書いてあったので
# 以下に別解を示す。

# 上記/別解の実行速度の差は519/508msだった。別解の方が早い
# 上記/別解のメモリの差は14200/15108KBだった。上記の方が省メモリ.
# 感触としてはメモリと速度はトレードオフだけど、当たりくじの累積和が決まれば自動的に外れくじの累積も求まるという気づきが
# 結構うれしかった。工夫できていたかなと思うので。

# N = int(input())
# lottery = list(map(int, input().split()))

# win = [0]
# lose = [0]
# for i in range(N):
#     if lottery[i] == 1:
#         s = win[i] + 1
#         win.append(s)
#         lose.append(lose[i])
#     else:
#         s = lose[i] + 1
#         win.append(win[i])
#         lose.append(s)

# Q = int(input())
# for i in range(Q):
#     L, R = map(int, input().split())
#     if win[R] - win[L-1] == lose[R] - lose[L-1]:
#         print("draw")
#     elif win[R] - win[L-1] > lose[R] - lose[L-1]:
#         print("win")
#     else:
#         print("lose")