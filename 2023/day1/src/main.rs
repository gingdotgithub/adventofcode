use regex::Regex;
use std::collections::HashMap;

fn main() {
    part1();
    part2();
}

fn part1() {
    let mut answer:u32 = 0;
    let re = Regex::new(r"[^0-9]").unwrap();
    let my_str = include_str!("1.in");
    let data = my_str.split("\n");
    for line in data {
        let result = re.replace_all(line,"");
        let strlen = result.len();
        let combined = format!("{}{}",&result[0..1],&result[strlen-1..]);
        answer += combined.parse::<u32>().unwrap();
    }
    println!("{}",answer);
}

fn part2() {
    let mut answer:u32 = 0;
    let conversions = HashMap::from([
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
        ("6","6"),
        ("7","7"),
        ("8","8"),
        ("9","9"),
        ("one", "1"),
        ("two", "2"),
        ("three", "3"),
        ("four", "4"),
        ("five", "5"),
        ("six", "6"),
        ("seven", "7"),
        ("eight", "8"),
        ("nine", "9"),
    ]);
    println!("{}",answer);
}

// fn findReplacements(line: String, R2L: bool) -> String {
//     let convert = HashMap::new();

//     if R2L == true { 
        
//     }
// }
