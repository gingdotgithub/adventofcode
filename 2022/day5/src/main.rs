fn main() {
    let my_str = include_str!("5.in");
    let data = my_str.split("\n");
    let mut stacks: Vec<Vec<char>> = Vec::new();
    let mut num_stacks: usize = 0;
    let mut stacks_built = false;
    for entry in data {
        
        // create a vector of vectors
        if num_stacks == 0 {
            num_stacks = ((1.0+dbg!(entry.len() as f32))/4.0).ceil() as usize;
            dbg!(num_stacks);
            for _i in 0..num_stacks {
                let stack = Vec::new();
                stacks.push(stack);
            } 
        }
        // switch mode between stack building and crate moving
        if entry == "" {
            stacks_built = true;
            for i in 0..stacks.len() {
                stacks[i].reverse();
            }
            continue;
        }

        
        if !stacks_built {
            // build stacks
            for i in 0..num_stacks {
                let new_crate = entry.chars().nth((i*4)+1).unwrap();
                if new_crate.is_alphabetic(){
                    stacks[i].push(new_crate);
                }
            }
        } else {
            // move crates
            let move_action: Vec<String> = entry.split(" ").map(|s| s.to_string()).collect();
            // part 1
            // for _i in 0..dbg!(move_action[1].parse().unwrap()) {
                
                // let stack_to_move: char = stacks[move_action[3].parse::<usize>().unwrap()-1].pop().unwrap();
                // dbg!(stack_to_move);
                // stacks[move_action[5].parse::<usize>().unwrap()-1].push(stack_to_move);
            // }

            //part 2
            let movecount = move_action[1].parse::<usize>().unwrap();
            let source =  move_action[3].parse::<usize>().unwrap()-1;
            let destination = move_action[5].parse::<usize>().unwrap()-1;
            let mut crane_lift: Vec<char> = Vec::new();
            for _i in 0..movecount {
                crane_lift.push(stacks[source].pop().unwrap());
            }
            crane_lift.reverse();
            stacks[destination].append(&mut crane_lift);
        }
    }


    let mut outcome = "".to_string();
    for i in 0..stacks.len() {
        outcome.push(stacks[i].pop().unwrap());
    }

    dbg!(stacks);
    println!("Part 1: {outcome}");
    
}
