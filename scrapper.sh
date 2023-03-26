#!/bin/bash

# Clear the data
/usr/bin/python3 /home/ubuntu/Linux-Saison8/fileClear.py

# Fetch the web page HTML
html=$(curl -s https://www.coingecko.com/en/coins/bitcoin)

# Extract the Bitcoin price using regular expressions
price=$(echo "$html" | grep -Po '^\$[\d,]+\.\d{2}$')

# Get the current time in a human-readable format
time=$(date +"%Y-%m-%d %H:%M:%S")

# Print the result with the current time
echo "$time Bitcoin price: $price"

# Save the result to a file
echo "$time Bitcoin price: $price" >> price.txt

#Kill all the processus
sudo fuser -k 8050/tcp

#update the python code 
/usr/bin/python3 /home/ubuntu/Linux-Saison8/getPrice.py
