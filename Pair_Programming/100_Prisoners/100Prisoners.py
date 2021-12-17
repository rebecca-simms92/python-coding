from random import randint

def prisonerProblem():
    list_of_prisoners = ['0']*99 + ['L']*1
    no_of_prisoners = len(list_of_prisoners)
    counter = 0
    tries = 0
    while counter < 100:
        i = randint(0, no_of_prisoners - 1)
        if list_of_prisoners[i] == '0':
            list_of_prisoners[i] = '1'
        elif list_of_prisoners[i] == '1':
            counter += 1
        tries += 1
    print("100 prisoners have entered the room. This took", tries, "tries")

prisonerProblem()
