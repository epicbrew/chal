import sys

class Fence():
    def __init__(self, width, height, origin):
        '''origin is a two-tuple representing upper leftmost coordinate.'''
        self.width = width
        self.height = height
        self.origin = origin
        self.coordinates = self.init_coords()


    def init_coords(self):
        


def init_marsh():
    """Marsh will be represented as a set of coordinates."""

    marsh = set()
    row = 0
    
    for line in sys.stdin.readlines():
        col = 0
    
        for c in line:
            if c == 'x': marsh.add( (row, col) )
            col += 1
    
        row += 1

    return marsh


if __name__ == '__main__':
    land_dims = [ int(n) for n in sys.stdin.readline().strip().split() ]
    marsh = init_marsh()
    
    print marsh
