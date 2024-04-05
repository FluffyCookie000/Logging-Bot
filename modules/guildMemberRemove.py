from datetime import datetime as DT
from discord.ext import commands

import datetime
import discord
import json


class guildMemberRemove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("guildMemberRemove initialized")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        with open('server config/server.json', 'r') as file:
            loggingchannels = json.load(file)
        for loggingchannel in loggingchannels['channels']:
            channel = self.bot.get_channel(loggingchannel)
            with open(f'server config/{loggingchannel}.json', 'r') as file:
                permconfig = json.load(file)
            if member.guild.id == channel.guild.id and permconfig['config']['guildMemberRemove'] == 1:
                entry = list(await member.guild.audit_logs(limit=1).flatten())[0]   
                if str(entry.action) == "AuditLogAction.kick" and entry.target.id == member.id:
                    des = f"{member} was kicked"
                    id = f"```INI\nUser = {member.id}\nPerpetrator = {entry.user.id}```"
                    fote = entry.user
                    foic = entry.user.avatar.url
                else:
                    des = f"{member} left the server"
                    id = f"```INI\nUser = {member.id}```"
                    fote = self.bot.user
                    foic = self.bot.user.avatar.url
                embed = discord.Embed(description=des, color=0xff0000)
                embed.add_field(name="User Information", value=f"{member} ({member.id}) {member.mention}")
                roles = ""
                for r in member.roles:
                    if r.id != member.guild.id:
                        roles = f'{roles}{r.name}, '
                if roles == "":
                    roles = "None, "
                embed.add_field(name="Roles", value=roles[:-2], inline=False)
                joindate = str(member.joined_at)
                timestamp = DT.strptime(joindate[:-13],"%Y-%m-%d %H:%M:%S").replace(tzinfo=datetime.timezone.utc).timestamp()

                embed.add_field(name="Joined At", value=f"<t:{str(timestamp)[:-2]}:F> (<t:{str(timestamp)[:-2]}:R>)", inline=False)
                createdate = str(member.created_at)
                timestamp = DT.strptime(createdate[:-13],"%Y-%m-%d %H:%M:%S").replace(tzinfo=datetime.timezone.utc).timestamp()
                embed.add_field(name="Created At", value=f"<t:{str(timestamp)[:-2]}:F> (<t:{str(timestamp)[:-2]}:R>)", inline=False)
                if 'Perpetrator' in id:
                    embed.add_field(name="Reason", value=entry.reason, inline=False)
                embed.add_field(name="ID", value=id)
                embed.set_author(name=member, icon_url=member.avatar.url)
                embed.set_footer(text=fote, icon_url=foic)
                embed.timestamp = DT.now()
                await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(guildMemberRemove(bot))