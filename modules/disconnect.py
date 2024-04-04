from discord.ext import commands

class disconnect(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("disconnect initialized")

def setup(bot):
    bot.add_cog(disconnect(bot))