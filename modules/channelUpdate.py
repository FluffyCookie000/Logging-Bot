from discord.ext import commands

class channelUpdate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("channelUpdate initialized")

def setup(bot):
    bot.add_cog(channelUpdate(bot))