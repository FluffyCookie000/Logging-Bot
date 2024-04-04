from discord.ext import commands

class shardPreReady(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("shardPreReady initialized")

def setup(bot):
    bot.add_cog(shardPreReady(bot))