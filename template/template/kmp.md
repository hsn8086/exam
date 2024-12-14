# KMP
## Code
``` python
def kmp(text, pattern):
    if not pattern:
        return 0

    # Build failure function
    failure = [0] * len(pattern)
    i = 1
    j = 0
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            failure[i] = j + 1
            i += 1
            j += 1
        elif j > 0:
            j = failure[j-1]
        else:
            failure[i] = 0
            i += 1

    # Find pattern in text
    i = 0  # index in text
    j = 0  # index in pattern
    while i < len(text):
        if pattern[j] == text[i]:
            if j == len(pattern) - 1:
                return i - j
            i += 1
            j += 1
        elif j > 0:
            j = failure[j-1]
        else:
            i += 1
    return -1
```