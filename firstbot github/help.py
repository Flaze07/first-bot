import discord 
from discord.ext.commands import Bot
from discord.utils import get

from math import *

command_list = dict()
command_list['f!cal'] = 'a calculator, usage ex: f!cal 1 + 2'
command_list['f!conv'] = "convert a measurement from one unit to another. Format: f!conv <from> <to> <number>"
command_list['f!listconv'] = "list all available conversion"
command_list[ 'f!counsel'] = "counsel someone, used by owner of counselor role. Format: f!counsel <ping someone>"
command_list[ 'f!vote' ] = "make a vote, format: f!vote <whatever>"

async def show_command( message, input_str ):
    input_int = 1
    try:
        input_int = int( input_str )
    except ValueError:
        input_int = 1
    max_page = ceil( len( command_list.keys() ) / 2 )
    if input_int > max_page:
        await message.channel.send( "page limit exceeded, max page is " + str( max_page ) )
    input_int -= 1
    embed = discord.Embed( title='command list', description='page: ' + input_str + ' of ' + str( max_page ) )
    command_name, command_desc = sorted( list( command_list.items() ) )[ ( input_int * 2 ) ] 
    embed.add_field( name=command_name, value=command_desc, inline=False )
    if ( input_int * 2 ) + 1 < len( command_list ):
        command_name, command_desc = sorted( list( command_list.items() ) )[ ( input_int * 2 ) + 1 ]
        embed.add_field( name=command_name, value=command_desc, inline=False )
    await message.channel.send( embed=embed )
