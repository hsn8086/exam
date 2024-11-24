#include <stdio.h>
#include <stdlib.h>

void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// 最大堆的上滤
void heapify_up(int heap[], int index) {
    while (index > 0) {
        int parent = (index - 1) / 2;
        if (heap[parent] > heap[index]) {
            swap(&heap[parent], &heap[index]);
            index = parent;
        } else {
            break;
        }
    }
}

// 最大堆的下滤
void heapify_down(int heap[], int size, int index) {
    while (2 * index + 1 < size) {
        int left_child = 2 * index + 1;
        int right_child = 2 * index + 2;
        int smallest = left_child;

        if (right_child < size && heap[right_child] < heap[left_child]) {
            smallest = right_child;
        }

        if (heap[index] > heap[smallest]) {
            swap(&heap[index], &heap[smallest]);
            index = smallest;
        } else {
            break;
        }
    }
}

void push(int heap[], int* size, int value) {
    heap[*size] = value;
    (*size)++;
    heapify_up(heap, *size - 1);
}

void pop(int heap[], int* size) {
    heap[0] = heap[*size - 1];
    (*size)--;
    heapify_down(heap, *size, 0);
}

int top(int heap[]) {
    return heap[0];
}

int solve(int n, int k, int an[]) {
    int heap[k + 1];  // 最大堆数组，大小为k + 1
    int heap_size = 0;

    for (int i = 0; i < n; i++) {
        if (heap_size <= k) {
            push(heap, &heap_size, -an[i]); // 压入负值实现最大堆效果
        } else {
            push(heap, &heap_size, -an[i]);
            pop(heap, &heap_size);
        }
    }
    
    return -top(heap); // 返回堆顶元素，变为正值
}

int main() {
    int n, k;
    scanf("%d %d", &n, &k);
    int an[n];
    
    for (int i = 0; i < n; i++) {
        scanf("%d", &an[i]);
    }

    printf("%d\n", solve(n, k, an));

    return 0;
}
