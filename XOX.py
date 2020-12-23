availables = {str(i):'' for i in range(1,10)}
running = True
p1 = 0
table = '''
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
'''
def is_won(table):
    win_combinations = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
                       [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    
    for i in win_combinations:
        pass



make_move = lambda notat, char: table.replace(notat, char)

while running:
    move = input('Please do your move: ')
    if p1 % 2:
        char = 'O'
    else:
        char = 'X'
    table = make_move(move, char)
    print(table)
    availables[move] = char
    print(availables)
    p1 += 1
    
