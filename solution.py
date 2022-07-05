from multiprocessing.dummy import current_process


def print_map(arr):
    """
    Prints the city map row by row
    """
    for elem in arr:
        print(elem)


def translate_coords(x, y):
    """
    Translating the input coordinates into ones that are compatibile with the nested list approach
    X-coord is inverted to negative to make use out of the negative indexing in Python, since the map origin is in the bottom-left corner
    Y-coord is decremented by 1, to account for indexing in Python staring from 0
    """
    return -x, y-1


def vary_around(point_val, r):
    return list(range(point_val - r, point_val + r + 1))

# TODO: deal with the range in the city notation (and not in the Python notation)
def delete_points_outside_range(points, n):
    """
    Handles the points that are outside of the borders of the map (using the map coords, and not Python indices)
    """
    result = []
    for point in points:
        if point[0] < 1 or point[0] > n or point[1] < 1 or point[1] > n:
            continue
        else:
            result.append(point)
    return result

# TODO: fix the diagonal movement
# TODO: plug the pizza shop correctly
def plug_pizzeria_on_map(pizza_x, pizza_y, pizza_r, city_map):
    """
    Plugging the Pizza Shop on the correct coordinate spot in the nested list; then the 
    """
    blocks = delete_points_outside_range(generate_deliverable_blocks(pizza_x, pizza_y, pizza_r, city_map), n)

    for point in blocks:
        new_x, new_y = translate_coords(point[0], point[1])
        print('[{}, {}] => [{}, {}]'.format(point[0], point[1], new_x, new_y))
        city_map[new_x][new_y] += 1
    print_map(city_map)


def generate_deliverable_blocks(pizza_x, pizza_y, pizza_r, city_map):
    # [pizza_x, pizza_y] is the centre point
    xs = vary_around(pizza_x, r)
    ys = vary_around(pizza_y, r)

    possible_point = [(x, y) for x in xs for y in ys]
    print(possible_point)
    print('Length of the possible points list: {}'.format(len(possible_point)))
    # pizza_r denotes the number of steps (blocks) that can be taken
    return possible_point

def find_max_block(city_map):
    """
    Finds maximum in each row and keeps track of the biggest value so far; maximum of all rows is returned.
    """
    current_max = 0
    for row in city_map:
        if current_max < max(row):
            current_max = max(row)
    return current_max


if __name__ == '__main__':

    # getting the input in the program for now
    n = int(input('what is the side of the map: '))
    m = int(input('Number of the Pizza Shops to plug on the map: '))

    # create the city map according to the given measurement
    city_map = [[0 for i in range(n)] for i in range(n)]

    print('Before Pizzerias are in town')
    print_map(city_map)

    pizza_shops = []
    # loop through the number of the needed Pizza Shops and get their coordinates
    for i in range(1, m+1):
        pizza_details = input('> Input Pizza Shop #{} details <x y r>: '.format(i)).split(' ')
        x, y, r = int(pizza_details[0]), int(pizza_details[1]), int(pizza_details[2])

        plug_pizzeria_on_map(x, y, r, city_map)

    max_pizza = find_max_block(city_map)
    print(max_pizza)
