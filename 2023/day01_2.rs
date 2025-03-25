use std::fs;

fn main () {
    let input = fs::read_to_string("day01_1.txt").expect("Should be able to read file");
    let len = input.len();
    // println!("With text:\n{input}");
    // println!("{len}");

    let mut output = 0;
    let mut first_dig = 10;
    let mut last_dig = 10;
    
    for (idx, val) in input.chars().enumerate() {
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
        } else if (idx+3 < len) && (input[idx..idx+3] == *"one") {
            if first_dig == 10 {
                first_dig = 1;
                last_dig = 1;
            } else {
                last_dig = 1;
            }
        } else if (idx+3 < len) && (input[idx..idx+3] == *"two") {
            if first_dig == 10 {
                first_dig = 2;
                last_dig = 2;
            } else {
                last_dig = 2;
            }
        } else if (idx+5 < len) && (input[idx..idx+5] == *"three") {
            if first_dig == 10 {
                first_dig = 3;
                last_dig = 3;
            } else {
                last_dig = 3;
            }
        } else if (idx+4 < len) && (input[idx..idx+4] == *"four") {
            if first_dig == 10 {
                first_dig = 4;
                last_dig = 4;
            } else {
                last_dig = 4;
            }
        } else if (idx+4 < len) && (input[idx..idx+4] == *"five") {
            if first_dig == 10 {
                first_dig = 5;
                last_dig = 5;
            } else {
                last_dig = 5;
            }
        } else if (idx+3 < len) && (input[idx..idx+3] == *"six") {
            if first_dig == 10 {
                first_dig = 6;
                last_dig = 6;
            } else {
                last_dig = 6;
            }
        } else if (idx+5 < len) && (input[idx..idx+5] == *"seven") {
            if first_dig == 10 {
                first_dig = 7;
                last_dig = 7;
            } else {
                last_dig = 7;
            }
        } else if (idx+5 < len) && (input[idx..idx+5] == *"eight") {
            if first_dig == 10 {
                first_dig = 8;
                last_dig = 8;
            } else {
                last_dig = 8;
            }
        } else if (idx+4 < len) && (input[idx..idx+4] == *"nine") {
            if first_dig == 10 {
                first_dig = 9;
                last_dig = 9;
            } else {
                last_dig = 9;
            }
        }
    }

    println!("{output}");
}
