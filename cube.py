from enum import Enum
from collections import deque

c = [{'id': 1,
      'rot': 0,
      'flip': False,
      'shape': ((1,1,0,1,1),
                (1,1,1,1,1),
                (0,1,1,1,0),
                (1,1,1,1,1),
                (0,0,1,0,1))},
     {'id': 2,
      'rot': 0,
      'flip': False,
      'shape': ((0,2,0,2,0),
                (0,2,2,2,0),
                (2,2,2,2,2),
                (0,2,2,2,2),
                (0,0,2,0,0))},
     {'id': 3,
      'rot': 0,
      'flip': False,
      'shape': ((3,3,0,0,0),
                (0,3,3,3,3),
                (3,3,3,3,0),
                (0,3,3,3,3),
                (0,0,3,0,0))},
     {'id': 4,
      'rot': 0,
      'flip': False,
      'shape': ((4,4,0,4,0),
                (0,4,4,4,0),
                (4,4,4,4,0),
                (0,4,4,4,4),
                (4,4,0,4,4))},
     {'id': 5,
      'rot': 0,
      'flip': False,
      'shape': ((0,0,5,0,0),
                (0,5,5,5,0),
                (5,5,5,5,5),
                (0,5,5,5,0),
                (0,0,5,5,5))},
     {'id': 6,
      'rot': 0,
      'flip': False,
      'shape': ((0,6,0,6,0),
                (6,6,6,6,5),
                (0,6,6,6,0),
                (6,6,6,6,6),
                (0,0,6,0,0))}
]

def printColor(text, color):
    print('\x1b[1;' + str(30+color) +';40m' + text + '\x1b[0m', end='')

def printPiece(piece):
    print('trfe: '+str(piece))
    for line in piece['shape']:
        for block in line:
            if block == 0:
                print('  ', end='')
            else:
                printColor('██', block)
        print()

def printPieces(pieces):
    for piece in pieces:
        printPiece(piece)
        print()

def rotate(piece):
    res = [[],[],[],[],[]]
    for r in range(5):
        for c in range(5):
            res[4-c].append(piece['shape'][r][c])
    return {'id': piece.id,
            'rot': piece.rotate + 1,
            'flip': piece.flip,
            'shape': tuple(res)}

def flip(piece):
    res = [[],[],[],[],[]]
    for r in range(5):
        for c in range(5):
            res[4-r].append(piece['shape'][r][c])
    return {'id': piece.id,
            'rot': piece.rotate,
            'flip': not piece.flip,
            'shape': tuple(res)}

def test():
    print('\n:: ROTATIONS / FLIPS OF c[0] ::\n') 
    printPieces([
        c[0],
        rotate(c[0]),
        rotate(rotate(c[0])),
        rotate(rotate(rotate(c[0]))),
        flip(c[0]),
        rotate(flip(c[0])),
        rotate(rotate(flip(c[0]))),
        rotate(rotate(rotate(flip(c[0])))),
    ])

    print('\n:: c[0] -- c[5] ::\n')
    printPieces(c)

Pos = Enum('Pos', 'north south east')

def match(p1, p2, where):
    if where == Pos.north:
        b1 = p1['shape'][0]
        b2 = p2['shape'][-1]
    elif where == Pos.south:
        b1 = p1['shape'][-1]
        b2 = p2['shape'][0]
    elif where == Pos.east:
        b1 = [r[-1] for r in p1['shape']]
        b2 = [r[0] for r in p2['shape']]
    print(str(b1) + '\n' + str(b2))
    return all([x == 0 or y == 0 for x,y in zip(b1, b2)])

printPiece(c[0])
printPiece(c[1])
print(match(c[1], c[0], Pos.east))

def solve(pieces):
    res = pieces.pop()
    return solveHelper(pieces, res)
    
def solveHelper(pieces, result):
    

printPieces(solve(c))
