import math 
class IntricateIntegers:
    def __init__(self,mod,mul):
        if (not (isinstance(mod, int) and isinstance(mul, int))):
            raise ValueError("The value, modulus and multiplier must all be integers")
        elif (mod <= 0):
            raise ValueError("The modulus has to be a positive integer")
        elif (mul < 0) or (mul>= mod):  
            raise ValueError("The multiplier must be part of Zₙ")
        self.mod = mod
        self.mul = mul
        
    def size(self):
        return self.mod
    
    def __str__(self):
        output = "<["
        for i in range(self.size()):
            output+= str(i)+","
        output+="\b]>"
        return output

x = IntricateIntegers(3,2)
print(x)