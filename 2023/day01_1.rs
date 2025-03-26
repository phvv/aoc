use std::fs;

fn main () {
    let input = fs::read_to_string("day01.txt").expect("Should be able to read file");
    // let len = input.len();
    // println!("With text:\n{input}");
    // println!("{len}");

    let mut output = 0;
    let mut first_dig = 10;
    let mut last_dig = 10;
    
    for val in input.chars() {
        if val == '\n' {
            output += 10 * first_dig + last_dig;
            first_dig = 10;
            last_dig = 10;
        } else if val.is_digit(10) {
            let num = val.to_digit(10).unwrap() as u32;
            if first_dig == 10 {
                first_dig = num;
                last_dig = num;
            } else {
                last_dig = num;
            }
        }
    }

    println!("{output}");
}
