from discord.ext import commands

class guildDelete(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("guildDelete initialized")

def setup(bot):
    bot.add_cog(guildDelete(bot))