with open('day02-input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    games = {}
    for line in lines:
        gid = int(line.split(':')[0].split()[1])
        games[gid] = []
        for s in line.split(':')[1].split(';'):
            glist = []
            for ball in [b.strip() for b in s.split(',')]:
                num, color = ball.split(' ')
                glist.append((int(num), color))
            games[gid].append(glist)
    
    def game_possible(game, load):
        for blist in game:
            for ball in blist:
                num, color = ball
                if load[color] < num:
                    return False
        return True
    
    def get_min_load_power(game):
        ld = {'red': 0, 'blue': 0, 'green': 0}
        for blist in game:
            for ball in blist:
                num, color = ball
                if ld[color] < num:
                    ld[color] = num
        power = ld['red']*ld['blue']*ld['green']
        return power

    def solve1():
        load = {'red': 12, 'green': 13, 'blue': 14}
        return sum([id if game_possible(g, load) else 0 for id, g in games.items()])
    
    def solve2():
        return sum([get_min_load_power(g) for g in games.values()])

    print('day02 part1', solve1())

    print('day02 part2', solve2())
