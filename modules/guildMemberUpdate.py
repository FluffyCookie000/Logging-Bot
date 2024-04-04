from discord.ext import commands

class guildMemberUpdate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("guildMemberUpdate initialized")

def setup(bot):
    bot.add_cog(guildMemberUpdate(bot))