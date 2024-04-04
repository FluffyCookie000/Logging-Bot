from discord.ext import commands

class debug(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("debug initialized")

def setup(bot):
    bot.add_cog(debug(bot))