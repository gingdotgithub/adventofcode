use std::collections::HashSet;

fn main() {
    let my_str = include_str!("6.in");
    let data = my_str.split("\n");
    //part 1
    //let markersize = 4;
    //part 2
    let markersize = 14;
    for entry in data {
        println!("Marker location: {}", find_marker(entry.to_string(), markersize));
    }
}

fn find_marker(signal: String, markersize: usize) -> usize {
    for i in markersize..signal.len() {
        let buffer: HashSet<char> = HashSet::from_iter(signal[i-markersize..i].chars());
        if buffer.len() == markersize {
            return i;
        }
    }
    return signal.len();
}
