from pycoingecko import CoinGeckoAPI

class CoinGecko():
    def __init__(self):
        self.cg = CoinGeckoAPI()
        
    def getPrice(self, coins, cur):
        return self.cg.get_price(ids=coins, vs_currencies=cur)
    
    def getData(self, coin):
        return self.cg.get_price(ids=coin, vs_currencies='usd', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')
