import sys
import heapq

# 입력 받기
n = int(sys.stdin.readline())
classes = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 시작 시간 기준으로 정렬
classes.sort()

# 최소 힙 생성
heap = []

for start, end in classes:
    # 현재 수업 시작시간이 가장 빨리 끝나는 수업 끝난 이후면 → 그 방 재사용
    if heap and heap[0] <= start:
        heapq.heappop(heap)

    # 현재 수업 끝나는 시간 추가 (새 강의실이든 재사용이든)
    heapq.heappush(heap, end)

# 힙에 남아 있는 수업 수 = 필요한 강의실 수
print(len(heap))
