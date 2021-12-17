
no_of_sailors = 5


def coconut_remainder(num_of_coconuts):
    if num_of_coconuts % no_of_sailors  == 1:
        return True
    else:
        return False


def dividing_coconuts(total_coconuts):
    n = total_coconuts
    counter = 0
    coconuts_hidden = []
    for _ in range(no_of_sailors):
        coconuts_left = coconut_remainder(total_coconuts)
        if coconuts_left:
            a = (total_coconuts - 1) / no_of_sailors
            coconuts_hidden.append(a)
            total_coconuts = (no_of_sailors - 1)*((total_coconuts - 1) / no_of_sailors )
            counter += 1

    if counter == no_of_sailors :
        print("Size of initial pile of coconuts: ", int(n))
        print("Coconuts hidden by each sailor in the night: ", coconuts_hidden)





for k in range(1,100000):
    dividing_coconuts(k)

# Example answer:
# Size of initial pile of coconuts:  99996
# Coconuts hidden by each sailor in the night:  [19999.0, 15999.0, 12799.0, 10239.0, 8191.0]
# So pile of 99996 coconuts can be split this way without remainder. The amount of coconuts belonging to each sailor is contained in the list.
