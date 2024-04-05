from datetime import datetime as DT
from discord.ext import commands

import calendar
import discord
import json

class messageDelete(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("messageDelete initialized")

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        with open('server config/server.json', 'r') as file:
            loggingchannels = json.load(file)
        for loggingchannel in loggingchannels['channels']:
            channel = self.bot.get_channel(loggingchannel)
            with open(f'server config/{loggingchannel}.json', 'r') as file:
                permconfig = json.load(file)
            if message.guild.id == channel.guild.id and permconfig['config']['messageDelete'] == 1:
                embed = discord.Embed(description=f"Message deleted in <#{message.channel.id}>", color=0x822aed)
                content = message.content
                embed.add_field(name="Content", value=content, inline=False)
                date = DT.utcnow()
                utc_time = calendar.timegm(date.utctimetuple())
                embed.add_field(name="Date", value=f"<t:{utc_time}:F>", inline=False)
                embed.add_field(name="ID", value=f"```INI\nUser = {message.author.id}\nMessage = {message.id}```")
                embed.set_author(name=message.author, icon_url=message.author.avatar.url)
                embed.set_footer(text=f"Fluffbot#9011", icon_url=self.bot.user.avatar.url)
                embed.timestamp = DT.now()
            await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(messageDelete(bot))