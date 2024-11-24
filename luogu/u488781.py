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
@File       : u488781.py

@Author     : hsn

@Date       : 2024/10/9 下午4:21
"""

n, m = map(int, input().split())

a = list(map(int, input().split()))

prefix_xor = [0] * (n + 1)

for i in range(1, n + 1):
    prefix_xor[i] = prefix_xor[i - 1] ^ a[i - 1]

for _ in range(m):
    l, r = map(int, input().split())
    print(prefix_xor[r] ^ prefix_xor[l - 1])

"""
5 3 
1 2 3 4 5
1 3
1 4
3 5"""
