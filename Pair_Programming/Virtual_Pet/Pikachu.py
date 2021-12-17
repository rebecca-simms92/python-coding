# Pikachu the Virtual Pet.

import time
from threading import *



class Tamagotchi(object):
    def __init__(self, name):
        self.name = name

        self.Hunger = 50
        self.Fullness = 50
        self.Happiness = 50
        self.Tiredness = 50

        self.is_alive = True

        self.mood = "Content"

    def Is_Tamagotchi_Alive(self):
        return self.is_alive

    def Dead_Tamagotchi(self):
        if self.Hunger >= 100:
            self.is_alive = False
            print(self.name, "has DIED!")
            return True
        if self.Tiredness >= 100:
            self.is_alive = False
            print(self.name, "has DIED!")
            return True
        else:
            return False

    def Display_Stats(self):
        if self.Dead_Tamagotchi():
            return
        else:
            print(self.name,'`s Stats are: \nHunger:', self.Hunger, '\nFullness:', self.Fullness, '\nTiredness:', self.Tiredness, '\nHappiness:', self.Happiness, '\nMood:', self.mood, "\n")



    def Feed_Tamagotchi(self):
        if self.Dead_Tamagotchi():
            return
        else:
            self.Hunger -= 10
            self.Fullness += 10


    def Play_Tamagotchi(self):
        if self.Dead_Tamagotchi():
            return
        else:
            self.Happiness += 20
            self.Tiredness += 10


    def Sleep_Tamagotchi(self):
        if self.Dead_Tamagotchi():
            return
        else:
            self.Tiredness -= 30


    def Poop_Tamagotchi(self):
        if self.Dead_Tamagotchi():
            return
        else:
            self.Fullness -= 10


    def Update_Mood(self):
        if self.Happiness >= 50:
            self.mood = 'Happy'
        else:
            self.mood = 'Sad'

        if self.Hunger >= 70:
            self.mood = "Hungry"


    def Update_Stats(self):
        if self.Dead_Tamagotchi():
            return
        else:
            self.Hunger += 5
            self.Happiness -= 5
            self.Tiredness += 5
            self.Fullness -= 5

            self.Update_Mood()


def Display_Options():
    print("\nWhat you can do:\n")
    print("1. Feed your Tamagotchi by typing Feed")
    print("2. Play with your Tamagotchi by typing Play")
    print("3. Put Tamagotchi to bed by typing Sleep")
    print("4. Make your Tamagotchi poop by typing Poop")
    print("5. Check how your Tamagotchi is doing by typing Check")



def play():

    name = input("What is your Tamagotchi's name? ")
    Pet = Tamagotchi(name)
    Pet.Display_Stats()

    def Background_Timer():
        while(Pet.Is_Tamagotchi_Alive()):
            Pet.Update_Stats()
            time.sleep(15)

    def User_Input():
        Display_Options()
        while(Pet.Is_Tamagotchi_Alive()):
            command = input("Interact with " + Pet.name + "? (Type Help for options)  ")
            if command == "Feed":
                Pet.Feed_Tamagotchi()
            if command == "Play":
                Pet.Play_Tamagotchi()
            if command == "Sleep":
                Pet.Sleep_Tamagotchi()
            if command == "Poop":
                Pet.Poop_Tamagotchi()
            if command == "Check":
                Pet.Update_Mood()
                Pet.Display_Stats()
            if command == "Help":
                Display_Options()

        exit()


    # create threads
    t = Timer(0.0, Background_Timer)
    t2 = Timer(1.0, User_Input)

    # start threads
    t.start()
    t2.start()







if __name__ == "__main__":
    play()
