from discord.ext import commands

class voiceChannelJoin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("voiceChannelJoin initialized")

def setup(bot):
    bot.add_cog(voiceChannelJoin(bot))