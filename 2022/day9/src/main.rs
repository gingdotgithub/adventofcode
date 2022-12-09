fn main() {
    let my_str = include_str!("9.in");
    let data = my_str.lines();
    let mut h: [i32; 2] = [0,0];
    let mut t: [i32; 2] = [0,0];
    let mut t_locations: Vec<[i32; 2]> = Vec::new();
    t_locations.push([0,0]);
    //dbg!(h);
    for entry in data {
        let entry: Vec<&str> = entry.split_whitespace().collect();
        //dbg![entry[2] as i32 - 0x30];
        for x in 0..(entry[1].parse().unwrap()) {
            match entry[0] {
                "R" => move_right(&mut h, &mut t, &mut t_locations),
                "U" => move_up(&mut h, &mut t, &mut t_locations),
                "L" => move_left(&mut h, &mut t, &mut t_locations),
                "D" => move_down(&mut h, &mut t, &mut t_locations),
                _ => continue,
            }
        }
    }
    //dbg!(t_locations);
    println!("Part 1: t has been in {} locations", t_locations.len());
}

fn move_right(h: &mut [i32; 2], t: &mut [i32; 2], t_locations: &mut Vec<[i32;2]>) {
    h[0]+=1;
    if (h[0]-t[0]).abs() == 2 {
        t[0]+=1;
        if h[1] != t[1] {
            t[1] = h[1];
        }
        if !t_locations.contains(t) {
            t_locations.push(*t);
        }
    }
    println!("move right [{},{}] - [{},{}], t has been to {} places", h[0],h[1],t[0],t[1], t_locations.len());
}

fn move_up(h: &mut [i32; 2], t: &mut [i32; 2], t_locations: &mut Vec<[i32;2]>) {
    h[1]+=1;
    if (h[1]-t[1]).abs() == 2 {
        t[1]+=1;
        if h[0] != t[0] {
            t[0] = h[0];
        }
        if !t_locations.contains(t) {
            t_locations.push(*t);
        }
    }
    println!("move up [{},{}] - [{},{}], t has been to {} places", h[0],h[1],t[0],t[1], t_locations.len());
}

fn move_left(h: &mut [i32; 2], t: &mut [i32; 2], t_locations: &mut Vec<[i32;2]>) {
    h[0]-=1;
    if (h[0]-t[0]).abs() == 2 {
        t[0]-=1;
        if h[1] != t[1] {
            t[1] = h[1];
        }
        if !t_locations.contains(t) {
            t_locations.push(*t);
        }
    }
    println!("move left [{},{}] - [{},{}], t has been to {} places", h[0],h[1],t[0],t[1], t_locations.len());
}

fn move_down(h: &mut [i32; 2], t: &mut [i32; 2], t_locations: &mut Vec<[i32;2]>) {
    h[1]-=1;
    if (h[1]-t[1]).abs() == 2 {
        t[1]-=1;
        if h[0] != t[0] {
            t[0] = h[0];
        }
        if !t_locations.contains(t) {
            t_locations.push(*t);
        }
    }
    println!("move down [{},{}] - [{},{}], t has been to {} places", h[0],h[1],t[0],t[1], t_locations.len());
}