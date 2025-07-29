use std::collections::HashMap;

const MOD: i64 = 998244353;

fn factorial(n: i64, memo: &mut HashMap<i64, i64>) -> i64 {
    if n == 0 || n == 1 {
        return 1;
    }
    if let Some(&val) = memo.get(&n) {
        return val;
    }
    let res = (n as i64 * factorial(n - 1, memo)) % MOD;
    memo.insert(n, res);
    res
}

fn count(counts: &[i64], memo: &mut HashMap<i64, i64>) -> i64 {
    let total: i64 = counts.iter().sum();
    let mut denominator = 1;
    for &cnt in counts {
        denominator = (denominator * factorial(cnt, memo)) % MOD;
    }
    let total_fact = factorial(total, memo);
    // Modular division requires finding the modular inverse
    let inv_denominator = mod_inverse(denominator, MOD);
    (total_fact * inv_denominator) % MOD
}

fn mod_inverse(a: i64, m: i64) -> i64 {
    let mut m0 = m;
    let mut a0 = a;
    let mut y = 0;
    let mut x = 1;

    if m == 1 {
        return 0;
    }

    while a0 > 1 {
        let q = a0 / m0;
        let mut t = m0;

        m0 = a0 % m0;
        a0 = t;
        t = y;

        y = x - q * y;
        x = t;
    }

    if x < 0 {
        x += m;
    }

    x
}

fn find_partitions(a: &[i64], target: i64) -> Vec<(Vec<i64>, Vec<i64>)> {
    let n = a.len();
    let mut dp = vec![vec![0; (target + 1) as usize]; n + 1];
    dp[0][0] = 1;

    for i in 1..=n {
        for j in 0..=target as usize {
            dp[i][j] = dp[i - 1][j];
            if j >= a[i - 1] as usize {
                dp[i][j] += dp[i - 1][j - a[i - 1] as usize];
            }
        }
    }

    if dp[n][target as usize] == 0 {
        return vec![];
    }

    let mut result = vec![];

    fn backtrack(
        a: &[i64],
        dp: &[Vec<i64>],
        i: usize,
        current_sum: i64,
        path_indices: &mut Vec<usize>,
        result: &mut Vec<(Vec<i64>, Vec<i64>)>,
    ) {
        if current_sum == 0 {
            let b: Vec<i64> = path_indices.iter().map(|&idx| a[idx]).collect();
            let c: Vec<i64> = (0..a.len())
                .filter(|idx| !path_indices.contains(idx))
                .map(|idx| a[idx])
                .collect();
            result.push((b, c));
            return;
        }
        if i == 0 || current_sum < 0 {
            return;
        }
        if current_sum >= a[i - 1] && dp[i - 1][(current_sum - a[i - 1]) as usize] > 0 {
            path_indices.push(i - 1);
            backtrack(a, dp, i - 1, current_sum - a[i - 1], path_indices, result);
            path_indices.pop();
        }
        if dp[i - 1][current_sum as usize] > 0 {
            backtrack(a, dp, i - 1, current_sum, path_indices, result);
        }
    }

    backtrack(
        a,
        &dp,
        n,
        target,
        &mut vec![],
        &mut result,
    );

    result
}

fn main() {
    use std::io::{self, BufRead};

    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();

    let t: i32 = lines.next().unwrap().unwrap().trim().parse().unwrap();
    for _ in 0..t {
        let line = lines.next().unwrap().unwrap();
        let a: Vec<i64> = line
            .split_whitespace()
            .filter(|s| !s.is_empty())
            .map(|s| s.parse().unwrap())
            .collect();

        let value: i64 = a.iter().sum();
        if value % 2 != 0 {
            println!("0");
            continue;
        }
        let partitions = find_partitions(&a, value / 2);
        let mut memo = HashMap::new();
        let mut cnt = 0;
        for (b, c) in partitions {
            cnt = (cnt + (count(&b, &mut memo) * count(&c, &mut memo)) % MOD) % MOD;
        }
        println!("{}", cnt);
    }
}