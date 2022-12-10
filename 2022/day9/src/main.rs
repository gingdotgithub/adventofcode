const ropelen: usize = 9;

fn main() {
    let my_str = include_str!("9.in");
    let data = my_str.lines();
    //let mut h: [i32; 2] = [0,0];
    //let mut t: [i32; 2] = [0,0];
    let mut ropes: [[i32;2];ropelen+1] = [[0,0]; ropelen+1];
    let mut t_locations: Vec<[i32; 2]> = Vec::new();
    t_locations.push([0,0]);
    //dbg!(h);
    for entry in data {
        let entry: Vec<&str> = entry.split_whitespace().collect();
        //dbg![entry[2] as i32 - 0x30];
        for x in 0..(entry[1].parse().unwrap()) {
            match entry[0] {
                "R" => move_right2(&mut ropes, 0, &mut t_locations),
                "U" => move_up2(&mut ropes, 0, &mut t_locations),
                "L" => move_left2(&mut ropes, 0, &mut t_locations),
                "D" => move_down2(&mut ropes, 0, &mut t_locations),
                _ => continue,
            }
        }
    }
    //dbg!(t_locations);
    println!("Part 1: t has been in {} locations", t_locations.len());
    //dbg!(t_locations);
}

// fn move_right(h: &mut [i32; 2], t: &mut [i32; 2], t_locations: &mut Vec<[i32;2]>) {
//     h[0]+=1;
//     if (h[0]-t[0]).abs() == 2 {
//         t[0]+=1;
//         if h[1] != t[1] {
//             t[1] = h[1];
//         }
//         if !t_locations.contains(t) {
//             t_locations.push(*t);
//         }
//     }
//     println!("move right [{},{}] - [{},{}], t has been to {} places", h[0],h[1],t[0],t[1], t_locations.len());
// }

// fn move_up(h: &mut [i32; 2], t: &mut [i32; 2], t_locations: &mut Vec<[i32;2]>) {
//     h[1]+=1;
//     if (h[1]-t[1]).abs() == 2 {
//         t[1]+=1;
//         if h[0] != t[0] {
//             t[0] = h[0];
//         }
//         if !t_locations.contains(t) {
//             t_locations.push(*t);
//         }
//     }
//     println!("move up [{},{}] - [{},{}], t has been to {} places", h[0],h[1],t[0],t[1], t_locations.len());
// }

// fn move_left(h: &mut [i32; 2], t: &mut [i32; 2], t_locations: &mut Vec<[i32;2]>) {
//     h[0]-=1;
//     if (h[0]-t[0]).abs() == 2 {
//         t[0]-=1;
//         if h[1] != t[1] {
//             t[1] = h[1];
//         }
//         if !t_locations.contains(t) {
//             t_locations.push(*t);
//         }
//     }
//     println!("move left [{},{}] - [{},{}], t has been to {} places", h[0],h[1],t[0],t[1], t_locations.len());
// }

// fn move_down(h: &mut [i32; 2], t: &mut [i32; 2], t_locations: &mut Vec<[i32;2]>) {
//     h[1]-=1;
//     if (h[1]-t[1]).abs() == 2 {
//         t[1]-=1;
//         if h[0] != t[0] {
//             t[0] = h[0];
//         }
//         if !t_locations.contains(t) {
//             t_locations.push(*t);
//         }
//     }
//     println!("move down [{},{}] - [{},{}], t has been to {} places", h[0],h[1],t[0],t[1], t_locations.len());
// }
////////


fn move_right2(ropes: &mut [[i32; 2];ropelen+1], d:usize, t_locations: &mut Vec<[i32;2]>) {
    ropes[d][0]+=1;
    println!("{} move right [{},{}]", d, ropes[d][0],ropes[d][1]);
    if d != ropelen && ((ropes[d][0]-ropes[d+1][0]).abs() == 2 || (ropes[d][1]-ropes[d+1][1]).abs() == 2) {
        println!("moving {} right", d+1);
        if ropes[d][1] > ropes[d+1][1] {
            //t[1] = h[1];
            println!("moving {} up to match", d+1);
            ropes[d+1][0]+=1;
            move_up2(ropes, d+1, t_locations);
        } else if ropes[d][1] < ropes[d+1][1] {
            println!("moving {} down to match", d+1);
            ropes[d+1][0]+=1;
            move_down2(ropes, d+1, t_locations);
        } else {
            move_right2(ropes,d+1, t_locations);
        }
        if d+1==ropelen && !t_locations.contains(&ropes[d+1]) {
            t_locations.push(ropes[d+1]);
            println!("tail moved to a new location: [{},{}].  t has been to {} places", ropes[d+1][0], ropes[d+1][1], t_locations.len());
        }
    }
    
}

fn move_up2(ropes: &mut [[i32; 2];ropelen+1], d:usize, t_locations: &mut Vec<[i32;2]>) {
    ropes[d][1]+=1;
    println!("{} move up [{},{}].", d, ropes[d][0],ropes[d][1]);
    if  d != ropelen && ((ropes[d][1]-ropes[d+1][1]).abs() == 2 || (ropes[d][0]-ropes[d+1][0]).abs() == 2) {
        println!("moving {} up", d+1);
        if ropes[d][0] > ropes[d+1][0] {
            //t[0] = h[0];
            println!("moving {} right to match", d+1);
            ropes[d+1][1]+=1;
            move_right2(ropes, d+1, t_locations);
        } else if ropes[d][0] < ropes[d+1][0] {
            //t[0] = h[0];
            println!("moving {} left to match", d+1);
            ropes[d+1][1]+=1;
            move_left2(ropes, d+1, t_locations);
        } else {
            move_up2(ropes,d+1, t_locations);
        }
        if d+1==ropelen && !t_locations.contains(&ropes[d+1]) {
            t_locations.push(ropes[d+1]);
            println!("tail moved to a new location: [{},{}].  t has been to {} places", ropes[d+1][0], ropes[d+1][1], t_locations.len());
        }
    }
    //println!("{} move up [{},{}], t has been to {} places", d, ropes[d][0],ropes[d][1], t_locations.len());
}

fn move_left2(ropes: &mut [[i32; 2];ropelen+1], d:usize, t_locations: &mut Vec<[i32;2]>) {
    ropes[d][0]-=1;
    println!("{} move left [{},{}].", d, ropes[d][0],ropes[d][1]);
    if  d != ropelen && ((ropes[d][0]-ropes[d+1][0]).abs() == 2 || (ropes[d][1]-ropes[d+1][1]).abs() == 2) {
        println!("moving {} left", d+1);
        if ropes[d][1] > ropes[d+1][1] {
            //t[1] = h[1];
            println!("moving {} up to match", d+1);
            ropes[d+1][0]-=1;
            move_up2(ropes, d+1, t_locations);
        } else if ropes[d][1] < ropes[d+1][1] {
            println!("moving {} down to match", d+1);
            ropes[d+1][0]-=1;
            move_down2(ropes, d+1, t_locations);
        } else {
            move_left2(ropes,d+1, t_locations);
        }
        if d+1==ropelen && !t_locations.contains(&ropes[d+1]) {
            t_locations.push(ropes[d+1]);
            println!("tail moved to a new location: [{},{}].  t has been to {} places", ropes[d+1][0], ropes[d+1][1], t_locations.len());
        }
    }
    //println!("{} move left [{},{}], t has been to {} places", d, ropes[d][0],ropes[d][1], t_locations.len());
}

fn move_down2(ropes: &mut [[i32; 2];ropelen+1], d:usize, t_locations: &mut Vec<[i32;2]>) {
    ropes[d][1]-=1;
    println!("{} move down [{},{}]", d, ropes[d][0],ropes[d][1]);
    if  d != ropelen && ((ropes[d][1]-ropes[d+1][1]).abs() == 2 || (ropes[d][0]-ropes[d+1][0]).abs() == 2) {
        println!("moving {} down", d+1);
        
        if ropes[d][0] > ropes[d+1][0] {
            //t[0] = h[0];
            println!("moving {} right to match", d+1);
            ropes[d+1][1]-=1;
            move_right2(ropes, d+1, t_locations);
        } else if ropes[d][0] < ropes[d+1][0] {
            //t[0] = h[0];
            println!("moving {} left to match", d+1);
            ropes[d+1][1]-=1;
            move_left2(ropes, d+1, t_locations);
        } else {
            move_down2(ropes,d+1, t_locations);
        }
        if d+1==ropelen && !t_locations.contains(&ropes[d+1]) {
            t_locations.push(ropes[d+1]);
            println!("tail moved to a new location: [{},{}].  t has been to {} places", ropes[d+1][0], ropes[d+1][1], t_locations.len());
        }
    }
    //println!("{} move down [{},{}], t has been to {} places", d, ropes[d][0],ropes[d][1], t_locations.len());
}