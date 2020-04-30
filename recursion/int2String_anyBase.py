"""
this file implements a recursive solution to converting a given integer to a string in any base (between 2, 16)

"""

def convert(number=None, base=None):
    if number is None:
        number = int(input("What number would you like to convert? "))
    if base is None:
        base = int(input("What base would you like to convert? "))

    characters = '0123456789ABCDEF'

    # check for base case
    if number < base:
        return characters[number]

    # reduce problem size and make recursive call
    return convert(number // base, base) + characters[number % base]

if __name__=="__main__":
    print("###---Recursive Base Conversion---###")
    print("Example number: 38576")
    print("Base 10:", convert(38576,10))
    print("Base 16:", convert(38576,16))
    print("Base  8:", convert(38576, 8))
    print("Base  2:", convert(38576, 2))
    print("\nInteractive example...")
    print(convert())
