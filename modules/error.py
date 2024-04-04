from discord.ext import commands

class error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("error initialized")

def setup(bot):
    bot.add_cog(error(bot))