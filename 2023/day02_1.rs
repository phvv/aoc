use std::fs;

fn round (r: &str) -> bool {
    let max_red = 12;
    let max_green = 13;
    let max_blue = 14;

    let mut valid = true;

    for part in r.split(", ") {
        let mut iter = part.split_whitespace();
        let count: u8 = iter.next().unwrap().parse().unwrap();
        let color = iter.next().unwrap();

        match color {
            "red" if count > max_red => valid = false,
            "green" if count > max_green => valid = false,
            "blue" if count > max_blue => valid = false,
            _ => {}
        }
    }

    valid
}

fn game (g: &str) -> u32 {
    let game_num: u32 = g.split(":").nth(0).unwrap().split(" ").nth(1).unwrap().parse().unwrap();

    for rounds in g.split(": ").nth(1).unwrap().split("; ") {
        if !round(rounds) {
            return 0;
        }
    }

    game_num
}

fn main () {
    let input = fs::read_to_string("day02.txt").expect("Should be able to read file");
    // println!("With text:\n{input}");

    let mut output: u32 = 0;
    
    for game_line in input.split("\n") {
        output += game(game_line);
    }

    println!{"{output}"};
}
