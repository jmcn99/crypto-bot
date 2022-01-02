from dotenv import load_dotenv
import os
import platform

import disnake
from disnake.ext import commands



#loading dotenv values
load_dotenv()

token = os.getenv('KEY')

#Setup bot
intents = disnake.Intents.default()
bot = commands.Bot(command_prefix="!", description="test", intents=intents, test_guilds=[842134671181479998])


#On ready:
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    print(f"Discord.py API version: {disnake.__version__}")
    print(f"Python version: {platform.python_version()}")
    print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    print("-------------------")

#load cogs
if __name__ == "__main__":
    print("Loading extensions...")
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cogs.{extension}")
                print(f"Loaded extension '{extension}")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension: {extension}\n{exception}")


#Run 

bot.run(token)