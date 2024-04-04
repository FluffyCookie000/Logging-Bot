from discord.ext import commands

class guildRoleCreate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("guildRoleCreate initialized")

def setup(bot):
    bot.add_cog(guildRoleCreate(bot))