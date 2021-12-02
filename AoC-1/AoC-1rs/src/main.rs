use std::env;
use std::fs;
use std::{
    fs::File,
    io::{prelude::*, BufReader},
    path::Path,
};

fn lines_from_file(filename: impl AsRef<Path>) -> Vec<String> {
    let file = File::open(filename).expect("no such file");
    let buf = BufReader::new(file);
    buf.lines()
        .map(|l| l.expect("Could not parse line"))
        .collect()
}
fn main() {
    let lines = lines_from_file("../../input1.txt");
    let mut prevline = 0;
    let mut counter = 0;
    for line in lines {
        if prevline < line.parse::<i32>().unwrap() && prevline != 0{
            counter+=1;
        }
        prevline = line.parse::<i32>().unwrap();
    }
    println!("{}", counter);
}
