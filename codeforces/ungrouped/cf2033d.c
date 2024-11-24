#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to find the maximum number of beautiful segments
int max_beautiful_segments(int n, int *arr) {
    int *prefix_sum = (int *)malloc((n + 1) * sizeof(int));
    prefix_sum[0] = 0;
    for (int i = 0; i < n; i++) {
        prefix_sum[i + 1] = prefix_sum[i] + arr[i];
    }

    int *dp = (int *)malloc((n + 1) * sizeof(int));
    memset(dp, 0, (n + 1) * sizeof(int));

    // Hash map to store the last seen index of each prefix sum
    int *seen = (int *)malloc((2 * 100000 + 1) * sizeof(int)); // Adjust this based on constraints
    for (int i = 0; i <= 2 * 100000; i++) seen[i] = -1; // Initialize with -1
    seen[100000] = 0; // 0 sum last seen at index 0 (shifted to handle negative sums)

    for (int i = 1; i <= n; i++) {
        int shifted_sum = prefix_sum[i] + 100000; // Shift to positive index

        // If the current prefix sum has been seen before, we can potentially form a new segment
        if (seen[shifted_sum] != -1) {
            int last = seen[shifted_sum];
            dp[i] = dp[i - 1] > dp[last] + 1 ? dp[i - 1] : dp[last] + 1;
        } else {
            dp[i] = dp[i - 1];
        }
        // Update the last seen position of the current prefix sum
        seen[shifted_sum] = i;
    }
    int result = dp[n];

    free(prefix_sum);
    free(dp);
    free(seen);

    return result;
}

int main() {
    int t;
    scanf("%d", &t);
    while (t--) {
        int n;
        scanf("%d", &n);
        int *arr = (int *)malloc(n * sizeof(int));
        for (int i = 0; i < n; i++) {
            scanf("%d", &arr[i]);
        }
        printf("%d\n", max_beautiful_segments(n, arr));
        free(arr);
    }
    return 0;
}
