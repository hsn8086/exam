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
@File       : P9581.py

@Author     : hsn

@Date       : 2024/9/29 下午5:42
"""


def clac(a: int, b: int):
    if abs(a) > abs(b):
        _min = b
        _max = a
    else:
        _min = a
        _max = b

    print(abs(_max - _min) + abs(_min))


if __name__ == "__main__":
    inp = input()
    a, b = map(int, inp.split())
    clac(a, b)
