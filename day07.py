from collections import Counter

with open('day07-input.txt','r') as f:
    lines = [line.strip().split() for line in f.readlines()]
    hands = dict([(line[0], int(line[1])) for line in lines])

    card_order = list(reversed(['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']))

    # with joker the lowest rank
    card_order2 = list(reversed(['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']))

    def type_of_hand(hand):
        card_counts = Counter([c for c in hand])
        if len(card_counts) == 1: 
            return 7  #fiveofakind   AAAAA
        if len([x for x in card_counts.values() if x == 4]) == 1: 
            return 6  #fourofakind   AAAAC
        if len(card_counts) == 2 and len([x for x in card_counts.values() if x == 3]) == 1: 
            return 5  #fullhouse     AAACC
        if len(card_counts) == 3 and len([x for x in card_counts.values() if x == 3]) == 1: 
            return 4  #threeofakind  AAACE
        if len([x for x in card_counts.values() if x == 2]) == 2: 
            return 3  #twopair       AACCE
        if len(card_counts) == 4: 
            return 2  #onepair       AACED
        if len(card_counts) == 5: 
            return 1  #highcard      ABCDE

    def replace_jokers(hand):
        card_counts = Counter([c for c in hand])
        j_counts = card_counts['J']
        if j_counts == 5: 
            return hand
        if j_counts == 5: 
            return 'AAAAA'
        best_non_joker = [k[0] for k in card_counts.most_common() if k[0]!='J'][0]
        return hand.replace('J', best_non_joker, j_counts)

    def rank_of_hand(hand, with_joker=False):
        if with_joker:
            rank = type_of_hand(replace_jokers(hand))  
            for c in hand:
                rank = rank*100 + card_order2.index(c)+1 
        else:
            rank = type_of_hand(hand)  
            for c in hand:
                rank = rank*100 + card_order.index(c)+1 
        return rank
    
    ranked_cards = sorted(hands, key=lambda x: rank_of_hand(x))
    winnings = sum([hands[v] * (i+1) for i,v in enumerate(ranked_cards)])
    print('day07 part1', winnings) 

    ranked2_cards = sorted(hands, key=lambda x: rank_of_hand(x, with_joker=True))
    winnings2 = sum([hands[v] * (i+1) for i,v in enumerate(ranked2_cards)])
    print('day07 part2', winnings2) 
    
