fn main() {
    let mut elf_points = 0;
    let my_str = include_str!("2.in");
    
    // Part 1
    let data = my_str.split("\n");
    for entry in data {
        let go = go_score(entry.chars().last().unwrap());
        let result = go_outcome(entry);
        elf_points+= result + go;
    }
    println!("Part 1: {elf_points}");

    // Part 2
    elf_points = 0;
    let data = my_str.split("\n");
    for entry in data {
        let result = fix_outcome(entry.chars().next().unwrap(), entry.chars().last().unwrap());
        elf_points+= dbg!(result);
    }
    println!("Part 2: {elf_points}");

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

fn fix_outcome(go: char, ldw: char) -> i32 {
    let mut fix_score = 0;
    
    match ldw {
        'X' => {
            fix_score += 0;
            match go {
                'A' => fix_score += go_score('Z'),
                'B' => fix_score += go_score('X'),
                'C' => fix_score += go_score('Y'),
                _ => fix_score += 0,
            };
        },
        'Y' => {
            fix_score += 3;
            match go {
                'A' => fix_score += go_score('X'),
                'B' => fix_score += go_score('Y'),
                'C' => fix_score += go_score('Z'),
                _ => fix_score += 0,
            };
        },
        'Z' => {
            fix_score += 6;
            match go {
                'A' => fix_score += go_score('Y'),
                'B' => fix_score += go_score('Z'),
                'C' => fix_score += go_score('X'),
                _ => fix_score += 0,
            };
        },
        _ => return 0,
    }
    return fix_score;
}

