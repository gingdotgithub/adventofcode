use regex::Regex;

fn main() {
    part1()
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

// fn findReplacements(line: String, R2L: bool) -> String {
//     let convert = HashMap::new();

//     if R2L == true { 
        
//     }
// }
