import sys
import random

cards = {
    0: ['Ace', 15],
    1: ['2', 2],
    2: ['3', 3],
    3: ['4', 4],
    4: ['5', 5],
    5: ['6', 6],
    6: ['7', 7],
    7: ['8', 8],
    8: ['9', 9],
    9: ['10', 10],
    10: ['Jack', 12],
    11: ['Queen', 13],
    12: ['King', 14]
}

suits = {
    0: ['♣'],
    1: ['♦'],
    2: ['♥'],
    3: ['♠']
}

mvmts = {}

def output(card_t):
	print(f"You draw {card_t[1][0]} of {card_t[0][0]}")
	print(f"do {card_t[1][1]} {card_t[0][1]}")

def shuffle(deck):
	for i in deck:
		yield i

def draw_cards(num_of_cards, my_deck=[]):
    for z in range(num_of_cards):
        x = random.randint(0,3)
        y = random.randint(0,12)
        if len(my_deck) == 52 or num_of_cards == 0:
            print("The deck is empty")
            return my_deck
        card = (suits[x], cards[y], suits[1])
        if card not in my_deck:
            my_deck.append(card)
        else:
            num_of_cards = num_of_cards - z
            return draw_cards(num_of_cards, my_deck)
            
    return my_deck

if __name__ == '__main__':
	heart = input("Please enter exercice for Hearts ♥ : ")
	suits[0].append(heart)
	spades = input("Please enter exercice for Spades ♠ : ")
	suits[1].append(spades)
	diamonds = input("Please enter exercice for Diamonds ♦ : ")
	suits[2].append(diamonds)
	club = input("Please enter exercice for Club ♣ : ")
	suits[3].append(club)
	card_nb = int(input("Please enter number of cards you wanna play :"))
	#BOUCLE FOR
	print(suits)
	my_deck = draw_cards(card_nb)
	for card in my_deck:
		output(card)
		input_ret = input("Press any key for next card")
		if input_ret == "quit":
			quit()