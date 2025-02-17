from card import Card
import random

class GameDealer:
    def __init__(self):
        self.deck = list()
        self.suit_number = 13
        
    def make_deck(self):
        print('[GameDealer] 초기 카드 생성')

        card_suits = ['♠', '♥', '♣', '◆']
        card_numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for i in card_suits:
            for j in card_numbers:
                self.deck.append(Card(i,j))
        print('-'*50)                
        print(f"[GameDealer] 딜러가 가진 카드 수: {len(self.deck)}")
        for i in self.deck:
            card = Card(i[0],i[1])
            print(card)
        


        print('[GameDealer] 카드 섞기')
        random.suffle(self.deck)
        print('-'*50)                
        print(f"[GameDealer] 딜러가 가진 카드 수: {len(self.deck)}")
        
        
        
    def distribute_card(self, num):
        pass
    

dealer = GameDealer()

dealer.make_deck()
