import random

def select_cards(possible_cards, hand):
    i = 0 
    while i < 3: 
        card = random.choice(possible_cards)
        print("Do you want to pick up {}?".format(card))
        answer = input()
        if answer == 'y': 
            hand.append(card)
            i+=1 
        else: 
            hand.append(random.choice(possible_cards)) 
            i += 1 
    return hand


available_cards = ['queen of spades', '2 of clubs', '3 of diamonds', 'jack of spades', 'queen of hearts']

new_hand = select_cards(available_cards, [])

display_hand = "\n".join(new_hand)

print("Your new hand is: \n{}".format(display_hand))

