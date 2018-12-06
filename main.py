def is_feasible_to_continue(perm):
    i = len(perm) -1 #determine the last of the last placed queen.
    for j in range(i): # cycle through array to ensure queens are not attacking each other.
        if i - j == abs(perm[i] - perm[j]): # it is not feasible to continue if queens are attacking each other.
            return False
    return True

def build_permutations(perm, n):
    if len(perm) == n:
        print (perm)
        return

    for k in range(n):
        if k not in perm:
            perm.append(k)

            if is_feasible_to_continue(perm):
                build_permutations(perm, n)

            perm.pop()


build_permutations(perm = [], n = 8)
