from discord.ext import commands

class shardDisconnect(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("shardDisconnect initialized")

def setup(bot):
    bot.add_cog(shardDisconnect(bot))