from pycoingecko import CoinGeckoAPI

class CoinGecko():
    def __init__(self):
        self.cg = CoinGeckoAPI()
        
    def getPrice(self, coins, cur):
        return self.cg.get_price(ids=coins, vs_currencies=cur)




