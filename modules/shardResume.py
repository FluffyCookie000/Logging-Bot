from discord.ext import commands

class shardResume(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("shardResume initialized")

def setup(bot):
    bot.add_cog(shardResume(bot))