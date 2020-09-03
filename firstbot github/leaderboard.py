import discord

async def praise_leaderboard( message ):
    if message.guild.id == 732553190918193192:
        members = message.guild.members
        for member in members:
            if( not member.bot ):
                await message.channel.send( member )