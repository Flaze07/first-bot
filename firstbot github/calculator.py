from math import *

def calculatorFunc( messages ):
    messages = messages.replace( '^', '**' )
    return eval( messages )