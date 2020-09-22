# http://codercareer.blogspot.com.br/2012/02/no-34-string-path-in-matrix.html


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def left(self):
        return Point(self.x - 1, self.y)

    def right(self):
        return Point(self.x + 1, self.y)


    def up(self):
        return Point(self.x, self.y + 1)

    def down(self):
        return Point(self.x, self.y - 1)

    def __str__(self):
        return str((self.y, self.x))

    def __repr__(self):
        return str(self)


class Path():
    def __init__(self, matrix):
        self._points = []
        self.max_y = len(matrix[0])
        self.max_x = len(matrix)
        self.matrix = matrix
        self.mask = [[False] * self.max_y for i in range(self.max_x)]

    def neighbors(self):
        point = self._points[-1]
        up = point.up()
        if up.y < self.max_y and not self.visited(up):
            yield up

        down = point.down()
        if down.y >= 0 and not self.visited(down):
            yield down

        left = point.left()
        if left.x >= 0 and not self.visited(left):
            yield left

        right = point.right()
        if right.x < self.max_x and not self.visited(right):
            yield right

    def visited(self, point):
        return self.mask[point.x][point.y]

    def append(self, x, y):
        self._points.append(Point(x, y))
        self.mask[x][y] = True

    def pop(self):
        p = self._points.pop()
        self.mask[p.x][p.y] = False

    def char(self, x, y):
        return self.matrix[x][y]

    def search(self, word, x, y):
        if word == '':
            return self._points
        if self.char(x, y) == word[0]:
            self.append(x, y)
            for neighbor in self.neighbors():
                result = self.search(word[1:], neighbor.x, neighbor.y)
                if result:
                    return result
            self.pop()
        return []


def search_path(word, matrix):
    path = Path(matrix)
    for x, line in enumerate(matrix):
        for y, char in enumerate(line):
            result = path.search(word, x, y)
            if result:
                return result
    return []


m = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]

print(search_path('ABCB', m))