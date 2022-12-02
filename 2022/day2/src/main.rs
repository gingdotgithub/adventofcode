fn main() {
    let mut elf_points = 0;
    let my_str = include_str!("2.in");
    let data = my_str.split("\n");

    for entry in data {
        let go = go_score(entry.chars().last().unwrap());
        let result = go_outcome(entry);
        elf_points+= result + go;
    }
    println!("{elf_points}");
}

fn go_score(go: char) -> i32 {
    match go {
        'X' => return 1,
        'Y' => return 2,
        'Z' => return 3,
        _ => return 0,
    }
}

fn go_outcome(go: &str) -> i32 {
    match go {
        "A X" => return 3,
        "A Y" => return 6,
        "A Z" => return 0,
        "B X" => return 0,
        "B Y" => return 3,
        "B Z" => return 6,
        "C X" => return 6,
        "C Y" => return 0,
        "C Z" => return 3,
        _ => println!("not a real go"),
    }
    return 0;
}