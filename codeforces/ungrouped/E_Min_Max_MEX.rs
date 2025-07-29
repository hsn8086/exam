use std::collections::{HashMap, HashSet};
use std::io;

fn main() {
    let stdin = io::stdin();
    let mut input = String::new();
    
    // Read number of test cases
    stdin.read_line(&mut input).unwrap();
    let t: i64 = input.trim().parse().unwrap();
    input.clear();
    
    for _ in 0..t {
        // Read n and k
        stdin.read_line(&mut input).unwrap();
        let parts: Vec<i64> = input.split_whitespace()
            .map(|s| s.parse().unwrap())
            .collect();
        let (n, k) = (parts[0], parts[1]);
        input.clear();
        
        // Read array a
        stdin.read_line(&mut input).unwrap();
        let a: Vec<i64> = input.split_whitespace()
            .map(|s| s.parse().unwrap())
            .collect();
        input.clear();
        
        // Calculate mex
        let mut mex = 0;
        let mut s: HashSet<i64> = a.iter().cloned().collect();
        while s.contains(&mex) {
            mex += 1;
        }
        
        // Count frequencies
        let mut cnt = HashMap::new();
        for &num in &a {
            *cnt.entry(num).or_insert(0) += 1;
        }
        
        let mut left = 0;
        let mut right = mex;
        let mut ans = 0;
        
        while left <= right {
            let mid = (left + right) / 2;
            let mut valid = true;
            
            if mid > 0 {
                for i in 0..mid {
                    if !s.contains(&i) || cnt.get(&i).map_or(0, |&v| v) < k {
                        valid = false;
                        break;
                    }
                }
                if !valid {
                    right = mid - 1;
                    continue;
                }
            }
            
            if mid == 0 {
                if k <= n {
                    ans = 0;
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            } else {
                let req = mid;
                let mut c_cnt = HashMap::new();
                let mut c_seg = 0;
                let mut col = 0;
                
                for &num in &a {
                    if 0 <= num && num < req {
                        if !c_cnt.contains_key(&num) {
                            col += 1;
                        }
                        *c_cnt.entry(num).or_insert(0) += 1;
                        
                        if col == req {
                            c_seg += 1;
                            c_cnt.clear();
                            col = 0;
                        }
                    }
                }
                
                if c_seg >= k {
                    if mid > ans {
                        ans = mid;
                    }
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        
        println!("{}", ans);
    }
}