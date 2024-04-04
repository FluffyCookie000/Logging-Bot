from discord.ext import commands

class voiceChannelSwitch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("voiceChannelSwitch initialized")

def setup(bot):
    bot.add_cog(voiceChannelSwitch(bot))