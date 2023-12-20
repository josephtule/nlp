#![allow(unused_variables, dead_code)]

fn main() {
    let mut x = 1.;
    let mut xm1 = 2. * x;
    let mut err = 10.;
    let mut xp1;
    while err > 1e-5 {
        xp1 = x - secant(c(x), c(xm1), x, xm1) * c(x);
        err = (xp1 - x).abs();

        xm1 = x;
        x = xp1;
    }
    println!("{}", x)
}

fn c(x: f64) -> f64 {
    2. * x * x + 2. * x - 1.
}

fn secant(c: f64, cp: f64, x: f64, xp: f64) -> f64 {
    (x - xp) / (c - cp)
}
