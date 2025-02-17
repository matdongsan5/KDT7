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
                # print(Card(i,j))
                self.deck.append(Card(i,j))
        print('-'*50)                
        print(f"[GameDealer] 딜러가 가진 카드 수: {len(self.deck)}")
        # print(self.deck)
        for i in self.deck:
            card = Card(card_suit=i.suit,card_number=i.number)
            if self.deck.index(i) % 13 == 12:
                print(card)
            else:
                print(card, end=' ')
        print()


        print('[GameDealer] 카드 섞기')
        random.shuffle(self.deck) 
        print('-'*50)                
        print(f"[GameDealer] 딜러가 가진 카드 수: {len(self.deck)}")
        for i in self.deck:
            card = Card(card_suit=i.suit,card_number=i.number)
            if self.deck.index(i) % 13 == 12:
                print(card)
            else:
                print(card, end=' ')
        print()
        
        
    def distribute_card(self, num):
        
        distribute_list = list()
        for i in range(num):
            distribute_list.append(self.deck.pop())
        print(f'[GameDealer] 카드 나누어주기: {num}장')
        print('-'*50)                
        print(f"[GameDealer] 딜러가 가진 카드 수: {len(self.deck)}")
        for i in self.deck:
            card = Card(card_suit=i.suit,card_number=i.number)
            if self.deck.index(i) % 13 == 12:
                print(card)
            else:
                print(card, end=' ')
            
        print()
        return distribute_list
        

# dealer = GameDealer()

# dealer.make_deck()
