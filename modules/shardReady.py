from discord.ext import commands

class shardReady(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("shardReady initialized")

def setup(bot):
    bot.add_cog(shardReady(bot))