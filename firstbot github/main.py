import discord 
from discord.ext.commands import Bot
from discord.utils import get

import calculator
import help
import listconv
import conv
import voting
import counselling
import leaderboard
import rng

#bot stuff
TOKEN = "NULL"
BOT_ID = 0

#bot object

client = Bot( command_prefix='f!' )

@client.event
async def on_message( message ):
    if message.author.id != BOT_ID:
        messages = str( message.content ).lower()
        if messages[0:5] == "f!cal":
            await message.channel.send( calculator.calculatorFunc( messages[5:len(messages)] ) )
        elif messages[0:10] == 'f!listconv':
            await listconv.list_conv( message, messages[11:len(messages)] )
        elif messages[0:6] == 'f!conv':
            await conv.conv_unit( message, messages[7:len(messages)] )
        elif messages[0:6] == "f!vote":
            await voting.vote( message )
        elif messages[0:9] == 'f!counsel':
            await counselling.add_roles( message, message.mentions[0] )       
        elif messages[0:8] == 'f!praise':
            await leaderboard.praise_leaderboard( message )
        elif messages[0:5] == 'f!rng':
            await rng.rng( message, messages[6:len(messages)] )
        elif messages[0:6] == 'f!help':
            if len( messages ) >= 8:
                await help.show_command( message, messages[7:len(messages)] )
            else:
                await help.show_command( message, '1' )

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="type f!help for help"))
    
client.run( TOKEN )