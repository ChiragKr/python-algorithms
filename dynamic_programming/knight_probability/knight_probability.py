'''
Knight placed on a `N` * `N` board. allowed to move
`K` steps starting from position (col=`x`, row=`y`).
Probability Knight remains inside the board? Assume
Knight cannot move back into the board once it steps out.

INPUT:
8 6
0 0

OUTPUT:
0.1875

EXPLANATION:
N = 8, K = 0, x = 0, y = 0
'''
import sys

'''
y+2 |   | H |   | A |   |
    =====================
y+1 | G |   |   |   | B |
    =====================
y   |   |   | s |   |   |
    =====================
y-1 | F |   |   |   | C |
    =====================
y-2 |   | E |   | D |   |
     x-2 x-1  x  x+1 x+2
'''
MOVES = {(+1, +2), (+2, +1), (+2, -1), (+1, -2),
         (-1, -2), (-2, -1), (-2, +1), (-1, +2)}


def within_board(s, n):
    return (s[0] in range(0, n) and s[1] in range(0, n))


def knight_probability(s, n, k):
    probability = 0.00
    x, y = s
    is_within_board = within_board(s, n)
    if not is_within_board:
        probability = 0.00
    elif k == 0:
        probability = 1.00
    else:
        for ds in MOVES:
            dx, dy = ds
            s_ = (x + dx, y + dy)
            probability += (1.0 / 8.0) * knight_probability(s_, n, k-1)
    print(f'P[ (x={x},y={y}) | steps={k} ] = {probability}')
    return probability


def main(argc, argv):
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')
    n, k = map(int, input().split(' '))
    initialPosition = tuple(map(int, input().split(' ')))
    print(knight_probability(initialPosition, n, k))
    return 0


if __name__ == '__main__':
    argv = sys.argv
    argc = len(argv)
    if(main(argc, argv) == 0):
        print(argv[0]+" execution: SUCCESS")
    else:
        print(argv[0]+" execution: FAILURE")
