import sys
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

def perimeter(width, height):
    if width < 2 or height < 2:
        return 0
    else:
        return 2*(width - 1) + 2*(height - 1)


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
        return perimeter(self.width, self.height)

    def __lt__(self, other):
        return self.perimeter() < other.perimeter()

    def __hash__(self):
        return hash(repr(self))

    def __str__(self):
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

        #for fence in reversed(fences):
        for fence in xfences(land_width, land_height):
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


def xfences(land_width, land_height):
    tried = set()
    next_tries = []

    cur = Point(land_width, land_height)

    while True:
        if perimeter(cur.x, cur.y) >= 4:
            yield Fence(cur.x, cur.y, Point(0,0))
        else:
            break

        tried.add(cur)

        cand1 = Point(cur.x - 1, cur.y)
        if (cand1 not in tried) and cand1 not in next_tries and perimeter(cand1.x,cand1.y) >= 4:
            next_tries.append(cand1)

        cand2 = Point(cur.x, cur.y - 1)
        if (cand2 not in tried) and cand2 not in next_tries and perimeter(cand2.x,cand2.y) >= 4:
            next_tries.append(cand2)

        cand3 = Point(cur.x - 1, cur.y - 1)
        if (cand3 not in tried) and cand3 not in next_tries and perimeter(cand3.x,cand3.y) >= 4:
            next_tries.append(cand3)
            
        next_tries = sorted(next_tries, key=lambda p: perimeter(p.x,p.y))
        if len(next_tries) == 0:
            break

        cur = next_tries.pop()


if __name__ == '__main__':
    land_dims = [ int(n) for n in sys.stdin.readline().strip().split() ]
    land_height = land_dims[0]
    land_width = land_dims[1]
    marsh = init_marsh()
    fences = init_fences(land_width, land_height)

    solver = Solver(land_width, land_height, marsh, fences)
    solver.solve()
