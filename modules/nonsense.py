# overwite = '''overwrites=[(<Role id=767528920437227530 name='@everyone'>, <discord.permissions.PermissionOverwrite object at 0x0000025230BC4820>),
# (<Role id=967146581688189030 name='Karma-o'>, <discord.permissions.PermissionOverwrite object at 0x0000025230BC7700>),
# (<Role id=946412059724247105 name='pIain-o'>, <discord.permissions.PermissionOverwrite object at 0x0000025230BC7A60>),
# (<Member id=505492754038521859 name='bimply' discriminator='0' bot=False nick=None guild=<Guild id=767528920437227530 name='bot testing' shard_id=0 chunked=True member_count=31>>, <discord.permissions.PermissionOverwrite object at 0x0000025230BC7100>)]'''

# list = overwite.split("),")
# for i in list:
#     if 'discriminator' in i:
#         i = (i.split('discriminator')[0])[3:]
#     else:
#         i = (i.split('>')[0])[3:]

#     type = i.split(' ')[0]
#     id = (i.split(' ')[1])[3:]
#     name = (i.split("'")[1])[6:-1]

#     print(f'Type: {type}|ID: {id}|Name: {name}')
