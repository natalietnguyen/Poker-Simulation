#  File: Poker.py

#  Description: Play a game of poker!

#  Student's Name: Natalie Nguyen

#  Student's UT EID: ntn687

#  Partner's Name: Ethan Harris

#  Partner's UT EID: ejh2947

#  Course Name: CS 313E 

#  Unique Number: 52038

#  Date Created: 6 February, 2023

#  Date Last Modified: 12 February, 2023


import sys
import random

# creates a Card object
class Card (object):
    #intializes the ranks
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

    # initializes the suits
    SUITS = ('C', 'D', 'H', 'S')

    # constructor 
    def __init__ (self, rank = 12, suit = 'S'):
        if (rank in Card.RANKS):
            self.rank = rank
        else:
            self.rank = 12

        if (suit in Card.SUITS):
            self.suit = suit
        else:
            self.suit = 'S'

    # string representation of a Card object
    def __str__ (self):
        if (self.rank == 14):
            rank =  'A'
        elif (self.rank == 13):
            rank = 'K'
        elif (self.rank == 12):
            rank = 'Q'
        elif (self.rank == 11):
            rank = 'J'
        else:
            rank = str(self.rank)

        return rank + self.suit

    # equality tests
    def __eq__ (self, other):
        return self.rank == other.rank

    def __ne__ (self, other):
        return self.rank != other.rank

    def __lt__ (self, other):
        return self.rank < other.rank

    def __le__ (self, other):
        return self.rank <= other.rank

    def __gt__ (self, other):
        return self.rank > other.rank

    def __ge__ (self, other):
        return self.rank >= other.rank

# creates a Deck object
class Deck (object):
    # constructor
    def __init__ (self, num_decks = 1):
        self.deck = []
        # creates a deck of cards
        for i in range(num_decks):
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    card = Card(rank, suit)
                    self.deck.append(card)

    # shuffle the deck
    def shuffle (self):
        random.shuffle(self.deck)

    # deal a card
    def deal (self):
        if (len(self.deck) == 0):
            return None
        else:
            return self.deck.pop(0)

# creates a Poker object
class Poker (object):
    # constructor
    def __init__ (self, num_players = 2, num_cards = 5):
        self.deck = Deck()
        self.deck.shuffle()
        self.players_hands = []
        self.numCards_in_Hand = num_cards

        # deal all the cards
        for i in range(num_players):
            hand = []
            for j in range(self.numCards_in_Hand):
                hand.append(self.deck.deal())
            self.players_hands.append(hand)

    # simulate the play of the game
    def play (self):
        # sort the hands of each player and print
        for i in range(len(self.players_hands)):
            sorted_hand = sorted(self.players_hands[i], reverse = True)
            self.players_hands[i] = sorted_hand
            hand_str = ''
            for card in sorted_hand:
                hand_str = hand_str + str(card) + ' '
            print('Player ' + str(i + 1) + ' : ' + hand_str)

        # determine the type of each hand and print
        hand_type = []	# create a list to store type of hand
        hand_points = []	# create a list to store points for hand

        # initializes the current player's hand type and hand points
        current_hand_type = ''
        current_hand_points = 0

        # checks each player's hand for the type of hand they have
        for hand in self.players_hands:
            current_hand_points, current_hand_type = self.is_royal(hand)
            if current_hand_type != '' and current_hand_points != 0:
                hand_type.append(current_hand_type)
                hand_points.append(current_hand_points)
                current_hand_type = ''
                current_hand_points = 0
                continue

            current_hand_points, current_hand_type = self.is_straight_flush(hand)
            if current_hand_type != '' and current_hand_points != 0:
                hand_type.append(current_hand_type)
                hand_points.append(current_hand_points)
                current_hand_type = ''
                current_hand_points = 0
                continue

            current_hand_points, current_hand_type = self.is_four_kind(hand)
            if current_hand_type != '' and current_hand_points != 0:
                hand_type.append(current_hand_type)
                hand_points.append(current_hand_points)
                current_hand_type = ''
                current_hand_points = 0
                continue
            
            current_hand_points, current_hand_type = self.is_full_house(hand)
            if current_hand_type != '' and current_hand_points != 0:
                hand_type.append(current_hand_type)
                hand_points.append(current_hand_points)
                current_hand_type = ''
                current_hand_points = 0
                continue
            
            current_hand_points, current_hand_type = self.is_flush(hand)
            if current_hand_type != '' and current_hand_points != 0:
                hand_type.append(current_hand_type)
                hand_points.append(current_hand_points)
                current_hand_type = ''
                current_hand_points = 0
                continue
            
            current_hand_points, current_hand_type = self.is_straight(hand)
            if current_hand_type != '' and current_hand_points != 0:
                hand_type.append(current_hand_type)
                hand_points.append(current_hand_points)
                current_hand_type = ''
                current_hand_points = 0
                continue
            
            current_hand_points, current_hand_type = self.is_three_kind(hand)
            if current_hand_type != '' and current_hand_points != 0:
                hand_type.append(current_hand_type)
                hand_points.append(current_hand_points)
                current_hand_type = ''
                current_hand_points = 0
                continue
            
            current_hand_points, current_hand_type = self.is_two_pair(hand)
            if current_hand_type != '' and current_hand_points != 0:
                hand_type.append(current_hand_type)
                hand_points.append(current_hand_points)
                current_hand_type = ''
                current_hand_points = 0
                continue
            
            current_hand_points, current_hand_type = self.is_one_pair(hand)
            if current_hand_type != '' and current_hand_points != 0:
                hand_type.append(current_hand_type)
                hand_points.append(current_hand_points)
                current_hand_type = ''
                current_hand_points = 0
                continue
            
            current_hand_points, current_hand_type = self.is_high_card(hand)
            if current_hand_type != '' and current_hand_points != 0:
                hand_type.append(current_hand_type)
                hand_points.append(current_hand_points)
                current_hand_type = ''
                current_hand_points = 0
                continue    
        
        print()
        # prints each player's hand type
        for i in range(len(self.players_hands)):
            print('Player ' + str(i + 1) + ': ' + hand_type[i])

        # determine the winner and print

        # finds hand with the max points
        max_points = max(hand_points)
        # creates a list of winners
        winner = []
        # creates the winner's hand type
        winner_type = ''

        # adds winner with the most points to winner list
        winner.append(hand_points.index(max_points))
        # finds the winner's hand type
        winner_type = hand_type[winner[0]]
        
        # iterates through the players' hand types
        for i in range(len(hand_type)):
            # checks if other players have the same hand type as the winner's hand type
            if hand_type[i] == winner_type:
                if i not in winner:
                    winner.append(i)
        
        # creates a dictionary of players with the same hand and maps it to their amount of points
        tied_dict = {}
        # checks if there are multiple winners
        if len(winner) != 1:
            for index in winner:
                tied_dict[index] = hand_points[index]

        # sorts the tied_dict from highest to lowest based on amount of points
        tied_dict = dict(sorted(tied_dict.items(),reverse = True, key = lambda x: x[1]))
        
        # prints winners/ties
        if len(winner) == 1:
            print()
            print('Player ' + str(winner[0] + 1) + ' wins.')
        else:
            print()
            for player in tied_dict.keys():
                print('Player ' + str(player + 1) + ' ties.')

    # determine if a hand is a royal flush
    # takes as argument a list of 5 Card objects
    # returns a number of points for that hand
    def is_royal (self, hand):
        # creates variable indicating if all cards are the same suit
        same_suit = True
        # checks if all cards are the same suit
        for i in range(len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        # returns no points and no hand type if all cards are not the same suit
        if (not same_suit):
            return 0, ''
        
        # creates variable indicating if all cards are in order from 10 to ace
        rank_order = True
        # checks if all cards are in order from 10 to ace
        for i in range (len(hand)):
            rank_order = rank_order and (hand[i].rank == 14 - i)

        # returns no points and no hand type if cards are not in order from 10 to ace
        if (not rank_order):
            return 0, ''

        # determine the points
        points = 10 * 15**5 + (hand[0].rank) * 15**4 + (hand[1].rank) * 15**3 \
                 + (hand[2].rank) * 15**2 + (hand[3].rank) * 15**1 + (hand[4].rank)

        # returns the points and hand type
        return points, 'Royal Flush'

    # determine if a hand is a straight flush
    # takes as argument a list of 5 Card objects
    # returns a number of points for that hand
    def is_straight_flush (self, hand):
        # creates variable indicating if all cards are the same suit
        same_suit = True
        # creates a list of ranks if ace counts as one
        straight_exception = [2, 3, 4, 5, 14]
        # creates a list of ranks in hand 
        ranks = []

        # adds each rank of each card to ranks
        for i in range(len(hand)):
            ranks.append(hand[i].rank)
        
        # checks if list of ranks fits the exception
        if ranks == straight_exception:
            rank_order = True

        # checks if all cards are the same suit
        for i in range(len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        # returns no points and no hand type if all cards are not the same suit
        if (not same_suit):
            return 0, ''
        
        # creates variable indicating if all cards are in order from one to king
        rank_order = True
        # creates variable indicating if all cards are in order from one to king
        for i in range (len(hand) - 1):
            rank_order = rank_order and (hand[i].rank - 1 == hand[i + 1].rank)

        # returns no points and no hand type if cards are not in order from 10 to ace
        if (not rank_order):
            return 0, ''
        
        # determines the number of points
        points = 9 * 15**5 + (hand[0].rank) * 15**4 + (hand[1].rank) * 15**3 \
                 + (hand[2].rank) * 15**2 + (hand[3].rank) * 15**1 + (hand[4].rank)

        # returns the points and hand type
        return points, 'Straight Flush'

    # determine if a hand is a four of a kind
    # takes as argument a list of 5 Card objects
    # returns a number of points for that hand
    def is_four_kind (self, hand):
        # creates a card dictionary
        card_dict = {}
        # creates variable indicating if there is a four of a kind
        four_kind = False

        # iterates through the player's hand
        for i in range (len(hand)):
            # counts the number of times a rank shows up
            if hand[i].rank in card_dict.keys():
                card_dict[hand[i].rank] += 1
            else:
                card_dict[hand[i].rank] = 1

        # iterates through each rank in card_dict
        for rank in card_dict.keys():
            # tests if a rank shows up four times
            if card_dict[rank] == 4:
                four_kind = True
                break

        # returns no points and no hand type if there is not four of a kind
        if not(four_kind):
            return 0, ''

        # creates variable indicating rank of card with four of a kind
        four_kind_rank = 0
        # creates variable indicating rank of other card
        other_card = 0

        # iterates through ranks in card_dict
        for rank in card_dict.keys():
            # assigns ranks to four_kind_rank and other_card
            if card_dict[rank] == 4:
                four_kind_rank = rank
            else:
                other_card = rank

        # determines the number of points
        points = 8 * 15**5 + (four_kind_rank) * 15**4 + (four_kind_rank) * 15**3 \
                 + (four_kind_rank) * 15**2 + (four_kind_rank) * 15**1 + (other_card)

        # returns the points and hand type
        return points, 'Four of a Kind'

    # determine if a hand is a full house
    # takes as argument a list of 5 Card objects
    # returns a number of points for that hand
    def is_full_house (self, hand):
        # creates a card dictionary
        card_dict = {}
        # creates a variable indicating if there is a full house
        full_house = False
        
        # iterates through the player's hand
        for i in range (len(hand)):
            # counts the number of times a rank shows up
            if hand[i].rank in card_dict.keys():
                card_dict[hand[i].rank] += 1
            else:
                card_dict[hand[i].rank] = 1

        # tests if there is a full house
        if len(card_dict) == 2:
            full_house = True

        # returns no points and no hand type if there is not a full house
        if (not full_house):
            return 0, ''
        
        # creates variable indicating rank of card with three of a kind
        three_kind = 0
        # creates variable indicating rank of card with pairs
        pair = 0

        # iterates through rank in card_dict
        for rank in card_dict:
            # assigns rank to three_kind and pair
            if card_dict[rank] == 3:
                three_kind = rank
            else:
                pair = rank

        # determines the number of points
        points = 7 * 15**5 + (three_kind) * 15**4 + (three_kind) * 15**3 \
                 + (three_kind) * 15**2 + (pair) * 15**1 + (pair)

        # returns the points and hand type
        return points, 'Full House'

    # determine if a hand is a flush
    # takes as argument a list of 5 Card objects
    # returns a number of points for that hand
    def is_flush (self, hand):
        # creates variable indicating if all cards are the same suit
        same_suit = True

        # iterates through player's hand
        for i in range(len(hand) - 1):
            # tests if all cards are the same suit
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        # returns no points and no hand type if there is not a full house
        if (not same_suit):
            return 0, ''

        # determines the number of points
        points = 6 * 15**5 + (hand[0].rank) * 15**4 + (hand[1].rank) * 15**3 \
                 + (hand[2].rank) * 15**2 + (hand[3].rank) * 15**1 + (hand[4].rank)

        # returns the points and hand type
        return points, 'Flush'

    # determine if a hand is a straight
    # takes as argument a list of 5 Card objects
    # returns a number of points for that hand
    def is_straight (self, hand):
        # creates variable indicating if all cards are in order from one to king
        rank_order = True
        # creates a list of ranks if ace counts as one
        straight_exception = [2, 3, 4, 5, 14]
        # creates a list of ranks in hand 
        ranks = []

        # adds each rank of each card to ranks
        for i in range(len(hand)):
            ranks.append(hand[i].rank)

        # checks if list of ranks fits the exception
        if ranks == straight_exception:
            rank_order = True

        # iterates through the player's hand
        for i in range (len(hand) - 1):
            # checks if cards are in order from one to king
            rank_order = rank_order and (hand[i].rank - 1 == hand[i + 1].rank)

        # returns no points and no hand type if there is not a straight
        if (not rank_order):
            return 0, ''
        
        # determines the number of points
        points = 5 * 15**5 + (hand[0].rank) * 15**4 + (hand[1].rank) * 15**3 \
                 + (hand[2].rank) * 15**2 + (hand[3].rank) * 15**1 + (hand[4].rank)
        
        # returns the points and hand type
        return points, 'Straight'

    # determine if a hand is a three of a kind
    # takes as argument a list of 5 Card objects
    # returns a number of points for that hand
    def is_three_kind (self, hand):
        # creates a card dictionary
        card_dict = {}
        # creates a variable indicating if there is three of a kind
        three_kind = False
        
        # iterates through the player's hand
        for i in range (len(hand)):
            # counts the number of times a rank shows up
            if hand[i].rank in card_dict.keys():
                card_dict[hand[i].rank] += 1
            else:
                card_dict[hand[i].rank] = 1

        # iterates through each rank in card_dict
        for rank in card_dict.keys():
            # tests if a rank shows up 3 times
            if card_dict[rank] == 3:
                three_kind = True
                break

        # returns no points and no hand type if there is not three of a kind
        if not(three_kind):
            return 0, ''

        # creates variable indicating rank of card with four of a kind
        three_kind_card = 0
        # creates a list of other cards
        other_cards = []

        # iterates through rank in card_dict
        for rank in card_dict:
            # assigns rank to three_kind_card and other_cards
            if card_dict[rank] == 3:
                three_kind_card = rank
            else:
                other_cards.append(rank)

        # determines the number of points
        points = 4 * 15**5 + (three_kind_card) * 15**4 + (three_kind_card) * 15**3 \
                 + (three_kind_card) * 15**2 + (other_cards[0]) * 15**1 + (other_cards[1])

        # returns the points and hand type
        return points, 'Three of a Kind'

        
    # determine if a hand has a one pair
    # takes as argument a list of 5 Card objects
    # returns a number of points for that hand
    def is_two_pair (self, hand):
        # creates a card dictionary
        card_dict = {}
        # creates a variable indicating if there is two pairs
        two_pairs = False
        
        # iterates through the player's hand
        for i in range (len(hand)):
            # counts the number of times a rank shows up
            if hand[i].rank in card_dict.keys():
                card_dict[hand[i].rank] += 1
            else:
                card_dict[hand[i].rank] = 1

        # sorts card_dict by values from highest to lowest
        sorted_dict = dict(sorted(card_dict.items(), key = lambda x: x[1]))
        # creates a list of sorted ranks
        sorted_ranks = []
       
       # appends each rank in order of sorted_dict
        for rank in sorted_dict:
            sorted_ranks.append(rank)

        # tests if the first two ranks in sorted_dict are pairs
        if card_dict[sorted_ranks[-1]] == card_dict[sorted_ranks[-2]] == 2:
            two_pairs = True
        
        # returns no points and no hand type if there is not two pairs
        if (not two_pairs):
            return 0, ''

        # creates a list of ranks with pairs
        pairs = []
        # creates a variable indicating rank of other card
        other_card = 0

        # iterates through the rank in card_dict
        for rank in card_dict:
            # assigns rank to pairs and other_card
            if card_dict[rank] == 2:
                pairs.append(rank)
            else:
                other_card = rank

        # sort the rank pairs from highest to lowest
        pairs.sort(reverse = True)
        
        # determine the number of points
        points = 3 * 15**5 + (pairs[0]) * 15**4 + (pairs[0]) * 15**3 \
                 + (pairs[1]) * 15**2 + (pairs[1]) * 15**1 + (other_card)

        # returns the points and hand type
        return points, 'Two Pair'

    # determine if a hand has a one pair
    # takes as argument a list of 5 Card objects
    # returns a number of points for that hand
    def is_one_pair (self, hand):
        # creates a card dictionary
        card_dict = {}
        # creates a variable indicating if there is one pair
        one_pair = False
        
        # iterates through the player's hand
        for i in range (len(hand)):
            # counts the number of times a rank shows up
            if hand[i].rank in card_dict.keys():
                card_dict[hand[i].rank] += 1
            else:
                card_dict[hand[i].rank] = 1

        # iterates through rank in card_dict
        for rank in card_dict.keys():
            # tests if a rank shows up 2 times
            if card_dict[rank] == 2:
                one_pair = True
                break

        # returns no points and no hand type if there is not one pair
        if not(one_pair):
            return 0, ''

        # creates a variable indicating the rank of the pair
        one_pair = 0
        # creates a list of the other cards' rank
        other_cards = []

        # iterates through rank in card_dict
        for rank in card_dict:
            # assigns rank to one_pair and other_cards
            if card_dict[rank] == 2:
                one_pair = rank
            else:
                other_cards.append(rank)
     
        # determines the number of points
        points = 2 * 15**5 + (one_pair) * 15**4 + (one_pair) * 15**3 \
                 + (other_cards[0]) * 15**2 + (other_cards[1]) * 15**1 + (other_cards[2])

        # returns the points and hand type
        return points, 'One Pair'

    # returns points for the high card
    # takes as argument a list of 5 Card objects
    # returns a number of points for that hand
    def is_high_card (self, hand):
        # determines the number of points
        points = 1 * 15**5 + (hand[0].rank) * 15**4 + (hand[1].rank) * 15**3 \
                 + (hand[2].rank) * 15**2 + (hand[3].rank) * 15**1 + (hand[4].rank)

        # returns the points and hand type
        return points, 'High Card'


def main():
  # read number of players from stdin
  line = sys.stdin.readline()
  line = line.strip()
  num_players = int(line)
  if (num_players < 2) or (num_players > 6):
    return

  # create the Poker object
  game = Poker (num_players)

  # play the game
  game.play()


if __name__ == '__main__':
    main()