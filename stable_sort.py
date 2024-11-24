









def sort(arr: list[int], left: int, right: int) -> list[int]:
    mid = (left + right) // 2

    if left == right:
        return [arr[left]]

    left_list = sort(arr, left=left, right=mid)
    right_list = sort(arr, left=mid + 1, right=right)

    sorted_list = []
    left_e = left_list.pop(0)
    right_e = right_list.pop(0)

    while 1:
        if left_e > right_e:
            sorted_list.append(right_e)
            if right_list:
                right_e = right_list.pop(0)
            else:
                right_e = float("+inf")
        else:
            sorted_list.append(left_e)
            if left_list:
                left_e = left_list.pop(0)
            else:
                left_e = float("+inf")

        if left_e == float("+inf") and right_e == float("+inf"):
            break

    return sorted_list


import random

arr = [random.randint(1, 10000) for i in range(20)]
sorted_l = sort(arr, 0, len(arr) - 1)
print(sorted_l)
