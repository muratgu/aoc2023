with open('day04-input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    cards = {}
    for line in lines:
        s0, s1 = line.split(':')
        card_no = int(s0.split()[1])
        cnums, wnums = s1.split('|')
        cards[card_no] = {'cnums': cnums.split(), 'wnums': wnums.split(), 'score': 0, 'copies': 1}

    # caculates score for part1
    # every win doubles the score
    def evaluate1(cards):
        for card_no, v in cards.items():
            cnums, wnums = v['cnums'], v['wnums']
            score = -1 + sum([1 for cnum in cnums for wnum in wnums if cnum == wnum])
            cards[card_no]['score'] = 0 if score == -1 else 2**score
    
    # caculates score for part2
    def evaluate2(cards):
        for card_no, v in cards.items():
            cnums, wnums = v['cnums'], v['wnums']
            score = sum([1 for cnum in cnums for wnum in wnums if cnum == wnum])
            cards[card_no]['score'] = score
        for c in cards:
            for j in range(cards[c]['score']):
                cards[c+j+1]['copies'] += cards[c]['copies']
            
    evaluate1(cards)
    total = sum([v['score'] for v in cards.values()])
    print('day04 part1:', total)

    evaluate2(cards)
    total = sum([v['copies'] for v in cards.values()])
    print('day04 part2:', total)
