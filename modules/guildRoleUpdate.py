from discord.ext import commands

class guildRoleUpdate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("guildRoleUpdate initialized")

def setup(bot):
    bot.add_cog(guildRoleUpdate(bot))