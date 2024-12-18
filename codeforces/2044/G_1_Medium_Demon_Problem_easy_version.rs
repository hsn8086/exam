use std::collections::HashSet;
use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();

    // 读取测试用例数量
    let t: usize = lines.next().unwrap().unwrap().trim().parse().unwrap();

    for _ in 0..t {
        // 读取n
        let n: usize = lines.next().unwrap().unwrap().trim().parse().unwrap();
        // 读取r数组并减1
        let r: Vec<usize> = lines.next().unwrap().unwrap()
            .split_whitespace()
            .map(|x| x.parse::<usize>().unwrap() - 1)
            .collect();

        // 初始化当前集合
        let mut curr: HashSet<usize> = (0..n).collect();
        let mut seen: HashSet<HashSet<usize>> = HashSet::new();
        seen.insert(curr.clone());
        let mut year = 1;

        loop {
            // 更新当前集合
            curr = curr.iter().map(|&i| r[i]).collect();
            // 检查是否已见过
            if seen.contains(&curr) {
                println!("{}", year + 1);
                break;
            }
            seen.insert(curr.clone());
            year += 1;
        }
    }
}
