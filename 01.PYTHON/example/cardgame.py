from card import Card
from player import Player
from gamedealer import GameDealer


def play_game():
    # 두 명의 플레이어 객체 생성
    player1 = Player('alpha')
    player2 = Player('beta')
    
    dealer = GameDealer()
    dealer.make_deck()
    player1.add_card_list(dealer.distribute_card(10))
    player2.add_card_list(dealer.distribute_card(10))
    
    
if __name__ == '__main__':
    play_game()
    
    
    
play_game()
