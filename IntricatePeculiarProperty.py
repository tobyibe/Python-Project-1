from IntricateInteger import IntricateInteger

def has_intricate_peculiar_property(mod,mul):
    flag = True
    for i in range(mod):
        x = IntricateInteger(i,mod,mul)
        a = x*x
        if (a.object != x.object or a.mod != x.mod or a.mul != x.mul):
            flag = False
        else:
            print(x, a)
    return flag

def test_intricate_peculiar_property_to_50():
    for i in range(1,51):   #For each n to 50
        mod_minus_1 = False
        others = False
        mod = i
        for j in range(mod):    #For each multiplier to n-1
            mul = j
            if (mul == mod - 1 and has_intricate_peculiar_property(mod,mul)):
                mod_minus_1 = True
            elif(has_intricate_peculiar_property(mod,mul)):
                others = True
        if (mod_minus_1 and not others):
            print(mod)

test_intricate_peculiar_property_to_50()    #By running this, we can deem that for all 1≤n≤50, that the Intricate Peculiar Property only holds when a=n-1