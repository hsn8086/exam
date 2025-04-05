def binary_search(query: callable, left: int, right: int):
    while left < right:
        mid = (left + right + 1) // 2
        if query(mid) <= 0:
            left = mid
        else:
            right = mid - 1
    return left

