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
        self.max_x = self.pos.x + self.width - 1
        self.max_y = self.pos.y + self.height - 1
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

    def perimeter(self):
        return 2*(self.width - 1) + 2*(self.height - 1)

    def __lt__(self, other):
        return self.perimeter() < other.perimeter()

    def __hash__(self):
        return hash(repr(self))

    def __str__(self):
        #return 'Fence(width=%d, height=%d): %s' % (self.width, self.height, self.coordinates)
        return 'Fence(width=%d, height=%d, pos=%s)' % (self.width, self.height, self.pos)


class Solver():
    def __init__(self, land_width, land_height, marsh, fences):
        self.land_width = land_width
        self.land_height = land_height
        self.max_x = land_width - 1
        self.max_y = land_height - 1
        self.marsh = marsh


    def solve(self):
        solution = None

        for fence in reversed(fences):
            while fence.max_y <= self.max_y:
                if not fence.is_in_marsh(marsh):
                    solution = fence
                    break
                else:
                    if fence.max_x + 1 <= self.max_x:
                        fence.set_position(Point(fence.pos.x + 1, fence.pos.y))
                    else:
                        fence.set_position(Point(0, fence.pos.y + 1))

            if solution: break


        #while fence.is_in_marsh(marsh):
        #    if fence.max_x == self.max_x and fence.max_y == self.max_y:
        #        # reduce fence size and start over
        #        if fence.width > fence.height:
        #            fence = Fence(fence.width - 1, fence.height, Point(0,0))
        #        else:
        #            fence = Fence(fence.width, fence.height - 1, Point(0,0))

        #        if fence.width < 2 or fence.height < 2: # impossible case
        #            fence = None
        #            break
        #    else:
        #        if fence.max_x + 1 <= self.max_x:
        #            fence.set_position(Point(fence.pos.x + 1, fence.pos.y))
        #        else:
        #            fence.set_position(Point(0, fence.pos.y + 1))

        if solution is None:
            print 'impossible'
        else:
            #print fence, fence.coordinates
            print fence.perimeter()


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


def init_fences(land_width, land_height):
    fence_set = set()

    for w in xrange(2, land_width+1):
        for h in xrange(2, land_height+1):
            fence_set.add(Fence(w, h, Point(0,0)))

    return sorted(fence_set)


if __name__ == '__main__':
    land_dims = [ int(n) for n in sys.stdin.readline().strip().split() ]
    land_height = land_dims[0]
    land_width = land_dims[1]
    marsh = init_marsh()
    fences = init_fences(land_width, land_height)

    #for f in fences:
    #    print f

    solver = Solver(land_width, land_height, marsh, fences)
    solver.solve()

    #fence1 = Fence(land_width, land_height, Point(0,0))
    #fence2 = Fence(land_width, land_height - 2, Point(0,2))

    #print 'fence1 in marsh:', fence1.is_in_marsh(marsh)
    #print 'fence2 in marsh:', fence2.is_in_marsh(marsh)

    #print marsh
    #print fence.coordinates
