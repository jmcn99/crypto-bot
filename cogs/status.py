from modules.coingecko import CoinGecko

import disnake
from disnake.ext import commands
from disnake.ext import tasks


class StatusChange(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.cg = CoinGecko()
        self.counter = 0

        self.update_status.start()

    @tasks.loop(seconds=10)
    async def update_status(self):
        #Update prices every loop
        self.prices = self.cg.getPrice(['bitcoin','ethereum','litecoin'], 'usd')
        #Set counter to 0 when it has looped thru all element in list
        if self.counter >= len(self.prices) - 1:
            self.counter = 0

        else:
            self.counter += 1
        self.names = list(self.prices.keys())
        self.values = list(self.prices.values())

        self.status = f"{self.names[self.counter]}: ${self.values[self.counter]['usd']}"

        await self.bot.change_presence(status=disnake.Status.online,activity=disnake.Game(self.status))


    @update_status.before_loop
    async def before_update_status(self):
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(StatusChange(bot))

