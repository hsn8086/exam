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
@File       : U488794.py

@Author     : hsn

@Date       : 2024/10/9 下午3:52
"""

# n, k = map(int, input().split())
# an = list(map(int, input().split()))
#
#
# def clac(l, i, k):
#     return sum(l[i:i + k])
#
#
# i_l = 0
# i_r = k - 1
# rst = 0
# for _ in range(n - k + 1):
#     rst = max(rst, clac(an, i_l, k) + clac(an, i_r, k))
#     if clac(an, i_l, k) > clac(an, i_r, k):
#         i_r -= 1
#     else:
#         i_l += 1
# rst = max(rst, clac(an, i_l, k) + clac(an, i_r, k))
# print(rst)
#
n, k = map(int, input().split())
a = list(map(int, input().split()))


sum_k = [0] * (n - k + 1)
current_sum = sum(a[:k])
sum_k[0] = current_sum

for i in range(1, n - k + 1):
    current_sum = current_sum - a[i - 1] + a[i + k - 1]
    sum_k[i] = current_sum

max_sum_k_before = [0] * (n - k + 1)
max_sum_k_before[0] = sum_k[0]

for i in range(1, n - k + 1):
    max_sum_k_before[i] = max(max_sum_k_before[i - 1], sum_k[i])

max_total = float("-inf")

for R in range(k, n - k + 1):
    max_total = max(max_total, sum_k[R] + max_sum_k_before[R - k])
print(max_total)


# n,k=map(int,input().split())
# a=map(int,input().split())
# sum_k=[0]*(n+k-1)
# current_sum=sum(a[:k])
# sum_k[0]=current_sum

# for i in range(1,n+k-1):
#     current_sum=current_sum-a[i-1]+a[i+k-1]
#     sum_k[i]=current_sum

# max_sum_k_beforce=
