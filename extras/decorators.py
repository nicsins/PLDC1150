'''simple decorator from realpython'''
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

''' makes octothorps for effect'''
def decorate(func):
    def wrapper():
        print("#"*80)
        func()
        print("#"*80)
    return wrapper()



'''stolen from stack  '''
def bread(func):
    def wrapper():
        print("</''''''\>")
        func()
        print("<\______/>")
    return wrapper

def ingredients(func):
    def wrapper():
        print("#tomatoes#")
        func()
        print("~salad~")
    return wrapper

def sandwich(food="--ham--"):
    print(food)

sandwich()
#outputs: --ham--
sandwich = bread(ingredients(sandwich))
sandwich()
#outputs:
#</''''''\>
# #tomatoes#
# --ham--
# ~salad~
#<\______/>

'''from wiki'''
"""
Demonstrated decorators in a world of a 10x10 grid of values 0-255. 
"""

import random

def s32_to_u16( x ):
    if x < 0:
        sign = 0xf000
    else:
        sign = 0
    bottom = x & 0x00007fff
    return bottom | sign

def seed_from_xy( x,y ): return s32_to_u16( x ) | (s32_to_u16( y ) << 16 )

class RandomSquare:
    def __init__( s, seed_modifier ):
        s.seed_modifier = seed_modifier
    def get( s, x,y ):
        seed = seed_from_xy( x,y ) ^ s.seed_modifier
        random.seed( seed )
        return random.randint( 0,255 )

class DataSquare:
    def __init__( s, initial_value = None ):
        s.data = [initial_value]*10*10
    def get( s, x,y ):
        return s.data[ (y*10)+x ] # yes: these are all 10x10
    def set( s, x,y, u ):
        s.data[ (y*10)+x ] = u

class CacheDecorator:
    def __init__( s, decorated ):
        s.decorated = decorated
        s.cache = DataSquare()
    def get( s, x,y ):
        if s.cache.get( x,y ) == None:
            s.cache.set( x,y, s.decorated.get( x,y ) )
        return s.cache.get( x,y )

class MaxDecorator:
    def __init__( s, decorated, max ):
        s.decorated = decorated
        s.max = max
    def get( s, x,y ):
        if s.decorated.get( x,y ) > s.max:
            return s.max
        return s.decorated.get( x,y )

class MinDecorator:
    def __init__( s, decorated, min ):
        s.decorated = decorated
        s.min = min
    def get( s, x,y ):
        if s.decorated.get( x,y ) < s.min:
            return s.min
        return s.decorated.get( x,y )

class VisibilityDecorator:
    def __init__( s, decorated ):
        s.decorated = decorated
    def get( s,x,y ):
        return s.decorated.get( x,y )
    def draw(s ):
        for y in range( 10 ):
             for x in range( 10 ):
                 print ("%3d" % s.get( x,y ))


# Now, build up a pipeline of decorators:

random_square = RandomSquare( 635 )
random_cache = CacheDecorator( random_square )
max_filtered = MaxDecorator( random_cache, 200 )
min_filtered = MinDecorator( max_filtered, 100 )
final = VisibilityDecorator( min_filtered )

final.draw()

