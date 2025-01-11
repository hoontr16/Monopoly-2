

def drawRectangle(h, w, hChar, wChar):
    """
    create a string representation of a rectangle.

    arguments:
        h (int): how many characters tall the rectangle is, not counting the topmost line.
        w (int): how many characters wide the rectangle is, not counting either side.
        hChar (str): what character makes up the left and right sides.
        wChar (str): what character makes up the top and bottom sides.
    """
    top = ''.join([' ', wChar * w, ' '])
    middle = '\n'.join([''.join([hChar, ' ' * w, hChar])] * max(h - 1, 0))
    bottom = ''.join([hChar, wChar * w, hChar])
    return '\n'.join([top, middle, bottom])

class BoardSpace:
    def __init__(self, index, orientation):
        """
        initialize a BoardSpace object.

        arguments:
            index (int): the space's index number, starting at Go
            orientation (int): how to draw the space. 0 is tall, 1 is wide
        """
        if orientation == 0:
            self.wChar = '_'
            self.hChar = '|'
            self.shape = drawRectangle(3, 2, self.hChar,self.wChar)
        elif orientation == 1:
            self.wChar = '-'
            self.hChar = '_'
            self.shape = drawRectangle(2, 3, self.hChar, self.wChar)
        else:
            raise ValueError('bad orientation: ' + orientation)
    
    def __str__(self):
        return self.shape

class Board:
    def __init__(self):
        pass

    def draw(self):
        fullBoard = """
 ___ __ __ __ __ __ __ __ __ __ ___
|   |  |  |  |  |  |  |  |  |  |   |
|   |  |  |  |  |  |  |  |  |  |   |
|___|__|__|__|__|__|__|__|__|__|___|
|   |                          |   |
|___|                          |___|
|   |                          |   |
|___|                          |___|
|   |                          |   |
|___|                          |___|
|   |                          |   |
|___|                          |___|
|   |                          |   |
|___|                          |___|
|   |                          |   |
|___|                          |___|
|   |                          |   |
|___|                          |___|
|   |                          |   |
|___|                          |___|
|   |                          |   |
|___|__ __ __ __ __ __ __ __ __|___|
|   |  |  |  |  |  |  |  |  |  |   |
|   |  |  |  |  |  |  |  |  |  |   |
|___|__|__|__|__|__|__|__|__|__|___|"""
        return fullBoard

def drawBoardLine(type, smallLength, bigLength):
    gapLen = 8 + (smallLength * 9)
    smallSideUS = ['_' * smallLength]
    smallSideSpace = [' ' * smallLength]
    bigSideUS = ['_' * bigLength]
    bigSideSpace = [' ' * bigLength]
    if type == 0:
        return ' '.join([''] + bigSideUS + (smallSideUS * 9) + bigSideUS + [''])
    elif type == 1:
        return '|'.join([''] + bigSideSpace + (smallSideSpace * 9) + bigSideSpace + [''])
    elif type == 2:
        return '|'.join([''] + bigSideUS + (smallSideUS * 9) + bigSideUS + [''])
    elif type == 3:
        boardLen = 12 + (smallLength * 9) + (bigLength * 2)
        return '|'.join([''] + bigSideSpace + [' ' * gapLen] + bigSideSpace + [''])
    elif type == 4:
        return '|'.join([''] + bigSideUS + [' ' * gapLen] + bigSideUS + [''])
    elif type == 5:
        return ''.join(['|'] + bigSideUS + ['|']) + ' '.join(smallSideUS * 9) + ''.join(['|'] + bigSideUS + ['|'])
        return ' '.join([''.join(['|'] + bigSideUS + ['|'])] + (smallSideSpace * 9) + [''.join(['|'] + bigSideUS + ['|'])])

def genLineSeq(smallLength, bigLength):
    smallLength -= 1
    bigLength -= 1
    seq1 = [0] + ([1] * bigLength) + [2]
    seq3 = [5] + ([1] * bigLength) + [2]
    seq2 = ([4] + ([3] * smallLength)) * 8
    seq2.pop(0)
    return seq1 + seq2 + seq3

if __name__ == '__main__':
    lineInd = genLineSeq(5, 6)
    for i in lineInd:
        print(drawBoardLine(i, 5, 6))
    exit()

    #print(drawRectangle(6, 5, '|', '_'))
    #print(Board().draw())
    print(drawBoardLine(0, 5, 6))
    print(drawBoardLine(1, 5, 6))
    print(drawBoardLine(1, 5, 6))
    print(drawBoardLine(2, 5, 6))
    print(drawBoardLine(3, 5, 6))
    print(drawBoardLine(4, 5, 6))
    print(drawBoardLine(5, 5, 6))
    print()
    print(genLineSeq(5, 6))