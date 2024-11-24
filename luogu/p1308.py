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
@File       : p1308.py

@Author     : hsn

@Date       : 2024/9/29 下午6:33
"""

"""
python
 It's    all based on standard pyPython type declarations (thanks to Pydantic). No new syntax to learn. Just standard modern Python
"""
# word = input().lower()
# sentences = input().lower()
#
# if count := list(sentences.split()).count(word):
#     idx = f" {sentences} ".find(f" {word} ")
#
#     print(count, idx-1)
# else:
#     print(-1)
# word = input().lower()
# sentences = list(input().lower().split())
#
# if count := list(sentences).count(word):
#
# else:
#     print(-1)
"""
To
be or not to be is a question
"""
# word = input().lower()
# sentences = list(input().lower().split())
# if count := sentences.count(word):
#     idx_l = sentences.index(word)
#     idx_t = len(" ".join(sentences[:idx_l])) + 1
#
#     print(count, idx_t)
# else:
#     print(-1)
"""
to
to Did the Ottoman Empire lose its power at that time to
"""
word = input().lower()
sentences = input().lower()
count = 0
first = -1
now = ""
for i, alpha in enumerate(sentences):
    now += alpha
    if alpha == " ":
        if now[:-1] == word:
            count += 1
            if first == -1:
                first = i - len(word)

        now = ""

if now == word:
    count += 1
    if first == -1:
        first = len(sentences) - len(word)
if count:
    print(count, first)
else:
    print(-1)
