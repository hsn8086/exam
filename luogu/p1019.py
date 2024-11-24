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
@File       : p1019.py

@Author     : hsn

@Date       : 2024/9/30 上午4:26
"""
import copy

count = int(input())
words = [input() for _ in range(count)]
start = words[0]


def dfs(start, words, path):
    if len(path) == count:
        return [path]
    rt = []
    for i, v in enumerate(words):
        if i in path:
            continue
        if start == v[0]:
            path.append(i)
            res = dfs(v[0], words, copy.deepcopy(path))
            rt.extend(res)
            path.pop()
    return rt

path=[]
print(dfs(start, words, path))      
