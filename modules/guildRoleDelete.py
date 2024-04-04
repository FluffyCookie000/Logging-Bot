from discord.ext import commands

class guildRoleDelete(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("guildRoleDelete initialized")

def setup(bot):
    bot.add_cog(guildRoleDelete(bot))