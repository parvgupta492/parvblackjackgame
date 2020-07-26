from random import randint
class player():
    def __init__(self,name,initialamt):
        self.name=name
        self.balance=initialamt
        self.latestbetamt=0
        self.sumofcards=0
        self.cardlist=[]
        self.numofaces=0
    def initfunc(self):
        self.sumofcards=0
        self.cardlist=[]
        self.numofaces=0
    def placebet(self):
        inp=int(input("How much You want to bet out of your current balance of ${} ?: ".format(self.balance)))
        while inp>self.balance:
            inp=int(input("How much You want to bet out of your current balance of ${} ?: ".format(self.balance)))
        self.latestbetamt=inp
        self.balance-=inp
    def print_cards(self):
        print("\n{}'s Hand:".format(self.name))
        for item in self.cardlist:
            print(item)
        print("Sum= {}".format(self.sumofcards))
class computer():
    def __init__(self):
        self.cardlist=[]
        self.sumofcards=0
        self.numofaces=0
    def print_cards_first_card_unknown(self):
        print("\nDealer's Hand:")
        print("<card hidden>")
        counter=0
        for item in self.cardlist:
            if counter==0:
                counter+=1
                continue
            counter+=1
            print(item)
    def print_cards(self):
        print("\nDealer's Hand:")
        for item in self.cardlist:
            print(item)
        print("Sum= {}".format(self.sumofcards))
class cards():
    def __init__(self):
        self.suits=("hearts","spades","diamonds","clubs")
        self.availablecards={"hearts":[0,1,1,1,1,1,1,1,1,1,1,1,1,1],"spades":[0,1,1,1,1,1,1,1,1,1,1,1,1,1],"diamonds":[0,1,1,1,1,1,1,1,1,1,1,1,1,1],"clubs":[0,1,1,1,1,1,1,1,1,1,1,1,1,1]}
        self.cardvalues={1:11,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:10,11:10,12:10,13:10}
        self.cardnames=["","Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]
    def adjustforace(self,whodrawing):
        while whodrawing.sumofcards>21 and whodrawing.numofaces>0:
            whodrawing.sumofcards-=10
            whodrawing.numofaces-=1
    def draw_card(self,whodrawing):
        while True:
            cardsuit=randint(0,3)
            cardno=randint(1,13)
            if self.availablecards[self.suits[cardsuit]][cardno]==0:
                continue
            self.availablecards[self.suits[cardsuit]][cardno]=0
            whodrawing.cardlist.append(self.cardnames[cardno]+" of "+self.suits[cardsuit])
            whodrawing.sumofcards+=self.cardvalues[cardno]
            if cardno==1:
                whodrawing.numofaces+=1
            #adjustforace func can be needed to call when current drawn card is not an ace
            if whodrawing.numofaces>0 and whodrawing.sumofcards>21:
                self.adjustforace(whodrawing)
            break
def startgame():
    name=input("Please Enter your Name: ")
    initialamt=int(input("How much money worth chips you want to buy?: "))
    p1=player(name,initialamt)
    response=True
    while response and p1.balance>0:
        p1.initfunc()
        c1=cards()
        comp=computer()
        p1.placebet()
        c1.draw_card(p1)
        c1.draw_card(p1)
        c1.draw_card(comp)
        c1.draw_card(comp)
        comp.print_cards_first_card_unknown()
        p1.print_cards()
        print("\n{}'s TURN STARTS: ".format(p1.name))
        while p1.sumofcards<21:
            inp=input("Do you wish to 'HIT' or 'STAND' ?")
            if inp.lower()=='stand':
                break
            c1.draw_card(p1)
            p1.print_cards()
        if p1.sumofcards>21:
            print("You bust and hence you lost ${} ".format(p1.latestbetamt))
        else:
            print("\nDealer's TURN STARTS: ")
            comp.print_cards()
            while comp.sumofcards<17:
                c1.draw_card(comp)
                comp.print_cards()
            playerwon=False
            if comp.sumofcards>21:
                playerwon=True
            elif p1.sumofcards==comp.sumofcards:
                print("IT WAS A PASS AND YOU WILL GET YOUR MONEY BACK...")
                p1.balance+=p1.latestbetamt
            elif p1.sumofcards>comp.sumofcards:
                playerwon=True
            elif p1.sumofcards<comp.sumofcards :
                print("YOU LOST ${}".format(p1.latestbetamt))
            if playerwon==True:
                print("YOU WON ${}".format(p1.latestbetamt))
                p1.balance+=(2*p1.latestbetamt)
        print("\nFINALLY CARDS LOOKS LIKE: ")
        p1.print_cards()
        comp.print_cards()
        inp=input("Do You want to Place Bet ?YOUR CURRENT BALANCE IS : ${} ".format(p1.balance))
        if inp.lower()=='no':
            response=False
    if p1.balance==0 and response:
        print("AS YOUR CHIPS FINISHED SO YOU CANT PLAY ANYMORE!!!")
    return p1.balance
def playblackjack():
    print("Welcome to BlackJack! Get as close to 21 as you can without going over!")
    print("Dealer hits until she reaches 17. Aces count as 1 or 11.")
    response=True
    while response:
        moneywon=startgame()
        print("You Have ${} after Finishing playing the game ".format(moneywon))
        inp=input("Do you want to play again ? ")
        if inp.lower()=="no":
            response=False
    print("Thank You For playing BLACKJACK!")


playblackjack()