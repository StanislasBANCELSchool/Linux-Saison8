# Linux-Saison8

[Scrapper.sh]
curl command to get the source code of coingecko 

grep -Po to find the price using the regex ^$[\d,]+.\d{2}$

then storing the data in price.txt

[getPrice.py]

opening price.txt

from this file storing the data in variables (highest price, lowest and actual)

displaying with dash the actual price + time stemp 

line graph showing the 3 prices (highest price, lowest and actual)

[fileClear.py]

clear the price.txt file

============================================================================================

[USAGE]

chmod +x scrapper.sh
./scrapper.sh

python3 getPrice.py
python3 fileClear.py

run localhost:8050 on your web Browser