#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#  Copyright (C) 2024. Suto-Commune
#  _
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#  _
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#  _
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
@File       : p1012.py

@Author     : hsn

@Date       : 2024/9/30 上午3:50
"""
# count = int(input())
# nums = list(input().split())
#
#
# def normalise(a, max_len):
#     return int(a + "0" * (max_len - len(a)))
#
#
# print("".join(sorted(nums, key=lambda x: normalise(x, max(*map(len, nums))), reverse=True)))
from functools import cmp_to_key


def compare(a, b):
    if a + b > b + a:
        return -1
    elif a + b < b + a:
        return 1
    else:
        return 0


n = int(input())
nums = list(map(str, input().split()))

nums.sort(key=cmp_to_key(compare))

if nums[0] == '0':
    print(0)
else:
    print(''.join(nums))
