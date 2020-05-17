from enum import auto, Enum #enum okundu
# Tuple'larda keyler integer olarak tanımlanır. Enum burda bunun önüne geçer bir bakıma ve bize sembolik isimleri
# değerler için atamamıza olanak tanır.
from itertools import product 
"""
#itertools -> product

cartesian product, equivalent to a nested for-loop
ex -> product('ABCD', repeat=2)
output -> AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
"""
from random import shuffle
from typing import List, NamedTuple #namedtuple okundu


# class Vault:
#     def __init__(self,your_money,your_bet,iscond):
#             self.your_money = your_money
#             self.your_bet = your_bet
#             self.iscond = iscond
#     def money(self):
#         # global your_money
#         # global ask_sit
#         # global ask_bet
#         # global iscond
#         self.your_money = 0       
#         self.your_bet = 0     
#         ask_sit = int(input("sit with: ")) 
#         self.your_money += ask_sit        
#         ask_bet = int(input("bet with: "))      
#         self.your_bet = ask_bet       
#         self.iscond = 0
    

class Rank(Enum): #RANKLER TANIMLANIR
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 10
    QUEEN = 10
    KING = 10

class Suit(Enum):   #TAKIMLARI TANIMLANIR
    SPADES = auto()
    CLUBS = auto()
    DIAMONDS = auto()
    HEARTS = auto()

class Card(NamedTuple): #Card classı içine alarak bir kart fiziksel olarak oluşmuş olur.
    rank: Rank
    suit: Suit
    def __repr__(self) -> str:
        """Pretty-print the name of the card, e.g. 'Queen of Hearts'"""
        return f"{self.rank.name.title()} of {self.suit.name.title()}"





deck = [Card(rank, suit) for rank, suit in product(Rank, Suit)] #Cartesian product of input iterables. Tanımlanmış kartların altyapısı burda bir liste dönüşür ve böylece deste tamamlanmış olur.
print("Here's our deck fresh from the factory: ", deck)
shuffle(deck)
print("Here it is all shuffled: ", deck)



def best_value(hand: List[Card]) -> int:
    """Get the best blackjack value for a hand of cards (highest without busting)"""
    value = sum([card.rank.value for card in hand])
    if value < 12 and any([card.rank == Rank.ACE for card in hand]):
        # Count one of our aces as 11, adding 10 to the total.
        value += 10
    return value


print("Deal me two!")
hand = [deck.pop(), deck.pop()]
hand_op = [deck.pop(), deck.pop()]
print(f"My hand is {hand}, which is worth {best_value(hand)}")
print(f"Opponent has: {hand_op} = {best_value(hand_op)}")

# PROBLEMLER!!!!
# opponent kart aldıktan sonra kazanma senaryo eksik   
# 11'den ufakken as 11 geldi 
# 1. ben kart aldım 19-16 oldu, 2.stand dedim opponent kart aldı 19-18 oldu you win!! dedi ve bana hit or stand sordu.
#HERŞEY BİTİNCE VEYA ÖNCEDEN WORKFLOWA GEÇİR 

def Vault(): # Sit table with the money you want and bet
    your_money = 0       
    your_bet = 0     
    ask_sit = int(input("sit with: ")) 
    your_money += ask_sit        
    ask_bet = int(input("bet with: "))      
    your_bet = ask_bet       
    iscond = 0
    main()
    if iscond ==True:
                your_money += your_bet
                print(your_money)
    if iscond==False:
        your_money -= your_bet
        print(your_money)
    if iscond == 0 :
        pass
    



def main():
    
    if best_value(hand) == 21 :
        print("Won <line 75>!!")
        iscond = True
      
    if best_value(hand_op) == 21 :
        print("Opponent wins!!")
        iscond = False
        
    choice = int(input("Hit or Stand (HIT:1, STAND: 2): "))
    
    if choice == 2: #OPPONENT
        while best_value(hand_op) < 17: #Dealer 17'ye kadar kart çeker sonra sıra bize gelir eğer bir gün mp yaparsan sıra bekleyen olarak anla       
            print("Opponent says: Hit me!")
            card = deck.pop()
            hand_op.append(card)
            print("Opponent got ", card)
            
            if best_value(hand_op)==best_value(hand):
                print("DRAW!")
                iscond = 0
            """
            if best_value(hand_op) == 21 :
                print("Won!! <line 91>")
            """
        
        if  best_value(hand)<21 and best_value(hand_op)<best_value(hand):
            print("YOU WİN!!!")
            print(f"My hand was {hand}, which is worth {best_value(hand)}")
            print(f"Opponent had: {hand_op} = {best_value(hand_op)}")
            iscond = True
        if best_value(hand_op)<21 and (best_value(hand)<best_value(hand_op)):
            print("OPPONENT WİNS!!")
            print(f"Opponent had: {hand_op} = {best_value(hand_op)}")
            iscond = False
    

    if choice == 1: #YOUR NEXT PICK
        if best_value(hand) < 21: 
                print("You Say: Hit me!")
                card = deck.pop()
                hand.append(card)
                print("I got ", card)
                print(f"You have: {hand} = {best_value(hand)}")
                print(f"Opponent has: {hand_op} = {best_value(hand_op)}")
                if best_value(hand)<21 and best_value(hand) < best_value(hand_op):
                    main()
                if best_value(hand)<21 and best_value(hand) > best_value(hand_op):
                    main()
                
        """
        if best_value(hand) == 21 :
            print("Won!! <line 121>")
            main()
        if best_value(hand) > 21:
            print("YOU LOSE LINE 108 HAND >21")
        """
            
   

        if best_value(hand_op) > 21:
            print("Opponent bust you won")
            iscond = True
        if best_value(hand) > 21:
            print("You Bust Opponent won!")
            print(f"{hand} = {best_value(hand)}")
            print(f"{hand_op} = {best_value(hand_op)}")
            iscond =False
    
    

Vault()



  













