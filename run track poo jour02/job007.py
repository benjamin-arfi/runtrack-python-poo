import random

suits = ('coeur', 'carreau', 'pique', 'trefle')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Rene', 'Roi', 'As')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Valet':10,
         'Rene':10, 'Roi':10, 'As':11}

playing = True



class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' de ' + self.suit



class Deck:
    
    def __init__(self):
        self.deck = []  
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        deck_comp = '' 
        for card in self.deck:
            deck_comp += '\n' + card.__str__() 
        return 'The deck has' + deck_comp
            
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card



class Hand:
    def __init__(self):
        self.cards = []  
        self.value = 0   
        self.aces = 0    
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'As':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            
          



def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()



def hit_or_stand(deck,hand):
    global playing
    
    while True:
        x = input("voulez vous piocher ou garder? Entrer 'p' ou 'g'")
        
        if x[0].lower() == 'p':
            hit(deck,hand) 

        elif x[0].lower() == 'g':
            print("Player garde. Dealer joue.")
            playing = False

        else:
            print("reesaye")
            continue
        break


def show_some(player,dealer):
    print("\nmain du dealer")
    print("<carte cacher>")
    print(' ', dealer.cards[1])
    print("\nmain du joueur: ", *player.cards, sep= '\n')
        
def show_all(player,dealer):
    print("\nmain du dealer:", *dealer.cards, sep="\n")
    print("main du dealer =",dealer.value)
    print("\nmain du joeur: ", *player.cards, sep= '\n')
    print("main du joeur = ", player.value)
  


while True:
    
    print("Welcome Blackjack game.")
    
    
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    
    show_some(player_hand, dealer_hand)
    
    while playing:  
        
        
        hit_or_stand(deck, player_hand)
        
        
        show_some(player_hand,dealer_hand) 
        
        
        if player_hand.value >21:
            player_busts(player_hand, dealer_hand, )

            break

    
    if player_hand.value <= 21:
        
        while dealer_hand.value <17:
            hit(deck, dealer_hand)
    
        
        show_all(player_hand,dealer_hand)
        
        
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand)

        else:
            push(player_hand,dealer_hand)
        
    
    
    print("\nPlayers winnings stand at", player_chips.total)
    
    
    new_game = input("would you like to play again? Enter 'y' or 'n'")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thanks for playing! ')

        break