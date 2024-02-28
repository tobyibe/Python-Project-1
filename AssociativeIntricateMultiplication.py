from IntricateInteger import IntricateInteger
def has_associative_intricate_multiplication(n,alpha):
    for x in range(n): #Loop over each value within Zn set
        for y in range(n):
            for z in range(n):
                ii_x = IntricateInteger(x, n, alpha) #Calculate x y and z intricate numbers
                ii_y = IntricateInteger(y, n, alpha)
                ii_z = IntricateInteger(z, n, alpha)
                lhs = (ii_x*ii_y)*ii_z #Multiply them according to the order in spec
                rhs = ii_x*(ii_y*ii_z)
                if lhs.object != rhs.object: #Check if they are not equal and return false if so
                    return False
    print("Associativity holds for all n,alpha values:",n,",",alpha) #Notice how multiplication associativity holds for all values of n with alpha values of 0, or with alpha values *0.5 of the n value (excluding when n is an odd number).
    return True #Otherwise return true