import discord

async def vote( message ):
    temporary = message.content.replace( 'f!vote', '' )
    await message.delete()
    to_react = await message.channel.send( temporary )
    processed_emoji = "\N{GRINNING FACE}"
    await to_react.add_reaction( processed_emoji )