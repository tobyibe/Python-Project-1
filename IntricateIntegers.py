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

    # implemented functions to allow the iteration of IntricateInteger objects
    def __iter__(self):
        self.object = 0
        return self

    # iterates until the object count is smaller than the mod count
    def __next__(self):
        if self.object < self.mod:
            self.object += 1
            return f"<{self.object-1} mod {self.mod} | {self.mul}>"
        else:
            raise StopIteration

#Code for testing IntricateIntegers use

#for x in IntricateIntegers(3,2):
#   print(x)

#x = IntricateIntegers(3,2)
#print(x)