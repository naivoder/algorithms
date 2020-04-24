"""
Author: Cameron Redovian

This class defines a Fraction object, and provides method overrides so that all basic numerical operators function as expected.

"""

class Fraction:

  #class contstructor
  def __init__(self, top, bottom):
    self.num = top
    self.den = bottom

  #override of string method to implement print function
  def __str__(self):
    return str(self.num) + "/" + str(self.den)

  #override of addition method
  def __add__(self, fraction):
    top = self.num * fraction.den + self.den * fraction.num
    bottom = self.den * fraction.den
    divisor = self.gcd(top, bottom)
    return Fraction(top//divisor, bottom//divisor)

  #custom method to emulate a print statement
  def show(self):
    print(self.num, "/", self.den)

  #seek GCD via Euclid's algorithm
  def gcd(self, top, bottom):
    while top % bottom != 0:
      holdUp = top; holdDown = bottom;
      top = holdDown
      bottom = holdUp % holdDown
    return bottom

  #override for "deep" equality, i.e. value not object
  def __eq__(self, fraction):
    first = self.num * fraction.den
    second = fraction.num * self.den
    return first == second

  #override of multiplication method
  def __mul__(self, fraction):
     top = self.num * fraction.num
     bottom = self.den * fraction.den
     divisor = self.gcd(top, bottom)
     return Fraction(top//divisor, bottom//divisor)

  #override of division method
  def __truediv__(self, fraction):
     reciprocal = Fraction(fraction.den, fraction.num)
     top = self.num * reciprocal.num
     bottom = self.den * reciprocal.den
     divisor = self.gcd(top, bottom)
     return Fraction(top//divisor, bottom//divisor)

  #override of less than or equal comparison
  def __le__(self, fraction):
     first = self.num / self.den
     second = fraction.num / fraction.den
     return first <= second

  #override of greater than or equal comparison
  def __ge__(self, fraction):
     first = self.num / self.den
     second = fraction.num / fraction.den
     return first >= second
