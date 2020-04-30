"""
this file implements a recursive algorithm for checking whether a given string is a palindrome

"""

def palindrome(string=None):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    if string is None:
        string = input("What word or sentance should be tested? ")
    og_string = string
    string = [char for char in string if char.lower() in letters and char is not ' ']
    if len(string) <= 1:
        return True
    else:
        if string[0].lower() == string[-1].lower():
            return palindrome(string[1:-1])
        else:
            return False

if __name__=="__main__":
    print("###---Recursive Palindrome Checker---###")
    print("'Live not on evil':", palindrome('Live not on evil'))
    print("'kayak':", palindrome('kayak'))
    print("'Reviled did I live, said I, as evil I did deliver':", palindrome('Reviled did I live, said I, as evil I did deliver'))
    print("'Go hang a salami; Im a lasagna hog!':", palindrome('Go hang a salami; Im a lasagna hog!'))
    print("'Able was I ere I saw Elba':", palindrome('Able was I ere I saw Elba'))
    print(palindrome())
