def binary_search(nums: list[int], target: int) -> list[int]:
    res = []
    for idx, val in enumerate(nums):
        res.append((idx, val))
    res = sorted(res, key=lambda x: x[1])
    print(res)
    idx = -1
    left = 0
    right = len(res) - 1
    print(nums)
    while left < right:

        mid = (left+right)//2
        if res[mid][1] < target:
            left = mid+1
        elif res[mid][1] > target:
            right = mid
        else:
            idx = res[mid][0]
            break

    return idx
