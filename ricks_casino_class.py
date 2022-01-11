# Rick's Casino
import random
# variable for games
suits = ('♥', '♦', '♠', '♣')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
          '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11} # assing rank to value in dict
numbers_roulrtte = {'00': ['g', None], '0': ['g', None], '1': ['r', 'o'], '2': ['b', 'e'], '3': ['r', 'o'],
                    '4': ['b', 'e'], '5': ['r', 'o'], '6': ['b', 'e'], '7': ['r', 'o'], '8': ['b', 'e'],
                    '9': ['r', 'o'], '10': ['b', 'e'], '11': ['b', 'o'], '12': ['r', 'e'], '13': ['b', 'o'],
                    '14': ['r', 'e'], '15': ['b', 'o'], '16': ['r', 'e'], '17': ['b', 'o'], '18': ['r', 'e'],
                    '19': ['r', 'o'], '20': ['b', 'e'], '21': ['r', 'o'], '22': ['b', 'e'], '23': ['r', 'o'],
                    '24': ['b', 'e'], '25': ['r', 'o'], '26': ['b', 'e'], '27': ['r', 'o'], '28': ['b', 'e'],
                    '29': ['b', 'o'], '30': ['r', 'e'], '31': ['b', 'o'], '32': ['r', 'e'], '33': ['b', 'o'],
                    '34': ['r', 'e'], '35': ['b', 'o'], '36': ['r', 'e']} # Dict of numbers and there attribute
Slot_Reel = ['♥', '♦', '♠', '♣', '♥', '♦', '♠', '♣', '♥', '♦', '♠', '♣', '♥', '♦', '♠', '♣', '7']
letter_to_color = {'b': 'Black', 'r': 'Red', 'g': 'Green'}
# Games explanation (how to play)
slot_key = 'Welcome to  Roy\'s slot machine (please don\'t go bird watching) ' \
           '\n The BIGGEST prise is for 7,7,7 and you will get 1,000,000 Shmekels' \
           '\n for 3-of-a-kind (any other then 7) you will get five times your bet $_$ ' \
           '\n for 2-of-a-kind of 7 you will get X10 your bet (this will get you out of the carpet store)' \
           '\n for any other 2-of-a-kind you get what you bet... ' \
           '\n Please din\'t feed the Roy!!! and good luck  '
blackjack_key = '\nWelcome to BirdPerson Blackjack!!! \n At the start of the game you get 2 cards The goal is to get to a sum of 21, 2-10 worth their value,' \
                '\nall the royal family worth 10 and Ace worth 11 or 1 . \nAfter you get 2 card you can stay or take extra card.\nIf you get 21 on first 2 cards you win automaticly (double your bet) .' \
                '\nIf go over 21 you lose, if you stay its the dealer turn ,dealer will take cards until 17 or higher.' \
                '\nIf you win you get your what you bet .\nif you lose birdPerson will tour in to phoenixPerson so don\'t lose!!!  '
roulette_key = '\nWelcome to Summer\'s roulette!!' \
               '\nYou need guss what number summer is thinking about between 00 - 36 if you guss it you will get x7 your bet and summer love.' \
               '\nYou can also pick a color for Red/black to get your bet in winning or Green for x4.' \
               '\nAnd last you can bet on Odd/Even to get your bet in winning/' \
               '\nSummer is filling nice so you place bet on every thing you want in the round .' \
               '\nMay the Summer be ever  in your favor '

# Card handle the suits and ranks to bring you a card with suit & rank
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + '\t of ' + self.suit

# Handle the deck souffle the cards and remove cards from deck
class Deck:
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n ' + card.__str__()  # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)  # shuffle main deck

    def deal(self):
        single_card = self.deck.pop()  # remove card from main deck
        return single_card

# assigning hand to player/dealer add a card and hide dealer's first card from player
class Hand:
    def __init__(self, name, deck):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces
        self.name = name
        self.add_card(deck.deal())
        self.add_card(deck.deal())

    def __str__(self):
        cards = ', '.join([str(_) for _ in self.cards])
        return f'{self.name} cards: {cards} and their value is : {self.value}'

    def hide_first_card(self):
        cards = ', '.join([str(_) for _ in self.cards[1:]])
        return f'{self.name} cards: *\tof *, {cards}'

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'A':
            self.aces += 1

        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# ask the player if to stay or take
def ask_take(deck, hand):  # player take or saty function
    while True:
        x = input('would you like to take or stay? please enter "t" to take or "s" to stay: ')
        if x and x[0].lower() == 't':
            hand.add_card(deck.deal())
            print(hand)
            return True
        elif x and x[0].lower() == 's':
            print('Player is staying ,dealer turn  ')
            return False

        else:
            print('WTF enter only "t" or "s" are you dumb? try again  ')
            continue

# Random a number between 00-36 for the roulette game
def get_roulette_number():
    return random.choice(list(numbers_roulrtte.keys()))

# Because of the multi-bet need to stock the wining and losing to give a total of your result
def calc_result_roulette(all_bets, number):
    delta = 0

    for bet in all_bets['number_bets']:
        if number == bet[0]:
            delta += 6 * bet[1]
        else:
            delta -= bet[1]
    for bet_coler in all_bets['coler_bets']:
        if numbers_roulrtte[number][0] == bet_coler[0] and numbers_roulrtte[number][0] != 'g':
            delta += bet_coler[1]
        elif numbers_roulrtte[number][0] == bet_coler[0] and numbers_roulrtte[number][0] == 'g':
            delta += 3 * bet_coler[1]
        else:
            delta -= bet_coler[1]
    for bet_oddeven in all_bets['oddeven_bets']:
        if bet_oddeven[0] == numbers_roulrtte[number][1]:
            delta += bet_oddeven[1]
        else:
            delta -= bet_oddeven[1]
    return delta


# Bring the player the slot machine result one reel at a time for the drama
def spin_reel():
    all_result = []
    for i in range(3):
        result = random.choice(Slot_Reel)
        print(f'\nthe {i + 1} spin is :.....[ {result} ]!!\n ')
        if i < 2:
            input('press any key for the next one')
        all_result.append(result)
    print(f'The result {all_result}')
    return all_result


class Casino:
    def __init__(self):
        self.total = random.randint(5, 50) * 10
        self.bet = 0
        self.roulette_numbers_history = []
        self.slot_history = []

    def play_casino(self):
        print('Wolcome to Rick casino we only acept Shmekels !  ')
        print(f'You been given {self.total} Shmekels by the grease of all powerful Rick 137  \nUse them wisely... \n')
        bj_flag = 0
        while self.total > 0:
            print(f'\n\nyou got {self.total} Shmekels in your Shmekels bag ')

            pick_game = input(
                f'\nPlease pick:\n(B)BirdPorsen Bleckjack\n(R)Summer\'s Roulette\n(S) Roy\'s Slot machine\n(Q)Quit \nPick now: : ')
            if pick_game.lower() == 'b':
                self.black_jack(bj_flag)
                bj_flag += 1
            elif pick_game.lower() == 'r':
                self.roulette()
            elif pick_game.lower() == 's':
                self.slot_machine()
            elif pick_game.lower() == 'q':
                break
            else:
                print(f' {pick_game} is not one of the choices please pick right this time!!')
        if self.total <= 0:
            print('\ndon\'t ever and we mean ever come back here with out Shmekels!! $_$ ')

    def black_jack(self, bj_flag):
        if bj_flag == 0:
            print(blackjack_key)
        else:
            print('Welcome to BirdPerson Blackjack again :)')
        self.take_bet()
        deck = Deck()
        deck.shuffle()
        dealer_hand = Hand('Dealer', deck)
        player_hand = Hand('Player', deck)

        print(dealer_hand.hide_first_card())
        print(player_hand)

        if player_hand.value == 21:
            print(f'Congrats you got black jack you\'re so gooood and you double your bet so you won {self.bet * 2} ')
            self.total += self.bet * 2
            return
        take = True
        while take:
            take = ask_take(deck, player_hand)
            if player_hand.value > 21:
                print(f'you are a loser why did you take another card?!!? ,you lost {self.bet} ')
                self.total -= self.bet
                return
        while dealer_hand.value <= 16:
            dealer_hand.add_card(deck.deal())
            input(f'{dealer_hand} , press enter to continue')
        print(f'\n\n{player_hand}')
        print(dealer_hand)

        if dealer_hand.value > 21:
            print(f'Congrats you  WON!! now it was skill!! ,you won  {self.bet} ')
            self.total += self.bet
            return
        if player_hand.value > dealer_hand.value:
            print(f'Congrats you  WON!! now that was skill!! ,you won  {self.bet} ')
            self.total += self.bet
            return
        elif player_hand.value == dealer_hand.value:
            print(
                'You\'re both equally bad. And I honestly can\'t even tell the two of you apart half the time,\nBecause I don\'t go by height or age, I go by suckiness,\nwhich makes you both identical. oh and you didnt lose any shmekels this time')
            return
        else:
            print(f'you are a loser this is so sed go cry to Mammy , you lost {self.bet} ')
            self.total -= self.bet
            return

    def take_bet(self):
        while True:
            try:
                self.bet = int(input('\nHow much Shmekels do you want to bet on this round? '))
            except ValueError:
                print('sorry,you need to bet an integer(a whole number)')
            else:
                if self.bet > self.total:
                    print('Sorry you don''t have the Shmekels to make this bet  ')
                else:
                    break

    def roulette(self):
        history = '\n'.join(self.roulette_numbers_history)
        if len(self.roulette_numbers_history) > 0:
            print(f'\nthe Roulette numbers history is: \n{history} ')
        else:
            print(roulette_key)
        bets = self.take_roulette_bet()
        winning_number = get_roulette_number()
        self.roulette_numbers_history.append(
            '[' + winning_number + ',\t' + letter_to_color[numbers_roulrtte[winning_number][0]] + ']')
        print(f'the number is {winning_number} and the color is {letter_to_color[numbers_roulrtte[winning_number][0]]}')
        delta_shmekels = calc_result_roulette(bets, winning_number)
        print(f'\nthis round you "win" {delta_shmekels}')
        self.total += delta_shmekels
        print('thanks for playing roulette don\'t ever come back with out bird man')

    def take_roulette_bet(self):
        bets = {'number_bets': [], 'coler_bets': [], 'oddeven_bets': []}
        remaining_chips = self.total
        while 0 < remaining_chips:
            print(f'You got {remaining_chips} Shmekels to bet... use it wisely ')
            pick_bet = input(
                'Do you want to bet on a (N)Number (C)Color or (E)EvenOdd ? if you done beting press enter ')
            if pick_bet.lower() == 'n':
                while True:
                    number = input('\nplease pick a number between 0-36(or 00 ) :  ')
                    if number not in numbers_roulrtte:
                        print(f'no no no {number} is not in the limits :(  are you dumb or stupid? try again')
                        continue
                    else:
                        break
                while True:
                    single_bet = int(input(f'\nplease enter the amount you want to put on {number} : '))
                    if single_bet > remaining_chips:
                        print(
                            f'no no no {single_bet} is not in the limits of your Shmekels :(  are you dumb or stupid? try again')
                        continue
                    else:
                        break
                remaining_chips -= single_bet
                bets['number_bets'].append([number, single_bet])
            elif pick_bet.lower() == 'c':
                while True:
                    color_index = input('\nplease pick a color between (B)Black , (R)Red or (G)Green :  ')
                    if color_index.lower() != 'b' and color_index.lower() != 'r' and color_index.lower() != 'g':
                        print(
                            f'No no no {color_index} is not one of the color_index :(  are you dumb or stupid? try again')
                        continue
                    else:
                        break
                while True:
                    single_bet = int(
                        input(
                            f'\nPlease enter the amount you want to put on this color with color_index {color_index} : '))
                    if single_bet > remaining_chips:
                        print(
                            f'No no no {single_bet} is not in the limits of your Shmekels :(  are you dumb or stupid? try again')
                        continue
                    else:
                        break
                remaining_chips -= single_bet
                bets['coler_bets'].append([color_index.lower(), single_bet])
            elif pick_bet.lower() == 'e':
                while True:
                    oddeven = input('\nplease pick (O)Odd  or (E)Even :  ')
                    if oddeven.lower() != 'e' and oddeven.lower() != 'o':
                        print(f'No no no {oddeven} is not one of the choices :(  are you dumb or stupid? try again')
                        continue
                    else:
                        break
                while True:
                    single_bet = int(
                        input(f'\nPlease enter the amount you want to put on OddEven with the index {oddeven} : '))
                    if single_bet > remaining_chips:
                        print(
                            f'No no no {single_bet} is not in the limits of your Shmekels :(  are you dumb or stupid? try again')
                        continue
                    else:
                        break
                remaining_chips -= single_bet
                bets['oddeven_bets'].append([oddeven.lower(), single_bet])
            else:
                break
        return bets

    def slot_machine(self):
        if not self.slot_history:
            print(f'\n{slot_key}\n')
        else:
            print(f'Results history: {self.slot_history}')
        self.take_bet()
        results = spin_reel()
        self.slot_history.append(results)
        self.calc_result_slot(results)

    def calc_result_slot( self, results):
        counts = {'♥': 0, '♦': 0, '♠': 0, '♣': 0, '7': 0}
        win_str = f'you are a loser!! and your fired'
        self.total -= self.bet
        for shipe in results:
            counts[shipe] += 1
        for shipe, count in counts.items():
            if count == 3 and shipe == '7':
                self.total += 1000000
                print(f'WoW that\'s a GOD level luck you don\'t need science when you got a million Shmekels')
            elif count == 3 and shipe != '7':
                self.total += self.bet * 5
                win_str = f'You won 3-of-a-kind now maybe you can buy a life '
            elif count == 2 and shipe == '7':
                self.total += self.bet * 10
                win_str = f'You lucky dog now you bet 10 times it size  '
            elif count == 2 and shipe != '7':
                self.total += self.bet * 2
                win_str = f'You are very mediocre person take your Shmekels and go  '
        print(win_str)

c = Casino()
c.play_casino()
