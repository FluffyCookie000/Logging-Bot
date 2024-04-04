from discord.ext import commands

class guildUpdate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("guildUpdate initialized")

def setup(bot):
    bot.add_cog(guildUpdate(bot))