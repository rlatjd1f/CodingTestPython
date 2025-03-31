import sys

input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().strip().split()))
m = int(input())
m_list = list(map(int, input().strip().split()))

n_list.sort()


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


for i in m_list:
    result = binary_search(n_list, i, 0, n - 1)
    if result != None:
        print(1)
    else:
        print(0)
