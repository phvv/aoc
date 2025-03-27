use std::fs;

fn find_num (rc: usize, i: &str) -> (u32, usize) {
    let s = &i[rc..];

    let output_num_s: String = s.chars().take_while(|c| c.is_digit(10)).collect();
    let output_num: u32 = output_num_s.parse().unwrap();
    let output_size = output_num_s.len();

    (output_num, output_size)
}

fn valid_idx (r: usize, c: usize, total_r: usize, total_c: usize) -> bool {
    r < total_r && c < total_c
}

fn idxs (r: usize, c: usize, n: usize) -> Vec<(usize, usize)> {
    let mut output = vec![(r.wrapping_sub(1), c), (r.wrapping_sub(1), c.wrapping_sub(1)), (r, c.wrapping_sub(1)), (r+1, c.wrapping_sub(1)), (r+1, c)];

    for i in 1..n+1 {
        output.push((r.wrapping_sub(1), c+i));
        output.push((r+1, c+i));
    }

    output.push((r, c+n));

    output
}

fn is_symbol (r: usize, c: usize, total_c: usize, i: &str) -> bool {
    let rc = r * total_c + c;
    let val = i.chars().nth(rc).unwrap();

    if val.is_digit(10) || val == '.' || val == '\n' {
        return false;
    }

    true
}

fn main () {
    let input = fs::read_to_string("day03.txt").expect("Should be able to read file");
    // println!("With text:\n{input}");

    let mut output: u32 = 0;
    let total_r = input.lines().count();
    let total_c = input.lines().next().unwrap().len() + 1;

    let mut i: usize = 0;
    loop {
        let val = input.chars().nth(i).unwrap();
        
        if val.is_digit(10) {
            let mut add = false;

            let r = i / total_c;
            let c = i % total_c;

            let (num, num_size) = find_num(i, &input);
            let indexes = idxs(r, c, num_size);

            for (ri, ci) in indexes {
                if valid_idx(ri, ci, total_r, total_c) && is_symbol(ri, ci, total_c, &input) {
                    add = true;
                }
            }

            if add {
                output += num;
            }

            i += num_size - 1;
        }
        i += 1;

        if i >= (total_r * total_c - 1) {
            break;
        }
    }

    println!("{output}");
}
