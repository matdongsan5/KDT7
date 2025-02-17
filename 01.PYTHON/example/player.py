class Player:
    def __init__(self,name):
        self.name = name
        self.holding_card_list = list()
        self.open_card_list = list()
        
    def add_card_list(self, card_list):
        self.holding_card_list += card_list
        return self.name.display_two_card_lists()
        
    def display_two_card_lists(self):
        print('='*50)
        print(f"[{self}] Open card List: {len(self.open_card_list)}")
        print()
        print(f"[{self}] Holding card List: {len(self.holding_card_list)}")
        for i in self.holding_card_list:#['♠', '♥', '♣', '◆']
            if i.suit == '♣':
                print(f"\033[34m {i}\033[0m" ,end =' ')
            elif i.suit == '◆':
                print(f"\033[31m {i}\033[0m" ,end =' ')
            elif i.suit == '♥':
                print(f"\033[35m {i}\033[0m" ,end =' ')
            else:
                print(f"{i}", end=' ')
            
        print('\n')
        
    def check_one_pair_card(self):
        pass
    
    