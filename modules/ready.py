from discord.ext import commands

class ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("ready initialized")

def setup(bot):
    bot.add_cog(ready(bot))