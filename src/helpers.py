def in_grid(grid, coord):
    i, j = coord
    return not (i >= grid.height or i < 0 or j >= grid.width or j < 0)

def get_directions(directions=4):
    """ 
    """
    if directions == 4:
        return [(-1, 0), (0, 1), (1, 0), (0, -1)]
    elif directions == 8:
        holder = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]
        return [i for i in holder if i != (0, 0)]
    else:
        raise NotImplementedError("Unable to handle neighbour generation for {} directions.".format(directions))

def get_neighbour_coords(grid, coord, directions=4):
    """
    """
    si, sj = coord  # Initial coords
    res = [(si + i, sj + j) for i, j in get_directions(directions)]
    return [coord for coord in res if in_grid(grid, coord)]

def get_neighbours(grid, coord, allow_unpassable=False, directions=4):
    """Given a grid and coordinates on that grid, identifies all passable neighbours on the grid
    """
    coords = get_neighbour_coords(grid, coord, directions)
    neighbours = [grid[i][j] for i, j in coords]
    # If allow_unpassable is False, do not filter out all unpassable tiles
    neighbours = [i for i in neighbours if i.tags.get("passable", True) != False]
    return neighbours



def iternodes(grid):
    for i, row in enumerate(grid.grid):
        for j, node in enumerate(row):
            yield (node, i, j)


if __name__ == "__main__":
    from structs import Grid

    grid = Grid.from_matrix([[i for i in range(2)] for j in range(3)])
    assert(in_grid(grid, (1, 1)) is True)
    assert(in_grid(grid, (3, 1)) is False)
    assert(in_grid(grid, (0, -1)) is False)

    assert(set(get_neighbour_coords(grid, (0, 0))) == {(0, 1), (1, 0)})
    assert(set(get_neighbour_coords(grid, (0, 0), directions=8)) == {(0, 1), (1, 0), (1, 1)})
