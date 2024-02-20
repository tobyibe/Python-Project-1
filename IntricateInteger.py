import math
class IntricateInteger:
    def __init__(self, obj, mod, mul):
        self.object = obj
        self.mod = mod
        self.mul = mul

    # overwrite "print"
    def __str__(self):
        return "<"+str(self.object)+" mod "+str(self.mod)+" | "+str(self.mul)+">"

    # define "*"
    def __mul__(self,other):
        if ( self.mod != other.mod or self.mul != other.mul):
            raise ValueError("The two intricate integers should have the same modulus and multiplier")
        return IntricateInteger((self.object + other.object + self.mul*(math.lcm(self.object, other.object)))%self.mod, self.mod, self.mul)

a = IntricateInteger(3,5,4)
b = IntricateInteger(2,5,4)
print(a*b)