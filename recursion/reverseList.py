"""
this file implements a recursive function to reverse a list

"""

def reverse(a_list=None):
    if a_list is None:
        a_list = input("What list would you like to reverse? ")
        a_list = [char for char in a_list.split(',')]
    reversed = []
    if len(a_list) is 1:
        return reversed + a_list
    reversed.append(a_list.pop())
    return reversed + reverse(a_list)

if __name__=="__main__":
    example = reverse([1,2,3])
    print(example)
    user = reverse()
    print(user)
