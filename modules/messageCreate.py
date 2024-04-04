from discord.ext import commands

class messageCreate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("messageCreate initialized")

def setup(bot):
    bot.add_cog(messageCreate(bot))