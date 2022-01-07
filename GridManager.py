from random import randint, shuffle


class FallingPiece:
    def __init__(self, t):
        self.type = t
        self.coord = [6 if self.type in (3, 4, 7) else 7,
                      -3 if self.type in (3, 4, 7) else -4 if self.type == 2 else -2]
        self.coordd = [6 if self.type == 2 else 8, self.coord[1]]
        self.center = [int((self.coord[0]+self.coordd[0])/2), -3 if self.type == 2 else -2]
        self.box = self.sethitbox(self.coord)
        self.nextbox = self.box[:]
        self.moveinto = [0, 0]

    def sethitbox(self, coo):
        if self.type == 1:          # Square 2x2
            return [[coo[0] + v, coo[1] + i] for v in range(2) for i in range(2)]
        elif self.type == 2:        # Line 1x4
            return [[coo[0], coo[1] + i] for i in range(4)]
        elif self.type == 3:        # S 3x2
            return [[coo[0] + 1 + v, coo[1]] for v in range(2)] + [[coo[0] + v, coo[1] + 1] for v in range(2)]
        elif self.type == 4:        # Z 3x2
            return [[coo[0] + v, coo[1]] for v in range(2)] + [[coo[0] + 1 + v, coo[1] + 1] for v in range(2)]
        elif self.type == 5:        # L 2x3
            return [[coo[0], coo[1] + i] for i in range(3)] + [[coo[0] + 1, coo[1] + 2]]
        elif self.type == 6:        # J 2x3
            return [[coo[0] + 1, coo[1] + i] for i in range(3)] + [[coo[0], coo[1] + 2]]
        elif self.type == 7:        # T 3x2
            return [[coo[0] + v, coo[1]] for v in range(3)] + [[coo[0] + 1, coo[1] + 1]]

    def movehor(self, i, grid):
        self.nextbox = list(map(lambda x: [x[0] + i, x[1]], self.box))
        movable = True
        for v in self.nextbox:
            if v[0] in range(15) and v[1] in range(20):
                if not (grid[v[0]][v[1]] == 0):
                    movable = False
                    break
            elif not (v[0] < 0 or v[1] < 0):
                movable = False
                break
        if movable:
            self.coord[0] += i
            self.coordd[0] += i
            self.center[0] += i
            self.box = self.nextbox[:]

    def godown(self, grid):
        self.nextbox = list(map(lambda x: [x[0], x[1]+1], self.box))
        movable = True
        for v in self.nextbox:
            if v[0] in range(0, 15) and v[1] in range(0, 20):
                if not (grid[v[0]][v[1]] == 0):
                    movable = False
                    break
            if v[1] == 20:
                movable = False
        if movable:
            self.coord[1] += 1
            self.coordd[1] += 1
            self.center[1] += 1
            self.box = self.nextbox[:]
        else:
            return True
        return False

    def rotate(self):
        self.box = [[self.center[0]+v[1]-self.center[1], self.center[1]-(v[0]-self.center[0])]for v in self.box]
        self.coord = self.center[:]
        self.coordd = self.center[:]
        for v in self.box:
            self.coord = [v[0] if v[0] < self.coord[0] else self.coord[0],
                          v[1] if v[1] < self.coord[1] else self.coord[1]]
            self.coordd = [v[0] if v[0] > self.coord[0] else self.coord[0],
                           v[1] if v[1] < self.coord[1] else self.coord[1]]


class GridStruc:
    grid: list[list[int]]
    floor: list[int]

    def __init__(self):
        self.grid = [[0 for v in range(0, 20)] for i in range(0, 15)]
        self.igrid = [[0 for v in range(0, 15)] for i in range(0, 20)]
        self.floor = [19 for v in range(0, 15)]
        self.full = False
        self.pieces = [v+1 for v in range(7)] + [randint(1, 7) for v in range(7)]
        shuffle(self.pieces)
        self.counter = 0

    def refreshgrid(self):
        for k in range(15):
            self.grid[k] = list(map(lambda x: x[k], self.igrid))

    def setelement(self, b, t):
        self.counter += 1
        if self.counter == 14:
            self.pieces = [v+1 for v in range(7)] + [randint(1, 7) for v in range(7)]
            shuffle(self.pieces)
            self.counter = 0
        for v in b:
            self.grid[v[0]][v[1]] = t
            self.igrid[v[1]][v[0]] = t
        dellines = [k for k, v in enumerate(self.igrid) if 0 not in self.igrid[k]]
        if dellines:
            for v in dellines:
                del(self.igrid[v])
                self.igrid.insert(0, [0 for i in range(20)])
            self.refreshgrid()

    def curtype(self):
        return self.pieces[self.counter]
