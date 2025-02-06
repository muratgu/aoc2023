with open('day03-input.txt', 'r') as f:
    lines = [ line.strip() for line in f.readlines() ]
    matrix = [ list(line) for line in lines ]

    ROWS = len(matrix)
    COLS = len(matrix[0])

    digits = list('0123456789')
    non_symbols = digits + ['.']
    
    dirs = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]
    
    # returns true if location x,y has any symbol adjecent to it
    def adj_to_sym(x, y):
        for d in dirs:
            nx, ny = x + d[0], y + d[1]
            if nx >= 0 and nx < ROWS and ny >= 0 and ny < COLS:
                if matrix[nx][ny] not in non_symbols:
                    return True
        return False
    
    # finds (and yields each location of) all '*' symbols next to a location x,y
    def find_star(x, y):
        for d in dirs:
            nx, ny = x + d[0], y + d[1]
            if nx >= 0 and nx < ROWS and ny >= 0 and ny < COLS:
                if matrix[nx][ny] == '*':
                    yield (nx, ny)
        
    # finds all numbers adjecent to symbols (for part1)
    # finds all pairs of numbers near '*' symbols (for part2)
    def find_numbers():

        def add_num(num, adj):
            if num != '':
                if adj: 
                    numbers.append(int(num))
                for s in stars:
                    gears[s] = [int(num)] if s not in gears \
                               else gears[s] + [int(num)]
                return True

        numbers = []
        gears = {}
        num = adj = ''
        stars = set()

        for i in range(ROWS):
            for j in range(COLS):
                c = matrix[i][j]
                if c in digits:
                    num += c
                    adj += c if adj_to_sym(i, j) else ''
                    [stars.add(s) for s in find_star(i, j)]
                elif add_num(num, adj):
                    num, adj, stars = '', '', set()
            if add_num(num, adj):
                num, adj, stars = '', '', set()
        return numbers, gears

    def solve():
        numbers, gears = find_numbers()
        total = sum(numbers)
        geartotal = 0
        for g in gears:
            if len(gears[g]) == 2:
                [numbers.remove(n) for n in gears[g]]
                geartotal += gears[g][0] * gears[g][1]
        return total, geartotal
    
    t, g = solve()
    print('day03 part1:', t)

    print('day03 part2:', g)
