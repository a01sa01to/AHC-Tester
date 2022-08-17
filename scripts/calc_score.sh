# Write Script to calculate score
# Runs in tools directory
cargo run --release --bin vis in/$1.txt out/$1.txt > res/$1.txt
cat res/$1.txt
