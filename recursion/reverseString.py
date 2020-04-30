"""
this file implements a recursive solution to string reversal

"""

def reverser(string=None):
    if string is None:
        string = input("What string would you like to reverse? ")

    reversedString = ''

    # base case
    if len(string) is 1:
        return reversedString + string

    # reduce and recurse
    else:
        reversedString += string[-1]
        return reversedString + reverser(string[:-1])

if __name__=="__main__":
    print("###---Recursive String Reversal---###")
    print("Atlanta in reverse:", reverser("Atlanta"))
    print(reverser())
