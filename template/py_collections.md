# Counter
## 初始化方式

```python
c = Counter()                           # 空计数器
c = Counter('gallahad')                 # 从可迭代对象创建
c = Counter({'red': 4, 'blue': 2})      # 从字典创建  
c = Counter(cats=4, dogs=8)             # 从关键字参数创建
```

## 主要特性

- 访问不存在的键返回0而不是KeyError
- 设置计数为0不会删除元素，需使用del删除
- 继承dict的所有方法
- 3.7版本后保持插入顺序

## 特殊方法

1. `elements()`: 返回元素迭代器，每个元素重复其计数次
2. `most_common([n])`: 返回出现次数最多的n个元素
3. `subtract([iterable])`: 从另一个可迭代对象中减去元素计数
4. `update([iterable])`: 从另一个可迭代对象中增加元素计数

## 数学运算

支持以下运算符:

```python
c + d    # 相加: c[x] + d[x]
c - d    # 相减: 保持正计数
c & d    # 交集: min(c[x], d[x])
c | d    # 并集: max(c[x], d[x])
+c       # 保留正计数
-c       # 取反计数
```

## 常用操作

```python
sum(c.values())                 # 计数总和
c.clear()                       # 重置所有计数
list(c)                        # 唯一元素列表
dict(c)                        # 转换为普通字典
c.items()                      # 转换为(元素,计数)对列表
```
