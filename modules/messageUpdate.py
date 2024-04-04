from datetime import datetime as DT
from discord.ext import commands
from variables.other import loggingchannels
import discord
import json

class messageUpdate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("messageUpdate initialized")

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        with open('server config/server.json', 'r') as file:
            loggingchannels = json.load(file)
        for loggingchannel in loggingchannels['channels']:
            channel = self.bot.get_channel(loggingchannel)
            with open(f'server config/{loggingchannel}.json', 'r') as file:
                permconfig = json.load(file)
            if after.guild.id == channel.guild.id and permconfig['config']['messageUpdate'] == 1:
                embed = discord.Embed(description=f"**{after.author}** updated their message in: {after.channel.name}.", color=0xe62aed)
                embed.add_field(name="Channel", value=f"<#{after.channel.id}>({after.channel.name})\n[Go To Message](https://discord.com/channels/{after.guild.id}/{after.channel.id}/{after.id})", inline=False)
                nowcontent = after.content
                previouscontent = before.content
                embed.add_field(name="Now", value=nowcontent, inline=False)
                embed.add_field(name="Previous", value=previouscontent, inline=False)
                embed.add_field(name="ID", value=f"```INI\nUser = {after.author.id}\nMessage = {after.id}```")
                embed.set_author(name=after.author, icon_url=after.author.avatar.url)
                embed.set_footer(text=f"Fluffbot#9011", icon_url=self.bot.user.avatar.url)
                embed.timestamp = DT.now()
            await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(messageUpdate(bot))