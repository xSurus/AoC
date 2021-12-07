use std::env;
use std::fs;
use std::{
    fs::File,
    io::{prelude::*, BufReader},
    path::Path,
};

fn main() {
    let reader = BufReader::new(File::open("../../input.txt").expect("Cannot open file.txt"));
    for line in reader.lines() {
        let con = line.unwrap().split(',');
        let mut group: [i32; 9];
        for i in con: 
        println!("good: {}",v[0]);
    }
    let mult: u64 = (horiz as u64) * (depth as u64);
    println!("{}",horiz * depth );
}
