#pythonの再帰上限を引き上げるためだけど計算終わらないと思うから無意味
import sys
sys.setrecursionlimit(10**9)

def Ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return Ackermann(m-1, 1)
    else:
        return Ackermann(m-1, Ackermann(m, n-1))

print(Ackermann(3, 3))