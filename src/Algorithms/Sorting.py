def bubble_sort(nums: list[int]) -> list[int]:
    swap = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                swap += 1
    print("Number of swaps: ", swap)
    return nums


def insertion_sort(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key

    return nums


# def merge_sort(nums: list[int]) -> list[int]:
#     if len(nums) <= 1:
#         return nums
#
#     mid = len(nums)//2
#
#     def merge(left, right):
#         sorted_arr = []
#         l = 0
#         r = 0
#
#     left_half = merge_sort(nums[:mid+1])
#     right_half = merge_sort(nums[mid+1:])
#
#     return nums
