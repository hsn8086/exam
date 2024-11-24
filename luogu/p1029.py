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
@File       : p1029.py

@Author     : hsn

@Date       : 2024/9/29 下午6:21
"""

import math


def count_pairs(x0, y0):
    if y0 % x0 != 0:
        return 0

    c = y0 // x0
    count = 0

    for a in range(1, int(math.sqrt(c)) + 1):
        if c % a == 0:
            b = c // a
            if math.gcd(a, b) == 1:
                if a == b:
                    count += 1
                else:
                    count += 2

    return count

x0, y0 = map(int, input().split())

print(count_pairs(x0, y0))

# import math
#
# inp = input()
# x, y = map(int, inp.split())
# count = 0
# for i in range(x, int(math.sqrt(x*y))):
#     for j in range(i, y+1):
#         if gcd(i, j) == x and _min(i, j) == y:
#             count += 1
# print(count*2)
# inp = input()
# x, y = map(int, inp.split())
# while True:
#     a = random.randint(2, 1000)
#     b = random.randint(a, 1000)
#     try:
#         assert gcd(a, b) == a and _min(a, b) == b
#     except:
#         print(a, b, gcd(a, b), _min(a, b))
