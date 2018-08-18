class Coord:
    pass

class Node:
    """Map node instance
    """

    def __init__(self, char, tags, coord, cost=1):
        """
        @args
            char
            cost
            tags (dict): Dictionary containing tag objects
            coord (2tup): Unique coordinates on a 2d grid
        """
        self.char = str(char)  # Consider allowing for tile based representations
        self.cost = cost
        self.tags = tags
        self.coord = coord

    def __repr__(self):
        return f"<Node: char={self.char}, cost={self.cost}, coord={self.coord}, tags={self.tags}"


class Grid:
    def __init__(self, grid):
        """
        @args:
            grid (2d list of Node objects)
        """
        self.grid = grid

    def __getitem__(self, i):
        return self.grid[i]

    def to_string(self):
        return "\n".join("".join(val.char for val in row) for row in self.grid)

    @property
    def shape(self):
        return (self.height, self.width)

    @property
    def height(self):
        return len(self.grid)

    @property
    def width(self):
        return len(self.grid[0])

    @classmethod
    def from_iter(cls, mat, costs=None):
        """Generates a Grid from a 2d iterable containing character/numeric objects
        @args:
            mat (2d iterable):
            costs (2d iterable):
        """
        grid = [[Node(val, {}, (i, j)) for j, val in enumerate(row)] for i, row in enumerate(mat)]
        if costs:
            for i, row in enumerate(costs):
                for j, cost in enumerate(row):
                    grid[i][j].cost = cost
        return cls(grid)

    @classmethod
    def from_dictiter(cls, mat):
        grid = [[Node(data["char"],
                      data["tags"],
                      data["coord"],
                      cost=data["cost"]) for j, data in enumerate(row)] for i, row in enumerate(mat)]



if __name__ == "__main__":
    grid = Grid.from_iter([[".", ".", "."],
                             ["#", "#", "."],
                             [".", ".", "."]])
    print(grid.shape)
    print(grid.to_string())

