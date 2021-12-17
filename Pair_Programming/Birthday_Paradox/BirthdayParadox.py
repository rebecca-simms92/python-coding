

def possiblePairs(n):
    """ The number of possible independent pairs in a group of n people
    """
    return n*(n-1)/2

def birthdayParadox(p):
    no_of_pairs = possiblePairs(p)
    # probability of two people having the same birthday
    return( 1 -  (364/365) ** no_of_pairs)



p2 = 100
print(birthdayParadox(p2))

p3 = 164
print(birthdayParadox(p3))


def test_answer():
    assert round(birthdayParadox(23),2) == 0.50
