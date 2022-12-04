use std::collections::HashSet;

fn main() {
    let my_str = include_str!("4.in");

    //part 1
    let data = my_str.split("\n");
    let mut contain_count = 0; 
    for entry in data {
        let elves: Vec<&str> = entry.split(",").collect();
        let elf1: Vec<i8> = elves[0].split("-").map(|s| s.parse().expect("parse error")).collect();
        let elf2: Vec<i8> = elves[1].split("-").map(|s| s.parse().expect("parse error")).collect();
        if elf_contains(elf1, elf2) { 
            contain_count+=1;
        }
    }
    println!("Part 1: {contain_count}");


    //part 2
    let data = my_str.split("\n");
    let mut overlap_count = 0; 
    for entry in data {
        let elves: Vec<&str> = entry.split(",").collect();
        let elf1: Vec<i8> = elves[0].split("-").map(|s| s.parse().expect("parse error")).collect();
        let elf2: Vec<i8> = elves[1].split("-").map(|s| s.parse().expect("parse error")).collect();
        if elves_overlap(elf1,elf2) {
            overlap_count+=1;
        }
    }
    println!("Part 2: {overlap_count}");
}

fn elf_contains(elf1: Vec<i8>, elf2: Vec<i8>) -> bool {
    if elf1[0] <= elf2[0] && elf1[1] >= elf2[1] {
        return true;
    } else if elf2[0] <= elf1[0] && elf2[1] >= elf1[1] {
        return true;
    } else {
        return false;
    }
}

fn elves_overlap(elf1: Vec<i8>, elf2: Vec<i8>) -> bool {
    let elf1range: HashSet<i8> = (elf1[0]..=elf1[1]).collect();
    let elf2range: HashSet<i8> = (elf2[0]..=elf2[1]).collect();
    if elf1range.contains(&elf2[0]) || elf1range.contains(&elf2[1]) {
        return true;
    } else if elf2range.contains(&elf1[0]) || elf2range.contains(&elf1[1]) {
        return true;
    } else {
        return false;
    }
}
