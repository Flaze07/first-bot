import discord 
from discord.ext.commands import Bot
from discord.utils import get

conv_list = dict()
conv_list['length'] = 'km \n cm \n mm \n feet \n inch'
conv_list['mass'] = 'kg \n g \n lb( pound )'
conv_list['time'] = 'second \n minute \n hour \n day \n week \n month \n year'

async def list_conv( message, input_str ):
    max_page = len( conv_list.keys() )
    input_int = 1
    try:
        input_int = int(input_str)
    except:
        input_int = 1
    if( input_int > max_page ):
        await message.channel.send( "page limit exceeded, max page is " + str( max_page ) )
        return
    conv_cat, convert_list = sorted( list( conv_list.items() ) )[ input_int - 1 ]
    embed = discord.Embed( title="list conversion", description='page ' + str( input_int ) + ' of ' + str( max_page )  )
    embed.add_field( name=conv_cat, value=convert_list, inline=False )
    await message.channel.send( embed=embed )