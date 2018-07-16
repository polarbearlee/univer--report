from sys import exit
from random import randint

class Game(object):

    def __init__(self, start):
        self.quips = [
            " you kinda suck at this.",
            "don't quit your day job.",
            "Such a loser."
        ]
        self.start = start

    #main method to start playing
    def play(self):
        next = self.start
        action = "y"

        #start playing
        while True:
            print("\n-------")
            print("Beginning blkjk")
            print("Dealing.. \n")

            #deal user's cards
            unum1 = randint(1,10)
            unum2 = randint(1,10)
            utotal = unum1 + unum2
            print("Ur cards are: %d & %d totalling %d \n" % (unum1, unum2, utotal))

            #hit until user says stop
            while action == "y":
                action = input("Hit? > ")
                if action == "y":
                    utotal = utotal + self.hit()
                    print("ur new total is %d" % utotal)

            print("Ur total is %d " % utotal)

            #deal dealer's cards
            dnum1 = randint(1,10)
            dnum2 = randint(1,10)
            dtotal = dnum1 + dnum2
            print("Dealer's cards are %d & %d totalling %d \n" % (dnum1, dnum2, dtotal))

            #dealer keeps hitting until close/more than 21
            while dtotal < 21:
                print("    Dealer hits\n")
                dtotal = dtotal + self.hit()

            if dtotal <= 21:
                print("Dealer's total is %d " % dtotal)
                if utotal > dtotal:
                    print("you win!")
                    exit(1)
                else:
                    print("dealer wins")
                    self.death()
            else:
                print("Dealer busts, u win!")
                exit(1)




    def death(self):
        print(self.quips[randint(0, len(self.quips) - 1)])
        exit(1)

    def hit(self):
        nextcard = randint(1,9)
        print("ok, next card is %d " % nextcard)
        return nextcard


a_game = Game("deal")
a_game.play()