from discord.ext import commands

class voiceChannelLeave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("voiceChannelLeave initialized")

def setup(bot):
    bot.add_cog(voiceChannelLeave(bot))