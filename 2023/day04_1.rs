use std::fs;

fn main () {
    let input = fs::read_to_string("day04.txt").expect("Should be able to read file");
    // println!("With text:\n{input}");

    let mut output: u32 = 0;

    for card in input.split('\n') {
        let nums = card.split(':').nth(1).unwrap();

        let mut nums_iter = nums.split('|');
        let winning_nums_str = nums_iter.next().unwrap().trim();
        let my_nums_str = nums_iter.next().unwrap().trim();

        let mut winning_nums: Vec<u32> = Vec::new();
        for winning_num in winning_nums_str.split_whitespace() {
            let num0: u32 = winning_num.parse().unwrap();
            winning_nums.push(num0);
        }

        let mut exp: u32 = 0;
        for my_num in my_nums_str.split_whitespace() {
            let num1: u32 = my_num.parse().unwrap();
            if winning_nums.contains(&num1) {
                exp += 1;
            }
        }

        if exp > 0 {
            output += 2_u32.pow(exp - 1);
        }        
    }

    println!("{output}");
}
