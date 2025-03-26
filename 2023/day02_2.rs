use std::fs;

fn round (r: &str) -> (u32, u32, u32) {
    let mut red = 0;
    let mut green = 0;
    let mut blue = 0;

    for part in r.split(", ") {
        let mut iter = part.split_whitespace();
        let count: u32 = iter.next().unwrap().parse().unwrap();
        let color = iter.next().unwrap();

        match color {
            "red" => red = count,
            "green" => green = count,
            "blue" => blue = count,
            _ => {}
        }
    }

    (red, green, blue)
}

fn game (g: &str) -> u32 {
    let mut max_r: u32 = 0;
    let mut max_g: u32 = 0;
    let mut max_b: u32 = 0;

    for rounds in g.split(": ").nth(1).unwrap().split("; ") {
        let (r, g, b) = round(rounds);
        if r > max_r {
            max_r = r;
        }
        if g > max_g {
            max_g = g;
        }
        if b > max_b {
            max_b = b;
        }
    }

    max_r * max_g * max_b
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
