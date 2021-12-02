use std::env;
use std::fs;
use std::{
    fs::File,
    io::{prelude::*, BufReader},
    path::Path,
};

fn main() {
    let mut depth = 0;
    let mut horiz = 0;
    let mut aim = 0;
    let reader = BufReader::new(File::open("../../input2.txt").expect("Cannot open file.txt"));
    for line in reader.lines() {
        let con =line.unwrap(); 
        let v: Vec<&str> = con.split(' ').collect();
        match v[0]{
            "forward" => {horiz += v[1].parse::<i32>().unwrap(); depth += v[1].parse::<i32>().unwrap() * aim}
            "up" => aim -= v[1].parse::<i32>().unwrap(),
            "down" => aim += v[1].parse::<i32>().unwrap(),
            _ => println!("{}",v[0]),
        }  
        println!("good: {}",v[0]);
    }
    let mult: u64 = (horiz as u64) * (depth as u64);
    println!("{}",horiz * depth );
}
