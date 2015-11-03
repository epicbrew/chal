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


    def is_in_marsh(self, marsh):
        return not self.coordinates.isdisjoint(marsh) 


    def set_position(self, pos):
        self.pos = pos
        self.init_coords()
        

class Solver():
    def __init__(self, land_width, land_height, marsh):
        self.land_width = land_width
        self.land_height = land_height
        self.max_x = land_width - 1
        self.max_y = land_height - 1
        self.marsh = marsh


    def solve(self):
        fence = Fence(self.land_width, self.land_height, Point(0,0))
        


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
    land_height = land_dims[0]
    land_width = land_dims[1]
    marsh = init_marsh()

    fence1 = Fence(land_width, land_height, Point(0,0))
    fence2 = Fence(land_width, land_height - 2, Point(0,2))

    print 'fence1 in marsh:', fence1.is_in_marsh(marsh)
    print 'fence2 in marsh:', fence2.is_in_marsh(marsh)

    #print marsh
    #print fence.coordinates
