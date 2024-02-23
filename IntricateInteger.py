import math
class IntricateInteger:
    # Represents an intricate integer with modular arithmetic operations.

    def __init__(self, object, mod, mul):
        if (not (isinstance(object, int) and isinstance(mod, int) and isinstance(mul, int))):
            raise ValueError("The value, modulus and multiplier must all be integers")
        elif (mod <= 0):
            raise ValueError("The modulus has to be a positive integer")
        elif (object < 0) or (object >= mod) or (mul < 0) or (mul>= mod):  
            raise ValueError("The value and the multiplier must be part of Zₙ")
        self.object = object
        self.mod = mod
        self.mul = mul

    # overwrite "print"
    def __str__(self):
        # Returns a string representation of the IntricateInteger object.
        return "<"+str(self.object)+" mod "+str(self.mod)+" | "+str(self.mul)+">"

    # define "*"
    def __mul__(self,other):
        # Multiplies two IntricateInteger objects.
        if ( self.mod != other.mod or self.mul != other.mul):
            raise ArithmeticError("The two intricate integers must have the same modulus and multiplier")
        return IntricateInteger((self.object + other.object + self.mul * (math.lcm(self.object, other.object))) % self.mod, self.mod, self.mul)



