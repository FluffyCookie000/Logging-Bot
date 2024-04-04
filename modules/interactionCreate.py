from discord.ext import commands

class interactionCreate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("interactionCreate initialized")

def setup(bot):
    bot.add_cog(interactionCreate(bot))