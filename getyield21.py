"""!/usr/bin/env python3"""
import urllib
from bs4 import BeautifulSoup
#
#MMY4Nasdaq.com
# This program will scrape yield (and related) information from Nasdaq.com for money market funds. 
# (Because IEX returns None for dividendYield on money markets - https://github.com/iexg/IEX-API/issues/654)


def get_mm_yield(param1):
    """Function get's the yield of the money market fund (only) specified from Nasdaq.com

    Args:
        param1: symbol for look-up

    Returns:
        The return value. """
    symbol = param1
    baseurl = "https://www.nasdaq.com/symbol/"
    url = baseurl + symbol
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data_content = response.read()
    soup = BeautifulSoup(data_content, "html5lib")
    all_td = soup.find_all("td")


    asset_symbol = (all_td[3].text)
    asset_description = (all_td[4].text)
    asset_type = (all_td[5].text)
    asset_yield = (all_td[7].text)
    return asset_symbol, asset_description, asset_type, asset_yield

def main():
    """ Function executes main logic loop
    """
    symbol_list = ['swvxx', 'vmmxx', 'sprxx', 'mjlxx', 'vmfxx', 'VUSXX', 'VMVXX', \
     'IUSXX']
    for i in symbol_list:
        print(get_mm_yield(i))
if __name__ == '__main__':
    main()
