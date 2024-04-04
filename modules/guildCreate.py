from discord.ext import commands

class guildCreate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("guildCreate initialized")

def setup(bot):
    bot.add_cog(guildCreate(bot))