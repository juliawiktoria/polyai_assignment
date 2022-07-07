import numpy as np # numpy for easy arrays
import sys # sys for stdin management


def manhattan_dist(x_origin, y_origin, x, y):
    """
    Calculates Manhattan Distance between two points - distance in straight lines that does not allows for diagonal moves
    """
    return abs(x_origin - x) + abs(y_origin - y)


class PizzaBlock:
    def __init__(self, n, x, y, r):
        # translate the city coordinates into Python coordinates ([1,1] in the top-left corner for now)
        self.x = x - 1
        self.y = y - 1
        self.r = r
        # initialise empty grid in the city dimensions
        self.grid = np.zeros((n, n))

    def fill_map(self):
        # goes through every point on the map and marks it with '1' if its Manhattan Distance is withing the given r
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if manhattan_dist(self.x, self.y, i, j) <= self.r:
                    self.grid[i][j] = 1
        
        # flip the grid so the final coords are in line with the task coordinates ([1,1] in the bottom-left corner insted od the top-left one)
        self.grid = np.flipud(self.grid)
        return self.grid


if __name__ == '__main__':
    
    # catch all lines of the stdin into an easy to manipulate array
    input_lines = []
    for line in sys.stdin:
        input_lines.append(line.strip('\n'))

    # first line - city dimensions and number of pizza shops
    first_line = [int(number) for number in input_lines[0].split(' ')]
    n, m = first_line[0], first_line[1]

    # initialise empty city map that will have multiple blocks added onto it
    full_city_map = np.zeros((n, n))

    # loop through the number of the needed Pizza Shops and get their coordinates
    # work on the initial input list; start indexing at 1 to avoid using extra space
    for i in range(1, m+1):
        pizza_details = input_lines[i].split(' ')
        x, y, r = int(pizza_details[0]), int(pizza_details[1]), int(pizza_details[2])

        # create a new block with info from one Pizza Shop
        new_pizza_block = PizzaBlock(n, x, y, r)
        # add the new Pizza Shop Map onto the exisitng city map
        full_city_map += new_pizza_block.fill_map()

    max_block = int(np.max(full_city_map))
    print(max_block)
