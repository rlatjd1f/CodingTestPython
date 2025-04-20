import sys
import heapq

input = sys.stdin.readline

# 입력 처리
n, k = map(int, input().strip().split())
jewels = [tuple(map(int, input().strip().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]

# 정렬
jewels.sort()  # 무게 기준 오름차순
bags.sort()

# 힙과 인덱스
total_value = 0
heap = []
jewel_idx = 0

for bag_weight in bags:
    # 현재 가방에 넣을 수 있는 보석을 다 힙에 넣음 (가격 기준 max heap)
    while jewel_idx < n and jewels[jewel_idx][0] <= bag_weight:
        heapq.heappush(heap, -jewels[jewel_idx][1])
        jewel_idx += 1

    # 가장 비싼 보석 선택
    if heap:
        total_value += -heapq.heappop(heap)

print(total_value)
