use std::{
    cmp::Ordering,
    collections::{BinaryHeap, HashMap, HashSet},
};

fn main() {
    let mut themap:Vec<Vec<char>> = Vec::new();
    let my_str = include_str!("12.in");
    let data = my_str.lines();
    let mut start:Vertex = Vertex::new(0,0);
    let mut end:Vertex = Vertex::new(0,0);
    let mut y = 0;
    let mut x = 0;
    for entry in data {
        let mut temprow:Vec<char> = entry.chars().collect();
        if temprow.contains(&'S') {
            x = temprow.iter().position(|&r| r == 'S').unwrap();
            start = Vertex::new(x,y);
            temprow[x] = 'a';
            //temprow = std::mem:replace(&mut temprow[x],'a');
        }
        if temprow.contains(&'E') {
            x = temprow.iter().position(|&r| r == 'E').unwrap();
            end = Vertex::new(x,y);
            temprow[x] = 'z';   
            //temprow = std::mem:replace(&mut temprow[x],'z');
        }
        themap.push(temprow);
        y+=1;
    }

    let mut vertices:Vec<Vertex> = Vec::new();
    let mut theas:Vec<Vertex> = Vec::new();
    let mut adjacency_list = HashMap::new();

    y=0;
    x=0;
    //println!("{:?}",themap.len());
    for y in 0..themap.len() {
        let mut temp: Vertex = Vertex::new(0,0);
        for x in 0..themap[0].len() {
            temp = Vertex::new(x,y);
            if themap[y][x] == 'a' {
                theas.push(temp);
            }
            vertices.push(temp);
            let mut neighbours:Vec<(Vertex, usize)> = Vec::new();
            if x > 0 {
                let cost = (themap[y][x-1] as i32) - (themap[y][x] as i32);
                if cost > -2 {
                    if !vertices.contains(&Vertex::new(x-1,y)) {
                        vertices.push(Vertex::new(x-1,y));
                    }
                    neighbours.push((Vertex::new(x-1,y), 1));
                }
            }
            if y > 0 {
                let cost = (themap[y-1][x] as i32) - (themap[y][x] as i32);
                if cost > -2 {
                    if !vertices.contains(&Vertex::new(x,y-1)) {
                        vertices.push(Vertex::new(x,y-1));
                    }
                    neighbours.push((Vertex::new(x,y-1), 1));
                }
            }
            if x < themap[0].len()-1 {
                let cost = (themap[y][x+1] as i32) - (themap[y][x] as i32);
                if cost > -2 {
                    if !vertices.contains(&Vertex::new(x+1,y)) {
                        vertices.push(Vertex::new(x+1,y));
                    }
                    neighbours.push((Vertex::new(x+1,y), 1));
                }
            }
            if y < themap.len()-1 {
                let cost = (themap[y+1][x] as i32) - (themap[y][x] as i32);
                if cost > -2 {
                    if !vertices.contains(&Vertex::new(x,y+1)) {
                        vertices.push(Vertex::new(x,y+1));
                    }
                    neighbours.push((Vertex::new(x,y+1), 1));
                }
            }
            adjacency_list.insert(temp,neighbours);
        }
    }
    // println!("{:?}",vertices);
    // println!("{:?}",adjacency_list);
    //println!("{:?}",adjacency_list.len());
    let mut bestdist = 10000;
    for v in theas {
        let distances = dijkstra(end, &adjacency_list);

        // for (v, d) in &distances {
        //     println!("name: [{},{}], distance: {}", v.myx, v.myy, d);
        // }
        println!("{:?}",start);
        println!("{:?}",end);
        println!("{:?}",distances.get(&v));
        if distances.contains_key(&v) && distances.get(&v).unwrap() < &bestdist {
            bestdist = *distances.get(&v).unwrap();
        }
    }
    println!("{bestdist}");
}


fn dijkstra(
    start: Vertex,
    adjacency_list: &HashMap<Vertex, Vec<(Vertex, usize)>>,
) -> HashMap<Vertex, usize> {
    let mut distances = HashMap::new();
    let mut visited = HashSet::new();
    let mut to_visit = BinaryHeap::new();

    distances.insert(start, 0);
    to_visit.push(Visit {
        vertex: start,
        distance: 0,
    });

    while let Some(Visit { vertex, distance }) = to_visit.pop() {
        if !visited.insert(vertex) {
            // Already visited this node
            continue;
        }

        if let Some(neighbors) = adjacency_list.get(&vertex) {
            for (neighbor, cost) in neighbors {
                let new_distance = distance + cost;
                let is_shorter = distances
                    .get(&neighbor)
                    .map_or(true, |&current| new_distance < current);

                if is_shorter {
                    distances.insert(*neighbor, new_distance);
                    to_visit.push(Visit {
                        vertex: *neighbor,
                        distance: new_distance,
                    });
                }
            }
        }
    }

    return distances;
}


//shamelessly stolen from https://codereview.stackexchange.com/questions/202677/dijkstras-algorithm-in-rust
#[derive(Debug, Copy, Clone, PartialEq, Eq, Hash)]
struct Vertex {
    myx: usize,
    myy: usize,
}

impl Vertex {
    fn new(x: usize, y: usize) -> Vertex {
        Vertex { myx: x, myy:y }
    }
}

#[derive(Debug)]
struct Visit<V> {
    vertex: V,
    distance: usize,
}

impl<V> Ord for Visit<V> {
    fn cmp(&self, other: &Self) -> Ordering {
        other.distance.cmp(&self.distance)
    }
}

impl<V> PartialOrd for Visit<V> {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl<V> PartialEq for Visit<V> {
    fn eq(&self, other: &Self) -> bool {
        self.distance.eq(&other.distance)
    }
}

impl<V> Eq for Visit<V> {}