import sys

input = sys.stdin.readline

N, K = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))
nums.sort()

print(nums[K - 1])
