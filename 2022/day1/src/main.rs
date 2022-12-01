fn main() {
    let my_str = include_str!("1.in");
    let data = my_str.split("\n");
    let mut elfsum: u32 = 0;
    //let mut topelf: u32 = 0;
    let mut elvescals = Vec::new();
    for entry in data {
        if entry == "" {
            // if dbg!(elfsum > topelf) {
            //     topelf = elfsum;
            // }
            elvescals.push(elfsum);
            elfsum = 0;
        } else {
            let entry: u32 = entry.parse().unwrap();
            elfsum+=entry;
        }
        
    }
    elvescals.sort();
    elvescals.reverse();
    println!("{}",elvescals[0]+elvescals[1]+elvescals[2]);
}
