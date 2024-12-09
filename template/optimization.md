# Optimization
## Python
### Recursion
``` python
import sys
sys.setrecursionlimit(10010)
```
### Sort
-  `functools.cmp_to_key(func)`

    将(旧式的)比较函数转换为新式的 key function . 在类似于 sorted() ， min() ， max() ， heapq.nlargest() ， heapq.nsmallest() ， itertools.groupby() 等函数的 key 参数中使用。此函数主要用作将 Python 2 程序转换至新版的转换工具，以保持对比较函数的兼容。

    比较函数意为一个可调用对象，该对象接受两个参数并比较它们，结果为小于则返回一个负数，相等则返回零，大于则返回一个正数。key function则是一个接受一个参数，并返回另一个用以排序的值的可调用对象。
### Cache
- `@functools.cache(user_function)`
  
    简单轻量级未绑定函数缓存。 有时称为 "memoize"。

    返回值与 lru_cache(maxsize=None) 相同，创建一个查找函数参数的字典的简单包装器。 因为它不需要移出旧值，所以比带有大小限制的 lru_cache() 更小更快。


- `@functools.lru_cache(maxsize=128, typed=False)`

    一个为函数提供缓存功能的装饰器，缓存 maxsize 组传入参数，在下次以相同参数调用时直接返回上一次的结果。用以节约高开销或I/O函数的调用时间。

    由于使用了字典存储缓存，所以该函数的固定参数和关键字参数必须是可哈希的。

    不同模式的参数可能被视为不同从而产生多个缓存项，例如, f(a=1, b=2) 和 f(b=2, a=1) 因其参数顺序不同，可能会被缓存两次。

