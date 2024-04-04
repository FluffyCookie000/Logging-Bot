from discord.ext import commands

class inviteCreate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("inviteCreate initialized")

def setup(bot):
    bot.add_cog(inviteCreate(bot))