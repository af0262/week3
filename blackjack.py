# This program plays a blackjack
# step 1
    # Shuflle the Deck
    # Deal two cards to the player
    # ask the player if they want more cards
    # provide the player cards until they say no or untill they they go over 21
    # When player says no, the dealer is given two cards
    # provide dealer cards untill the reach 17

import random
import time

suits = 'S H C D'
cards = "A 2 3 4 5 6 7 8 9 10 J Q K"
#card_value = {'A':11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}
#deck=list(card_value.items())

card=(cards.split())
suit=(suits.split())

deck = []
for s in suit:
    for c in card:
        deck.append(c + ' ' + 'of' + ' ' + s)

    random.shuffle(deck) 

##print(deck)

def score(hands):
  total = 0
  for hand in hands:
    c = hand[:-5]
    if c in ['J', 'Q', 'K']:
       point=10
    elif c == 'A':
      point = 11
    else:
      point = int(c)
    total = total+point
  return total

play = [deck.pop(0),deck.pop(0)]
total_score = score(play)

print ("Your Cards are:",(play))
print ("Your Cards are:",total_score)

while total_score < 21 and input("Do you want another card? (y/n) ") == 'y':
  play.append(deck.pop(0))
  total_score = score(play)
  print("Your hand:", ", ",(play))

if total_score > 21:
  print("You're Done!")
elif total_score == 21:
  print("You win!")
else:
  print("Your score is:",total_score)
  print()
  dealer_hand = [deck.pop(0), deck.pop(0)]
  dealer_score = score(dealer_hand)
  print("Dealer has", " ",(dealer_hand))

while dealer_score < 17:
    print("The dealer will take another card...")
    #time.sleep(5)
    dealer_hand.append(deck.pop(0))
    dealer_score = score(dealer_hand)
    print("Dealer now has", " ",(dealer_hand))
    #time.sleep(3)

if dealer_score > 21:
    print("The dealer busted! You win!")
elif dealer_score == 21:
    print("The dealer got 21! You lose.")
elif dealer_score > total_score:
    print("You lost.")
elif dealer_score == total_score:
    print("It's a tie.... nobody wins this time.")
else:
    print("You win!")

