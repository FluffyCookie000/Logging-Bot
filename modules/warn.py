from discord.ext import commands

class warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("warn initialized")

def setup(bot):
    bot.add_cog(warn(bot))