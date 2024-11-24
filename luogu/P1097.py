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
@File       : P1097.py

@Author     : hsn

@Date       : 2024/9/29 下午6:05
"""


# from collections import OrderedDict
# count = int(input())
# nums = []
# for i in range(count):
#     nums.append(int(input()))
# count_map = {i: 0 for i in nums}
# for v in nums:
#     count_map[v] += 1
# for v, count in count_map.items():
#     print(v, count)



count = int(input())
nums = []
for i in range(count):
    nums.append(int(input()))
sorted_list = sorted(nums)
count = 1
last = None
for i in sorted_list:
    if last == i:
        count += 1
    else:
        if last is not None:
            print(last, count)
        count = 1
    last = i
print(last, count)
