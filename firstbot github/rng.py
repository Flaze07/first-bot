import random

async def rng( message, messages ):
    temp = messages.split(' ')
    low_bound = int( temp[0] )
    high_bound = int( temp[1] )
    await message.channel.send( random.randint( low_bound, high_bound ) )