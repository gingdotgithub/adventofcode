fn main() {
    let my_str = include_str!("8.in");
    let data = my_str.lines();
    let mut forrest: Vec<Vec<u32>> = Vec::new();
    let mut x:usize = 0;
    let mut y:usize = 0;
    let mut visible_count:usize = 0; // part 1
    let mut best_view_score:usize = 0; //part 2
    for entry in data {
        let numbers: Vec<u32> = entry.chars().flat_map(|ch| ch.to_digit(10)).collect();
        forrest.push(numbers);
    }
    //dbg!(forrest);
    //println!("forest is {} by {}", forrest.len(), forrest[1].len());
    while y < forrest.len() {
        x = 0;
        while x < forrest[1].len() {
            let mut ndist:usize = 1; //part 2
            let mut edist:usize = 1; //part 2
            let mut sdist:usize = 1; //part 2
            let mut wdist:usize = 1; //part 2
            //check edge tree
            if x == 0 || y == 0 || x == forrest[0].len()-1 || y == forrest.len()-1 {
                visible_count+=1;
            } else {

                let mut noblock:bool = true;
                let mut found = false;
                //check north
                println!("checking north...");
                let mut j = y;
                while j > 0 {
                    j-=1;
                    if (forrest[j][x] >= forrest[y][x]) {
                        noblock = false;
                        break;
                    } else {        //part 2
                        ndist+=1;   //part 2
                    }               //part 2
                }
                if noblock {    //part 2
                    ndist-=1;  //part 2
                }               //part 2
                if noblock && !found {
                    visible_count+=1;
                    found = true;
                    println!("found one via north [{},{}]",x,y);
                }
                //check east
                noblock = true;
                println!("checking east...");
                let mut i = x;
                while i < forrest[0].len() -1 {
                    i+=1;
                    if (forrest[y][i] >= forrest[y][x]) {
                        noblock = false;
                        break;
                    } else {
                        edist+=1;
                    }
                }
                if noblock {
                    edist-=1;
                }
                if noblock && !found {
                    visible_count+=1;
                    found = true;
                    println!("found one via east [{},{}]",x,y);
                } 
                        
                //check south
                noblock = true;
                println!("checking south...");
                j = y;
                while j < forrest.len()-1 {
                    j+=1;
                    if forrest[j][x] >= forrest[y][x] {
                        noblock = false;
                        break;
                    } else {
                        sdist+=1;
                    }
                }
                if noblock {
                    sdist-=1;
                }
                if noblock && !found {
                    visible_count += 1;
                    found = true;
                    println!("found one via south [{},{}]",x,y);
                }

                //check west
                noblock = true;
                println!("checking west...");
                i = x;
                while i > 0 {
                    i-=1;
                    if (forrest[y][i] >= forrest[y][x]) {
                        noblock = false;
                        break;
                    } else {
                        wdist+=1;
                    }
                }
                if noblock {
                    wdist-=1;
                }
                if noblock && !found {
                    visible_count+=1;
                    found = true;
                    println!("found one via west [{},{}]",x,y);
                }
            }
            let newscore = ndist*edist*sdist*wdist;  //part 2
            if newscore > best_view_score {  //part 2
                best_view_score = newscore;  //part 2
                println!("new best score at position [{},{}] is n:{} e:{} s:{} w:{}", x, y, ndist, edist, sdist, wdist);
            }                               //part 2
            x+=1;
        }
        y+=1;
    }
    println!("part 1 - visible = {}", visible_count);
    println!("part 2 - best score = {}", best_view_score);  //part 2
}