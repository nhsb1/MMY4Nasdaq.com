# MMY4Nasdaq.com
Scrapes yield information from nasdaq.com for money market funds
(Because IEX returns None for dividendYield on money markets - something like https://github.com/iexg/IEX-API/issues/654)

Install
-------

    Download getyield21.py, replace symbols in the symbol_list with money market funds that you care about. 

Usage
-----

    python3 getyield21.py

Requirements
-----
Python3, urllib, bs4
