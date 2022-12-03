use std::collections::HashSet;


fn main() {
    let mut item_count = 0;
    let my_str = include_str!("3.in");
    let data = my_str.split("\n");
    let alphabet: Vec<char> = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".chars().collect();

    //part 1
    for entry in data {
        let (comp1, comp2) = entry.split_at(entry.len()/2);
        let comp1set: HashSet<char> = comp1.chars().collect();
        for c in comp2.chars() {
            if comp1set.contains(&c) {
                item_count += alphabet.iter().position(|&r| r == c).unwrap()+1;
                break;
            }
        }
    }
    println!("Part 1: {item_count}");

    //part 2
    let data = my_str.split("\n");
    let mut elf_count = 0;
    item_count = 0;
    let mut elf1_sack: HashSet<char> = "".chars().collect();
    let mut elf2_sack: HashSet<char> = "".chars().collect();
    for entry in data {
        if elf_count == 0 {
            elf1_sack = entry.chars().collect();
            elf_count+=1;
        } else  if elf_count == 1 {
            elf2_sack = entry.chars().collect();
            elf_count+=1;
        } else {
            elf_count = 0;
            for c in entry.chars() {
                if elf1_sack.contains(&c) && elf2_sack.contains(&c) {
                    item_count += alphabet.iter().position(|&r| r == c).unwrap()+1;
                    dbg!(c);
                    break;
                }
            }
        }
    }
    println!("Part 2: {item_count}");
    
}
