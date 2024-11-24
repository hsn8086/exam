#include <iostream>
#include <vector>

const int MOD = 1e9 + 7;

// Function to calculate incorrect binomials
std::vector<std::vector<int>> calculate_incorrect_binomials(int N) {
    std::vector<std::vector<int>> C(N, std::vector<int>(N, 0));

    // Initialize base cases
    for (int n = 0; n < N; ++n) {
        C[n][0] = C[n][n] = 1;
    }

    // Fill the table using the incorrect formula
    for (int n = 2; n < N; ++n) {
        for (int k = 1; k < n; ++k) {
            C[n][k] = (C[n][k - 1] + C[n - 1][k - 1]) % MOD;
        }
    }

    return C;
}

int main() {
    int t;
    std::cin >> t;  // Number of test cases

    // Read all n and k values
    std::vector<int> n_values(t);
    std::vector<int> k_values(t);
    for (int i = 0; i < t; ++i) {
        std::cin >> n_values[i];
    }
    for (int i = 0; i < t; ++i) {
        std::cin >> k_values[i];
    }

    // Assuming the maximum n won't exceed 100000 as per constraints
    int max_n = 0;
    for (int n : n_values) {
        max_n = std::max(max_n, n);
    }
    max_n++; // Increase max_n to account for the array indexing

    auto C = calculate_incorrect_binomials(max_n);

    // Output results
    for (int i = 0; i < t; ++i) {
        std::cout << C[n_values[i]][k_values[i]] << std::endl;
    }

    return 0;
}
