import sys
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

class Fence():
    def __init__(self, width, height, pos):
        '''pos is a Point representing upper leftmost coordinate.'''
        self.width = width
        self.height = height
        self.pos = pos
        self.init_coords()


    def init_coords(self):
        self.coordinates = set()

        for row in xrange(self.height):
            self.coordinates.add( Point(self.pos.x, self.pos.y + row) )
            self.coordinates.add( Point(self.pos.x + self.width - 1, self.pos.y + row) )

            if row == 0 or row == self.height - 1:
                self.coordinates.update(
                        [ Point(xcoord, self.pos.y + row) for xcoord in
                          xrange(self.pos.x + 1, self.pos.x + self.width - 1) ])
        


def init_marsh():
    """Marsh will be represented as a set of coordinates."""

    marsh = set()
    y = 0
    
    for line in sys.stdin.readlines():
        x = 0
    
        for c in line:
            if c == 'x': marsh.add( Point(x, y) )
            x += 1
    
        y += 1

    return marsh


if __name__ == '__main__':
    land_dims = [ int(n) for n in sys.stdin.readline().strip().split() ]
    marsh = init_marsh()
    fence = Fence(4, 2, Point(0,0))

    print marsh
    print fence.coordinates
