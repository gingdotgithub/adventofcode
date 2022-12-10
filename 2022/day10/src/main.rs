fn main() {
    let my_str = include_str!("10.in");
    let data = my_str.lines();
    let mut sum_signal = 0;
    let mut cycle:i32 = 1;
    let mut x:i32 = 1;
    let mut skip = false;
    let mut pixels: String = "".to_string();
    for entry in data {
        // Part 1 stuff
        if !skip && ((cycle+1+20)%40 == 0 || (cycle+20)%40 == 0) {
            println!("cycle {}, x = {}", cycle, x);
            if cycle%10 == 0 {
                sum_signal += x * cycle;
            } else {
                sum_signal += x * (cycle+1);
            }
            skip = true;
        } else {
            skip = false;
        }

        // Always does Part 2 before Part 1, since instructions only affect after.
        if entry == "noop" {
            if (cycle-1)%40 == x-1 || (cycle-1)%40 == x || (cycle-1)%40 == x+1 {
                pixels.push_str("#");
            } else {
                pixels.push_str(".");
            }
            //part 2 done, now part 1 for noop.
            cycle+=1;
        } else {
            let mut pixel = "".to_string();
            //probably should have made this a function, but does -1 first then n because
            //pixels were base 1. 
            if (cycle-1)%40 == x-1 || (cycle-1)%40 == x || (cycle-1)%40 == x+1 {
                pixels.push_str("#");
            } else {
                pixels.push_str(".");
            }
            if cycle%40 == x-1 || cycle%40 == x || cycle%40 == x+1 {
                pixels.push_str("#");
            } else {
                pixels.push_str(".");
            }
            //part 2 done, now part 1 for addx
            let value: Vec<&str> = entry.split_whitespace().collect();
            let value:i32 = value[1].parse().unwrap();
            //dbg!(value);
            x+=value;
            cycle+=2;
        }
    }
    println!("part 1: {}", sum_signal);
    println!("{}",pixels.chars().take(40).collect::<String>());
    println!("{}",pixels.chars().skip(40).take(40).collect::<String>());
    println!("{}",pixels.chars().skip(80).take(40).collect::<String>());
    println!("{}",pixels.chars().skip(120).take(40).collect::<String>());
    println!("{}",pixels.chars().skip(160).take(40).collect::<String>());
    println!("{}",pixels.chars().skip(200).take(40).collect::<String>());
}
