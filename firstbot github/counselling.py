import discord
from discord.utils import get

async def add_roles( message, args1 : discord.Member ):
    role_check = get( message.guild.roles, name='Counselor' )
    if( role_check in message.author.roles ):
        Member = args1
        role = get( message.guild.roles, name='Patient' )
        if( role in Member.roles ):
            await Member.remove_roles( role )
        else:
            await Member.add_roles( role )