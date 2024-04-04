from datetime import datetime as DT
from discord.ext import commands
from variables.other import loggingchannels
import discord
import json

class channelCreate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("channelCreate initialized")

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        with open('server config/server.json', 'r') as file:
            loggingchannels = json.load(file)
        for loggingchannel in loggingchannels['channels']:
            channell = self.bot.get_channel(loggingchannel)
            with open(f'server config/{loggingchannel}.json', 'r') as file:
                permconfig = json.load(file)
            if channel.guild.id == channell.guild.id and permconfig['config']['channelCreate'] == 1:
                entry = list(await channell.guild.audit_logs(limit=1).flatten())[0]   
                if str(entry.action) == "AuditLogAction.channel_create" and entry.target.id == channel.id:
                    perpetrator = entry.user
                embed = discord.Embed(description=f'{channel.type} channel created <#{channel.id}>', color=0x36393f)
                embed.add_field(name="Name", value=f"{channel.name}", inline=False)
                embed.add_field(name='ID', value=f'```INI\nUser = {perpetrator.id}\nChannel = {channel.id}```')
                listj = str(entry.after).split("overwrites=")
                listj = str(listj[1]).split("),")
                for i in listj:
                    if 'everyone' not in i:
                        if 'discriminator' in i:
                            i = (i.split('discriminator')[0])[3:]
                        else:
                            i = (i.split('>')[0])[3:]
                        type = i.split(' ')[0]
                        id = (i.split(' ')[1])[3:]
                        name = (i.split("'")[1])
                        
                        permch = self.bot.get_channel(channel.id)
                        if type == 'Role':
                            permrl = channel.guild.get_role(int(id))
                        else:
                            permrl = channel.guild.get_member(int(id))
                        perm_list = [perm[0] for perm in permch.overwrites_for(permrl) if perm[1]]
                        perm = ""
                        for p in perm_list:
                            perm = f'{perm}, {p}'
                        embed.add_field(name=name, value=f'Type: {type}\nPermissions: {perm[1:]}', inline=False)
                embed.set_author(name=perpetrator, icon_url=perpetrator.avatar.url)
                embed.set_footer(text=self.bot.user, icon_url=self.bot.user.avatar.url)
                embed.timestamp = DT.now()
                await channell.send(embed=embed)       

def setup(bot):
    bot.add_cog(channelCreate(bot))