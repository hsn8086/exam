use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut iterator = stdin.lock().lines();
    
    let first_line = iterator.next().unwrap().unwrap();
    let parts: Vec<i64> = first_line.split_whitespace().map(|x| x.parse().unwrap()).collect();
    let (n, m, q) = (parts[0], parts[1], parts[2]);
    
    let a: Vec<i64> = iterator.next().unwrap().unwrap()
        .split_whitespace().map(|x| x.parse().unwrap()).collect();
    let b: Vec<i64> = iterator.next().unwrap().unwrap()
        .split_whitespace().map(|x| x.parse().unwrap()).collect();
    
    let total: i64 = a.iter().flat_map(|&a_i| b.iter().map(move |&b_j| a_i * b_j)).sum();
    let sum_a: i64 = a.iter().sum();
    let sum_b: i64 = b.iter().sum();
    
    let mut possible = std::collections::HashSet::new();
    for &a_i in &a {
        for &b_j in &b {
            let new_total = total - a_i * sum_b - b_j * sum_a + a_i * b_j;
            possible.insert(new_total);
        }
    }
    
    for _ in 0..q {
        if let Some(Ok(line)) = iterator.next() {
            let x: i64 = line.trim().parse().unwrap();
            if possible.contains(&x) {
                println!("YES");
            } else {
                println!("NO");
            }
        }
    }
}
