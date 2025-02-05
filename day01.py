with open('day01-input.txt', 'r') as f:
    DEBUG = True
    lines = [line.strip() for line in f.readlines()]

    import re
    fex = re.compile(r'\d+')
    lex = re.compile(r'(\d+)(?!.*\d)')

    def solve1():
        res = 0
        for line in lines:
            res += int(fex.search(line).group()[0] + lex.search(line).group()[-1])
        return res
    
    def solve2():
        def rreplace(s, old, new, occurrence):
            li = s.rsplit(old, occurrence)
            return new.join(li)
        # to reuse the regex logic in part1, we will convert words to digits
        # but... certain words may overlap, i.e. 'nineight' or 'twone'
        # solution: preserve the first and last letters  
        digits = {'one': 'o1e', 'two': 't2o', 'three': 't3e',  'four': 'f4r', 
                 'five': 'f5e', 'six': 's6x', 'seven': 's7n', 'eight': 'e8t', 
                 'nine': 'n9n'}
        res = 0
        for line in lines:
            for d in digits:
                line = line.replace(d, digits[d])
            res += int(fex.search(line).group()[0] + lex.search(line).group()[-1])
        return res
    
    res = solve1()
    print('day01 part1', res)

    res = solve2()
    print('day01 part2', res)