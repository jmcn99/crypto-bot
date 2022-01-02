import disnake
from disnake.ext import commands
from disnake.ext.commands import bot
from modules.coingecko import CoinGecko

class PriceCheck(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot: commands.Bot = bot
        self.cg = CoinGecko()

    @commands.slash_command(description="Displays the Current Price of a Coin")
    async def price(self, inter, coin):
        try:
            self.data = self.cg.getPrice(coin, "usd")
            self.name = list(self.data.keys())
            self.value = list(self.data.values())[0]["usd"]
            await inter.response.send_message(f"The price of {self.name[0]} is currently ${self.value}.")
        except:
            await inter.response.send_message(f"Sorry, I can't recognize that coin name. Make sure you use the name and not the ticker.",ephemeral = True)

    @commands.slash_command(description="Retrieves data about specified coin")
    async def data(self, inter, coin):
        try:
            self.data = self.cg.getData(coin)
            self.name = list(self.data.keys())
            self.value = self.data[coin]["usd"]
            self.market_cap = self.data[coin]["usd_market_cap"]
            self.hr_vol = self.data[coin]['usd_24h_vol']
            self.hr_change = self.data[coin]['usd_24h_change']
            self.updated_at = self.data[coin]['last_updated_at']

            embed=disnake.Embed(title='Price Data', description='Bitcoin', color=0xd357fe)
            embed.add_field(name='Current Price', value=f"${self.value:,}", inline=True)
            embed.add_field(name='Current Market Cap', value=f"${self.market_cap:,}", inline=True)
            embed.add_field(name='24 Hour Volume', value=f"${self.hr_vol:,}", inline=True)
            embed.add_field(name='24 Hour Change', value=f"{self.hr_change:.2f}%", inline=True)
            await inter.send(embed=embed)
        except:
            await inter.response.send_message(f"Sorry, I can't recognize that coin name. Make sure you use the name and not the ticker.",ephemeral = True)


def setup(bot):
    bot.add_cog(PriceCheck(bot))
