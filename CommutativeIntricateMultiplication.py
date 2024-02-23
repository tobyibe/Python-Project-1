from IntricateInteger import IntricateInteger
def has_commutative_intricate_multiplication(n, alpha):
     # Checks if multiplication is commutative for given n and alpha.
    for x in range(n):
        for y in range(n):
            ii_x = IntricateInteger(x, n, alpha)
            ii_y = IntricateInteger(y, n, alpha)
            result_xy = ii_x * ii_y
            result_yx = ii_y * ii_x
            if result_xy.object != result_yx.object:
                return False  # Not commutative for these values
    return True  # Commutative for all x, y in Zn