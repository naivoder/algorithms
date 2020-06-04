"""
the task is to generate a random number between 0 and i using a binary (0, 1) generator only
all numbers must be equally likely

if range is 0 to (2**i)-1 inclusive, generating a random number is a simple as concatenating i bits produced
--> i.e. range(0, 3) == range(0, 2**2 - 1) requires two bits, with four possible outcomes (00) (01) (10) (11)

if range falls in between 2**i and 2**i+1, we require i+1 bits, but must check for any values outside of range
--> i.e. range(0, 6) is in between 2**2 and 2**3, we generate three bits, if (110) or (111) is outcome, we must reroll
--> note: according to EPI probability of not getting a satisfactory answer in 10 attempts is less than 1 in 1 million

"""
from random import choice

def uniform_random_number(lower_bound, upper_bound):
    number_of_outcomes = int(upper_bound) - int(lower_bound) + 1
    while True:
        random_number, i = (0, 0)
        # while 2**i < outcomes, i.e. while we havent filled all required bits
        while (1 << i) < number_of_outcomes:
            # append 0 or 1 as LSB
            random_number = (random_number << 1) | choice([0, 1])
            i += 1
        # if result is not greater than desired range
        if random_number < number_of_outcomes:
            break
    return random_number + int(lower_bound)

if __name__=="__main__":
    print("###---Uniform Random Number Generater---###")
    lower_bound = input("Lower bound? ")
    upper_bound = input("Upper bound? ")
    print("Random number:", uniform_random_number(lower_bound, upper_bound))
