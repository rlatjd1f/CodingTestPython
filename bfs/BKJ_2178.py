import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().strip().split())
xmap = [list(str(input().strip())) for _ in range(n)]
chk_map = [[False] * m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y):
    res = 0
    queue = deque()
    queue.append((x, y))

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if -1 < nx < m and -1 < ny < n:
                if chk_map[ny][nx] == False and xmap[ny][nx] == '1':
                    chk_map[ny][nx] = True
                    res += 1
                    queue.append((nx, ny))

    return res


print(bfs(0, 0))
