#[derive(Debug)]
struct Monkey {
    items:Vec<usize>, 
    operation:String,
    opval:String,
    divisor: usize,
    iftrue: usize,
    iffalse: usize,
  }

fn main() {
    let my_str = include_str!("11.in");
    let data = my_str.split("\n\n");
    let mut monkeys:Vec<Monkey> = Vec::new();
    let mut monkitemcounts:Vec<usize> = Vec::new();
    
    //create monkeys
    for entry in data {
        let mymonkey: Vec<&str> = entry.split("\n").collect();
        let myline: Vec<&str> = mymonkey[1].split(|c| c== ',' || c==' ').collect();
        //dbg!(myline);
        let mut items:Vec<usize> = Vec::new();
        for i in 4..myline.len() {
            if i%2 == 0 {
                items.push(myline[i].parse::<usize>().unwrap());
            }
        }
        let myline: Vec<&str> = mymonkey[2].split_whitespace().collect();
        let operation = myline[4].to_string();
        let opval = myline[5].to_string();
        let myline: Vec<&str> = mymonkey[3].split_whitespace().collect();
        let divisor = myline[3];
        let myline: Vec<&str> = mymonkey[4].split_whitespace().collect();
        let iftrue = myline[5];
        let myline: Vec<&str> = mymonkey[5].split_whitespace().collect();
        let iffalse = myline[5];
        let mut tempmonkey = Monkey {
            items: items,
            operation: operation,
            opval: opval,
            divisor: divisor.parse::<usize>().unwrap(),
            iftrue: iftrue.parse::<usize>().unwrap(),
            iffalse: iffalse.parse::<usize>().unwrap(),
        };
        //tempmonkey.items.push(10);
        monkeys.push(tempmonkey);
    }

    //dbg!(monkeys);
    let mut modprod = 1;
    for x in 0..monkeys.len() {
        monkitemcounts.push(0);
        modprod *= monkeys[x].divisor;
    }

    //// part 1
    for _round in 0..10000 {
        for y in 0..monkeys.len() {
            monkitemcounts[y]+= monkeys[y].items.len();
            println!("Monkay {}:", y);
            for _x in 0..monkeys[y].items.len() {
                let mut worry:usize = monkeys[y].items.remove(0);
                println!("  Monkey inspects item worry {worry}");
                let mut realopvalue = 0;
                if monkeys[y].opval == "old".to_string() {
                    realopvalue = worry;
                } else {
                    realopvalue = monkeys[y].opval.parse::<usize>().unwrap();
                }
                worry = match monkeys[y].operation.as_str() {
                    "*" => worry * realopvalue,
                    "+" => worry + realopvalue,
                    // "-" => worry - realopvalue,
                    // "/" => (worry as f32 / realopvalue as f32) as usize,
                    _ => worry,
                };
                println!(" .   worry now {worry}");
                //worry = (worry as f64/3.0).floor() as usize;
                worry = (worry%modprod);
                println!(" .   worry cut to {worry}");
                let mut newmonkey = 0;
                let mut newdivisor:usize = monkeys[y].divisor;
                let worrycheck = worry%newdivisor;
                println!(" .   worry check = {} ({} % {})",worrycheck, worry, newdivisor);
                if worrycheck == 0 {
                    println!(" .   throwing to monkey {}", monkeys[y].iftrue);
                    newmonkey = monkeys[y].iftrue;
                } else {
                    println!(" .   throwing to monkey {}", monkeys[y].iffalse);
                    newmonkey = monkeys[y].iffalse;

                } 
                monkeys[newmonkey].items.push(worry);
            }
        }
        for y in 0..monkeys.len() {
            println!("Monkey {}:",y);
            let monkitems = "";
            for x in 0..monkeys[y].items.len() {
                println!("item {}", monkeys[y].items[x]);
            }
        }
    }

    monkitemcounts.sort();
    monkitemcounts.reverse();
    for x in 0.. monkeys.len() {
        println!("Monkey {}: {} items", x, monkitemcounts[x]);
    }
    println!("monkey business: {}", monkitemcounts[0] * monkitemcounts[1]);

}
