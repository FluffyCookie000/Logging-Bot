from datetime import datetime as DT
from discord.ext import commands

import calendar
import datetime
import discord
import time

class logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("logging initialized")

    @commands.command()
    async def test(self, ctx):
        string= str(ctx.author.created_at)
        element = DT.strptime(string[:-13],"%Y-%m-%d %H:%M:%S")
        b = DT.utcnow().timestamp()
        a = time.mktime(time.strptime(string[:-13], "%Y-%m-%d %H:%M:%S"))
        delta = b - a
        delta = int(delta / 86400)
        
        # timestamp = DT.timestamp(element)

        await ctx.send(f'{delta}')

    @commands.command()
    async def audit(self, ctx):
        entry = list(await ctx.channel.guild.audit_logs(limit=1).flatten())[0]
        await ctx.send(str(entry.after))


    @commands.command()
    async def userinfo(self,ctx, member: discord.Role = None):
        if not member:
            member = ctx.message.author
        perm_list = [perm[0] for perm in ctx.channel.overwrites_for(member) if perm[1]]
        await ctx.send(perm_list)



def setup(bot):
    bot.add_cog(logging(bot))



