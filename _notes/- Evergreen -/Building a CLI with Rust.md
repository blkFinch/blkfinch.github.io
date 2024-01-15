---
title: Building a CLI with Rust
date: 2023-09-25
tags: []
aliases: []
feed: hide
---
tag: [[Programming]]

## How to Build Rust
- add dependencies to `Cargo.toml`
ex:
```
[package]
name = "crypto_cli"
version = "0.1.0"
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
tokio = { version = "1.15", features = ["full"] }
reqwest = { version = "0.11", features = ["json"] }
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"
```
- run `cargo run` to install dependecies
- build with `rustc path/to/main.rs`
- run the compiled file `./main` 
