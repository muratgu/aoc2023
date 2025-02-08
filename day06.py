import math

with open('day06-input.txt','r') as f:
    lines = [line.strip() for line in f.readlines()]
    times = lines[0].split(':')[1].split()
    dists = lines[1].split(':')[1].split()

    # find number of different button holds 
    # that would win a race. 
    # 1 msec of button hold adds 1mm/msec to boat speed 
    # and decreases the race duration by 1msec
    def find_holds(race):
        holds = 0
        race_time, race_dist = race
        for hold in range(1, race_time):
            speed = hold
            time = race_time - hold
            dist = speed * time
            holds += 1 if dist > race_dist else 0
        return holds
    
    # find the number button holds by calculating the range 
    # it's a quadratic equation
    # dist = holds * (time - holds)
    def find_holds_range(race):
        race_time, race_dist = race
        # find zeroes by (+/-) sqrt(b^2-4a)/2
        minx = (race_time - math.sqrt(race_time**2 - 4*race_dist))/2
        maxx = (race_time + math.sqrt(race_time**2 - 4*race_dist))/2 - 1
        # reduce by 1 before rounding for integer solutions 
        round_off = -1 if int(maxx-minx)==(maxx-minx) else 0
        return round(maxx-minx+round_off)
    
    def solve1(times, dists):
        times = [int(w) for w in lines[0].split(':')[1].split()]
        dists = [int(w) for w in lines[1].split(':')[1].split()]
        races = zip(times, dists)
        score = 1
        for race in races:
            score *= find_holds(race)
        return score
    
    def solve2(times, dists):
        time = int(''.join(times))
        dist = int(''.join(dists))
        return find_holds_range((time, dist))
    
    print('day06 part1', solve1(times,dists))
    print('day06 part2', solve2(times,dists))
