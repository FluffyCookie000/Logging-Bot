from discord.ext import commands
from datetime import datetime as DT
from discord.ext import commands
from variables.other import loggingchannels
import discord
import json
import os

class messageDeleteBulk(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("messageDeleteBulk initialized")

    @commands.Cog.listener()
    async def on_bulk_message_delete(self, messages):
        with open('server config/server.json', 'r') as file:
            loggingchannels = json.load(file)
        for loggingchannel in loggingchannels['channels']:
            channel = self.bot.get_channel(loggingchannel)
            with open(f'server config/{loggingchannel}.json', 'r') as file:
                permconfig = json.load(file)
            if messages[0].guild.id == channel.guild.id and permconfig['config']['messageDeleteBulk'] == 1:
                date = str(DT.now())
                for a in ['-', ' ', ':', '.']:
                    date = date.replace(a, '')
                file = open(f'imagedump/{date}.txt', 'w')
                filecontent = ""
                for message in messages:
                    filecontent = f"{filecontent}\n{message.author} ({message.author.id}) | ({message.author.avatar.url}) | {message.created_at}: {message.content}"
                file.write(filecontent)
                file.close()
                embed = discord.Embed(description=f'**{len(messages)}** message(s) were deleted and known in cache.', color=0xed498d)
                embed.set_footer(text=self.bot.user, icon_url=self.bot.user.avatar.url)
                embed.timestamp = DT.now()
                thing = await channel.send(embed=embed)
                await thing.reply( file=discord.File(f'imagedump/{date}.txt'))
                os.remove(f'imagedump/{date}.txt')



def setup(bot):
    bot.add_cog(messageDeleteBulk(bot))