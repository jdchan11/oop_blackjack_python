
from random import shuffle

class BlackJack():
    global suits, values
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    def __init__(self, cards =[]):
        self.cards = cards
        
    def shuffleCards(self):
        shuffle(self.cards)
        return self.cards

    def deckOfCards(self):
        self.cards = []
        for s in suits:
            for v in values:
                self.cards.append(str(v) + " of " + s)
        return self.cards

    def dealCards(self): 
        self.dealtCard1 = self.cards.pop()
        self.dealtCard2 = self.cards.pop()
        self.dealtCard3 = self.cards.pop()
        self.dealtCard4 = self.cards.pop()
        self.player1Cards = [self.dealtCard1, self.dealtCard3]
        self.dealerCards = [self.dealtCard2, self.dealtCard4]
        print(f"The dealer's face-up card is {self.dealtCard2}")
        print(f"Your cards are {self.dealtCard1} and {self.dealtCard3}")
    
    def dealerTotalCheck(self):
        self.dealer_total = []
        for card in self.dealerCards:
            self.dealVal = int(card.split()[0])
            self.dealer_total.append(self.dealVal)
            if self.dealVal == 1:
                print("Dealer has Blackjack!")
                break
            else:
                self.dealVal = sum(self.dealer_total)
            return self.dealerCards

    def cardsAdd(self):
        self.current_cards = []
        for card in self.player1Cards:
            cardVal = int(card.split()[0])
            self.current_cards.append(cardVal)
        self.current_sum = sum(self.current_cards)
        print(f"Your current total is {self.current_sum}")
        return self.current_sum

    def userHit(self):
        self.hitCard = self.cards.pop()
        self.player1Cards.append(self.hitCard)
        print(f"Your new card is {self.hitCard}")
        new_cardVal = int(self.hitCard.split()[0])
        self.current_sum = self.current_sum + new_cardVal
        print(f"Your new total is {self.current_sum}")
        return self.current_sum

    def userStand(self):
        print(f"Your final cards are {self.player1Cards}")
        print(f"Your final total is {self.current_sum}")

    def winner(self):
        
        print(f"The dealer's total was {self.dealVal}.")
        print(f"Your total was {self.current_sum}.")
        if self.dealVal > self.current_sum:
            print("The dealer is the winner!")
        else:
            print("You are the winner! \nCongratulations!\n")

    

test1 = BlackJack()
def run():
    while True:
        test1.deckOfCards()
        test1.shuffleCards()
        test1.dealCards()
        test1.dealerTotalCheck()
        first_total = test1.cardsAdd()
        if first_total == 21:
            print("Blackjack!")
        else:
            while True:
                response = input("Would you like to hit or stand? ")
                if response.lower() == 'hit':
                    total = test1.userHit()
                    if total == 21:
                        print("You won!")
                        break
                    elif total > 21:
                        print("You busted. Better luck next time!")
                    else:
                        continue
                elif response.lower() == 'stand':
                    test1.userStand()
                    break
                else:
                    print("Please try another option. ")
        
        test1.winner()
        user_input = input("Would you like to play again? Yes or no?")
        if user_input.lower() == 'yes':
            continue
        else:
            break

run()

