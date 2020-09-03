import discord 

def meter_to_feet( init_val ):
    conv_num = 3.28084
    temp = init_val * conv_num
    temp_str = str( temp )
    if( temp_str.count( "." ) != 1 ):
        return temp_str
    else:
        numbers = temp_str.split(".")
        feet_part = numbers[0]
        inch_part = float( numbers[1]  ) * 12
        return ( str( feet_part ) + "'" + str( inch_part ) )

async def conv_unit( message, input_str ):
    command_str = input_str.split(' ', 2 )
    from_unit = command_str[0]
    to_unit = command_str[1]
    num = float()
    succeed = False
    try:
        if( command_str[2].count("'") != 1 ):
            num = float(command_str[2])
    except ValueError:
        await message.channel.send("that's not a number, " + message.author.name + " is a dumbass" )
        return
    #length
    #from imperial
    if from_unit == "inch":
        conv_num = 0.0254
        if to_unit == "m":
            succeed = True
            await message.channel.send( str( num * conv_num ) )
        elif to_unit == "cm":
            succeed = True
            await message.channel.send( str( num * conv_num * 100 ) )
        elif to_unit == "mm":
            succeed = True
            await message.channel.send( str( num * conv_num * 1000 ) )
        elif to_unit == "km":
            succeed = True
            await message.channel.send( str( ( num * conv_num ) / 1000 ) )
        elif to_unit == "feet":
            succeed = True
            await message.channel.send( str( num / 12 ) )
    elif from_unit == "feet":      
        conv_num = 0.3048
        if( command_str[2].count("'") == 1 ):
            numbers = [float(e) for e in command_str[2].split("'") ]
            print( numbers[0], ' ', numbers[1] )
            numbers[1] = numbers[1] + ( numbers[0] * 12 )
            num = numbers[1]
            conv_num = 0.0254
        if to_unit == "m":
            succeed = True
            await message.channel.send( str( num * conv_num ) )
        elif to_unit == "cm":
            succeed = True
            await message.channel.send( str( num * conv_num * 100 ) )
        elif to_unit == "mm":
            succeed = True
            await message.channel.send( str( num * conv_num * 1000 ) )
        elif to_unit == "km":
            succeed = True
            await message.channel.send( str( ( num * conv_num ) / 1000 ) )      
        elif to_unit == "inch":
            succeed = True
            await message.channel.send( str( num * 12 ) )
    elif from_unit == "m":
        if to_unit == "cm":
            succeed = True
            await message.channel.send( str( num * 100 ) )
        elif to_unit == "mm":
            succeed = True
            await message.channel.send( str( num * 1000 ) )
        elif to_unit == "km":
            succeed = True
            await message.channel.send( str( num / 1000 ) )
        elif to_unit == "feet":
            succeed = True
            await message.channel.send( meter_to_feet( num ) )
        elif to_unit == "inch":
            succeed = True
            await message.channel.send( str( num * 39.3701 ) )
    elif from_unit == "cm":
        if to_unit == "m":
            succeed = True
            await message.channel.send( str( num / 100 ) )
        elif to_unit == "mm":
            succeed = True
            await message.channel.send( str( num * 10 ) )
        elif to_unit == "km":
            succeed = True
            await message.channel.send( str( num / 100000 ) )
        elif to_unit == "feet":
            succeed = True
            await message.channel.send( meter_to_feet( num / 100 ) )
        elif to_unit == "inch":
            succeed = True
            await message.channel.send( str( ( num / 100 ) * 39.3701 ) )
    elif from_unit == "mm":
        if to_unit == "cm":
            succeed = True
            await message.channel.send( str( num / 10 ) )
        elif to_unit == "m":
            succeed = True
            await message.channel.send( str( num / 1000 ) )
        elif to_unit == "km":
            succeed = True
            await message.channel.send( str( num / 1000000 ) )
        elif to_unit == "feet":
            succeed = True
            await message.channel.send( meter_to_feet( num / 1000 ) )
        elif to_unit == "inch":
            succeed = True
            await message.channel.send( str( ( num / 1000 ) * 39.3701 ) )
    elif from_unit == "km":
        if to_unit == "cm":
            succeed = True
            await message.channel.send( str( num * 100000 ) )
        elif to_unit == "m":
            succeed = True
            await message.channel.send( str( num * 1000 ) )
        elif to_unit == "mm":
            succeed = True
            await message.channel.send( str( num * 1000000 ) )
        elif to_unit == "feet":
            succeed = True
            await message.channel.send( meter_to_feet( num * 1000 ) )
        elif to_unit == "inch":
            succeed = True
            await message.channel.send( str( ( num * 1000 ) * 39.3701 ) )
    #mass
    elif from_unit == "kg":
        if to_unit == "g":
            succeed = True
            await message.channel.send( str( num * 1000 ) )
        elif to_unit == "lb" or to_unit == "pound":
            succeed = True
            await message.channel.send( str( num * 2.20462 ) )
    elif from_unit == "g":
        if to_unit == "kg":
            succeed = True
            await message.channel.send( str( num / 1000 ) )
        elif to_unit == "lb" or to_unit == "pound":
            succeed = True
            await message.channel.send( str( ( num / 1000 ) * 2.20462 ) )
    elif from_unit == "lb" or from_unit == "pound":
        if to_unit == "kg":
            succeed = True
            await message.channel.send( str( num * 0.453592 ) )
        elif to_unit == "g":
            succeed = True
            await message.channel.send( str( ( num * 0.453592  ) / 1000 ) )
    #time
    elif from_unit == "second":
        if to_unit == "minute":
            succeed = True
            await message.channel.send( str( num / 60 ) )
        elif to_unit == "hour":
            succeed = True
            await message.channel.send( str( num / ( 60 * 60 ) ) )
        elif to_unit == "day":
            succeed = True
            await message.channel.send( str( num / ( 60 * 60 * 24 ) ) )
        elif to_unit == "week":
            succeed = True
            await message.channel.send( str( num / ( 60 * 60 * 24 * 7 ) ) )
        elif to_unit == "month":
            succeed = True
            await message.channel.send( str( num / ( 60 * 60 * 24 * 30 ) ) ) 
        elif to_unit == "year":
            succeed = True
            await message.channel.send( str( num / ( 60 * 60 * 24 * 30 * 12 ) ) )
    elif from_unit == "minute":
        if to_unit == "second":
            succeed = True
            await message.channel.send( str( num * 60 ) )
        elif to_unit == "hour":
            succeed = True
            await message.channel.send( str( num / 60 ) )
        elif to_unit == "day":
            succeed = True
            await message.channel.send( str( num / ( 60 * 24 ) ) )
        elif to_unit == "week":
            succeed = True
            await message.channel.send( str( num / ( 60 * 24 * 7 ) ) )            
        elif to_unit == "month":
            succeed = True
            await message.channel.send( str( num / ( 60 * 24 * 30 ) ) )
        elif to_unit == "year":
            succeed = True
            await message.channel.send( str( num / ( 60 * 24 * 30 * 12 ) ) )
    elif from_unit == "hour":
        if to_unit == "second":
            succeed = True
            await message.channel.send( str( num * ( 60 * 60 ) ) )
        elif to_unit == "minute":
            succeed = True
            await message.channel.send( str( num * 60 ) )
        elif to_unit == "day":
            succeed = True
            await message.channel.send( str( num / 24 ) )
        elif to_unit == "week":
            succeed = True
            await message.channel.send( str( num / ( 24 * 7 ) ) )        
        elif to_unit == "month":
            succeed = True
            await message.channel.send( str( num / ( 24 * 30 ) ) )
        elif to_unit == "year":
            succeed = True
            await message.channel.send( str( num / ( 24 * 30 * 12 ) ) )
    elif from_unit == "day":
        if to_unit == "second":
            succeed = True
            await message.channel.send( str( num * ( 24 * 60 * 60 ) ) )
        elif to_unit == "minute":
            succeed = True
            await message.channel.send( str( num * ( 24 * 60 ) ) )
        elif to_unit == "hour":
            succeed = True
            await message.channel.send( str( num * 24 ) )
        elif to_unit == "week":
            succeed = True
            await message.channel.send( str( num / ( 7 ) ) )
        elif to_unit == "month":
            succeed = True
            await message.channel.send( str( num / 30 ) )
        elif to_unit == "year":
            succeed = True
            await message.channel.send( str( num / ( 30 * 12 ) ) )
    elif from_unit == "week":
        if to_unit == "second":
            succeed = True
            await message.channel.send( str( num * ( 7 * 24 * 60 * 60 ) ) )
        elif to_unit == "minute":
            succeed = True
            await message.channel.send( str( num * ( 7 * 24 * 60 ) ) )
        elif to_unit == "hour":
            succeed = True
            await message.channel.send( str( num * ( 7 * 24 ) ) )
        elif to_unit == "day":
            succeed = True
            await message.channel.send( str( num * 7 ) )
        elif to_unit == "month":
            succeed = True
            await message.channel.send( str( num / 4 ) )
        elif to_unit == "year":
            succeed = True
            await message.channel.send( str( num / ( 4 * 12 ) ) )
    elif from_unit == "week":
        if to_unit == "second":
            succeed = True
            await message.channel.send( str( num * ( 7 * 24 * 60 * 60 ) ) )
        elif to_unit == "minute":
            succeed = True
            await message.channel.send( str( num * ( 7 * 24 * 60 ) ) )
        elif to_unit == "hour":
            succeed = True
            await message.channel.send( str( num * ( 7 * 24 ) ) )
        elif to_unit == "month":
            succeed = True
            await message.channel.send( str( num / 4 ) )
        elif to_unit == "year":
            succeed = True
            await message.channel.send( str( num / ( 4 * 12 ) ) )
    elif from_unit == "month":
        if to_unit == "second":
            succeed = True
            await message.channel.send( str( num * ( 30 * 24 * 60 * 60 ) ) )
        elif to_unit == "minute":
            succeed = True
            await message.channel.send( str( num * ( 30 * 24 * 60 ) ) )
        elif to_unit == "hour":
            succeed = True
            await message.channel.send( str( num * (30 * 24 ) ) )
        elif to_unit == "week":
            succeed = True
            await message.channel.send( str( num * 4 ) )
        elif to_unit == "year":
            succeed = True
            await message.channel.send( str( num / 12  ) )
    elif from_unit == "year":
        if to_unit == "second":
            succeed = True
            await message.channel.send( str( num * ( 12 * 30 * 24 * 60 * 60 ) ) )
        elif to_unit == "minute":
            succeed = True
            await message.channel.send( str( num * ( 12 * 30 * 24 * 60 ) ) )
        elif to_unit == "hour":
            succeed = True
            await message.channel.send( str( num * ( 12 * 30 * 24 ) ) )
        elif to_unit == "week":
            succeed = True
            await message.channel.send( str( num * 12 * 4 ) )
        elif to_unit == "month":
            succeed = True
            await message.channel.send( str( num * 12  ) )   
    if( succeed == False ):
        await message.channel.send( "this conversion doesn't exist yet, feel free to contact the developer" ) 