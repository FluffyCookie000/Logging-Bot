from discord.ext import commands

class inviteDelete(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("inviteDelete initialized")

def setup(bot):
    bot.add_cog(inviteDelete(bot))