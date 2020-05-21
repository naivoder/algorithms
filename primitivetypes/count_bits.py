"""
this file implements a simple program to count the number of bits are set to '1' in a given number
it demonstrates shifting and masking techniques and is rather rude if your inputs are incorrect
experimenting with unpacking a function return with

"""

# function annotation format = (input: input's annotation) -> return's annotation
# function_name.__annotations__ prints dict {input: input's annotation, return: return's annotation}
def count_bits(number:int=None) -> int:
    if number is None:
        try:
            number = int(input("Enter a positive integer: "))
            if number <= 0:
                print("I said positive, idiot!")
                count_bits()
        except ValueError:
            print("Invalid number, idiot!")
            count_bits()
    given = number
    count = 0
    while number:
        count += number & 1
        number >>= 1
    return (given, bin(given), count)

def show(given, binary, solution):
    print("%s in binary = %s" % (given, binary))
    print("Total:", solution)
    print("Input type: %s\tReturn type: %s" % (count_bits.__annotations__['number'], count_bits.__annotations__['return']))

if __name__=="__main__":
    show(*count_bits(13))
    show(*count_bits())
    
