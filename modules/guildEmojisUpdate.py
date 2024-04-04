from discord.ext import commands

class guildEmojisUpdate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("guildEmojisUpdate initialized")

def setup(bot):
    bot.add_cog(guildEmojisUpdate(bot))