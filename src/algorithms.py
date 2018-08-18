from heapdict import heapdict
from collections import defaultdict

from helpers import iternodes, get_neighbours
import heuristics

def backtrack(tracker, coord, cur=()):
    next_coord = tracker.get(coord, None)
    if next_coord is None:
        return cur +(coord,)
    return backtrack(tracker, next_coord, cur + (coord,))






def bfs(grid, start, end):
    """Finds the Shortest path from A to B in a grid ingoring costs. If costs are desired, used astar/dijkstra instead
    """
    pass


def astar(grid, start, end, heuristic):
    """
    @args:
        start (tuple): 2d Tuple of form (i, j) indicating start position
        end (tuple): 2d Tuple of form (i, j) indicating end position
    @returns:
        Iterable object containing the derived path from start to end or None if no path exists
    @notes:
        Assumptions: Start point is accessible
                     No negative cycles
    """
    unvisited = {}
    visited = {start: 0}
    came_from = {}

    pq = heapdict({start: 0})
    while pq:
        # Pop the node with the lowest score
        coord, score = pq.popitem()
        # If the end has the lowest score, return
        if coord == end:
            return backtrack(came_from, coord)
        for neighbour in get_neighbours(grid, coord):
            ncoord = neighbour.coord
            # Score for a given neighbour from current node
            nscore = score + neighbour.cost + heuristic(coord, ncoord)
            # If a negative delta is observed, something has gone wrong (Negative cycles in graph)
            if nscore < score:
                raise Exception("Negative cycle found")
            # Update if the node is unvisited or the path is more efficient
            if ncoord not in visited or nscore < visited[ncoord]:
                visited[ncoord] = nscore
                pq[ncoord] = nscore
                came_from[ncoord] = coord
    return None


def djkstra(grid, start, end):
    return astar(grid, start, end, heuristics.identity)


if __name__ == "__main__":
    from structs import Grid

    grid = Grid.from_iter(["...",
                           "#..",
                           "..."],
                          [[1, 1, 1],
                           [100, 1, 1],
                           [1, 1, 1]])
    print(grid.to_string())
    print(djkstra(grid, (0, 0), (2, 0)))
