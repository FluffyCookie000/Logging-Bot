from discord.ext import commands

class voiceStateUpdate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("voiceStateUpdate initialized")

def setup(bot):
    bot.add_cog(voiceStateUpdate(bot))