# Find the greatest product of K consecutive digits in the N digit number.

#Input Format
#First line contains T that denotes the number of test cases.
#First line of each test case will contain two integers N & K. 
#Second line of each test case will contain a N digit integer.

# Output Format
# Print the required answer for each test case.

def get_Groups_Five(N, k):
    N = str(N)
    listN = []
    for digits in N:
        listN.append(int(digits))
    length_list = len(listN)
    combinations = []
    i = 0
    while i < (length_list - (k-1)):
        poss_comb = listN[i:i+k]
        combinations.append(poss_comb)
        i += 1
    return(combinations)


def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return(result)

def find_products(combs):
    products = []
    for list in combs:
        products.append(multiplyList(list))
    return(products)



def max_product(prod):
    max = 0
    for i in prod:
        if i > max:
            max = i
    return(max)




# test cases

n1 = 3675356291
k1 = 5

n2 = 2709360626
k2 = 5

n3 = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
k3 = 13


comb1 = get_Groups_Five(n1, k1)
prod1 = find_products(comb1)
print(max_product(prod1))

comb2 = get_Groups_Five(n2, k2)
prod2 = find_products(comb2)
print(max_product(prod2))

comb3 = get_Groups_Five(n3, k3)
prod3 = find_products(comb3)
print(max_product(prod3))
