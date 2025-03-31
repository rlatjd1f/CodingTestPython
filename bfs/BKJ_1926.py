import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().strip().split())
map = [list(map(int, input().strip().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
count = 0
max_val = 0


def dfs(y, x):
    rs = 1
    queue = deque()
    queue.append((y, x))

    while queue:
        by, bx = queue.popleft()
        for k in range(4):
            ny, nx = by + dy[k], bx + dx[k]

            if -1 < ny < n and -1 < nx < m:
                if map[ny][nx] == 1 and chk[ny][nx] == False:
                    chk[ny][nx] = True
                    rs += 1
                    queue.append((ny, nx))
    return rs

for j in range(n):
    for i in range(m):
        if map[j][i] == 1 and chk[j][i] == False:
            chk[j][i] = True
            count += 1
            max_val = max(max_val, dfs(j, i))

print(count)
print(max_val)
