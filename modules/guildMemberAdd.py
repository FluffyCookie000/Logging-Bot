from datetime import datetime as DT
from discord.ext import commands
from variables.other import loggingchannels
import calendar
import discord
import json
import time

class guildMemberAdd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("guildMemberAdd initialized")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open('server config/server.json', 'r') as file:
            loggingchannels = json.load(file)
        for loggingchannel in loggingchannels['channels']:
            channel = self.bot.get_channel(loggingchannel)
            with open(f'server config/{loggingchannel}.json', 'r') as file:
                permconfig = json.load(file)
            if member.guild.id == channel.guild.id and permconfig['config']['guildMemberAdd'] == 1:
                embed = discord.Embed(description=f"{member.mention} joined", color=0x00ff00)
                embed.add_field(name="Name", value=f"{member} ({member.id}) {member.mention}", inline=False)
                date = DT.utcnow()
                utc_time = calendar.timegm(date.utctimetuple())
                string= str(member.created_at)
                b = DT.utcnow().timestamp()
                a = time.mktime(time.strptime(string[:-13], "%Y-%m-%d %H:%M:%S"))
                delta = b - a
                delta = int(delta / 86400)
                embed.add_field(name="Joined At", value=f"<t:{utc_time}:F>", inline=False)                
                embed.add_field(name="Account Age", value=f"**{delta}** days", inline=True)
                embed.add_field(name="Member Count", value=member.guild.member_count, inline=True)
                embed.add_field(name="ID", value=f"```INI\nMember = {member.id}\nGuild = {member.guild.id}```", inline=False)
                embed.set_author(name=member, icon_url=member.avatar.url)
                embed.set_footer(text=f"Fluffbot#9011", icon_url=self.bot.user.avatar.url)
                embed.timestamp = DT.now()
                await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(guildMemberAdd(bot))