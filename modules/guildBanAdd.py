from datetime import datetime as DT
from discord.ext import commands

import discord
import json

class guildBanAdd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("guildBanAdd initialized")

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        with open('server config/server.json', 'r') as file:
            loggingchannels = json.load(file)
        for loggingchannel in loggingchannels['channels']:
            channel = self.bot.get_channel(loggingchannel)
            with open(f'server config/{loggingchannel}.json', 'r') as file:
                permconfig = json.load(file)
            if guild.id == channel.guild.id and permconfig['config']['guildBanAdd'] == 1:
                entry = list(await guild.audit_logs(limit=1).flatten())[0]   
                if str(entry.action) == "AuditLogAction.ban" and entry.target.id == user.id:
                    perpetratorid = entry.user.id
                    reason = entry.reason
                embed = discord.Embed(description=f'{user} was banned')
                embed.add_field(name="User Information", value=f"{user} ({user.id}) {user.mention}", inline=False)
                embed.add_field(name="Reason", value=reason, inline=False)
                embed.add_field(name='ID', value=f'```INI\nUser = {user.id}\nPerpetrator = {perpetratorid}```')
                embed.set_author(name=user, icon_url=user.avatar.url)
                embed.set_footer(text=entry.user, icon_url=entry.user.avatar.url)
                embed.timestamp = DT.now()
                await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(guildBanAdd(bot))