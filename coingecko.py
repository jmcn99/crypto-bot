from pycoingecko import CoinGeckoAPI

import os
from dotenv import load_dotenv

#init api
cg = CoinGeckoAPI()

print(cg.get_price(ids=['bitcoin','ethereum'], vs_currencies='cad'))
