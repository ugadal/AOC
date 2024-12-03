from collections import defaultdict


puzzle_input_str = open("d23.txt").read().split("\n\n")[1]
test_input_str = """pos=<0,0,0>, r=4
pos=<1,0,0>, r=1
pos=<4,0,0>, r=3
pos=<0,2,0>, r=1
pos=<0,5,0>, r=3
pos=<0,0,3>, r=1
pos=<1,1,1>, r=1
pos=<1,1,2>, r=1
pos=<1,3,1>, r=1"""


def parse_line(line):
	pos_str, r_str = line.split(", ")
	x,y,z = [int(c) for c in pos_str[5:-1].split(",")]
	r = int(r_str[2:])
	return (x,y,z,r)


def parse_input(input_str):
    return [ parse_line(line) for line in input_str.split("\n")]


def is_in_range(ax, ay, az, bx, by, bz, r):
    return r >= abs(ax - bx) + abs(ay - by) + abs(az - bz)


def calc_in_range(bots):
    in_range = defaultdict(set)
    j_max = len(bots)
    
    for i, (x,y,z,r) in enumerate(bots):
        
        j = i + 1
        in_range[i].add(i)
        while j < j_max:
            bx, by, bz, br = bots[j]

            if is_in_range(x, y, z, bx, by, bz, r):
                in_range[i].add(j)
                
            if is_in_range(x, y, z, bx, by, bz, br):
                in_range[j].add(i)
                
            j += 1
    
    return in_range


def part_one(input_str):
    bots = list(parse_input(input_str))
    
    max_index = None
    max_radius = 0
    
    ranges = calc_in_range(bots)

    for i, (x,y,z,r) in enumerate(bots):
        if r > max_radius:
            max_index = i
            max_radius = r
    
    return len(ranges[max_index])
        
assert 7 == part_one(test_input_str)

print("part one:", part_one(puzzle_input_str))


import math
from heapq import heappush, heappop


test_input_str_2 = """pos=<10,12,12>, r=2
pos=<12,14,12>, r=2
pos=<16,12,12>, r=4
pos=<14,14,14>, r=6
pos=<50,50,50>, r=200
pos=<10,10,10>, r=5"""


cube_deltas = (
    (0, 0, 0),
    (0, 0, 1),
    (0, 1, 0),
    (0, 1, 1),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 0),
    (1, 1, 1)
)


def calculate_initial_search_cube(bots):
    max_x = max_y = max_z = -math.inf
    min_x = min_y = min_z = math.inf
    
    for x,y,z,r in bots:
        max_x = max(x, max_x)
        max_y = max(y, max_y)
        max_z = max(z, max_z)
        
        min_x = min(x, min_x)
        min_y = min(y, min_y)
        min_z = min(z, min_z)
        
    min_side_length = max(
        abs(max_x - min_x),
        abs(max_y - min_y),
        abs(max_z - min_z)
    )
    
    # find a power of two, so subdividing the cube is cleaner
    side_length = 2
    while 1 + side_length < min_side_length:
        side_length *= 2
    
    return min_x, min_y, min_z, side_length


def cube_corners(x, y, z, sz):
    sz -= 1
    return list(
        (x+(dx*sz), y+(dy*sz), z+(dz*sz))
        for dx, dy, dz in cube_deltas
    )


def bot_extremities(bot):
    x, y, z, r = bot
    return (
        (x+r, y,   z),
        (x-r, y,   z),
        (x,   y+r, z),
        (x,   y-r, z),
        (x,   y,   z+r),
        (x,   y,   z-r)
    )


def subdivide_search_cube(x, y, z, sz):   
    assert sz != 0, "Cannot subdivide a cube of size 1, I must have broken something"
    sz = sz // 2
    for dx, dy, dz in cube_deltas:
        yield (x+(sz*dx), y+(sz*dy), z+(sz*dz), sz)
    

# the following might seem stupid and redundant but they are different
# - cube_intersects_bot: check if any cube corners are within manhattan range of bot centre
# - bot_intersects_cube: check if any bot extremities lie within the cube
def cube_intersects_bot(cube, bot):
    bx, by, bz, r = bot
    cx, cy, cz, sz = cube
    for x, y, z in cube_corners(cx, cy, cz, sz):
        if is_in_range(bx, by, bz, x, y, z, r):
            return True
    return False


def bot_intersects_cube(bot, cube):
    bx, by, bz, r = bot
    cx, cy, cz, sz = cube

    cx_max = cx + sz
    cy_max = cy + sz
    cz_max = cz + sz
    
    for x, y, z in bot_extremities(bot):
        x_inside = cx_max > x and cx <= x
        y_inside = cy_max > y and cy <= y
        z_inside = cz_max > z and cz <= z
        if x_inside and y_inside and z_inside:
            return True
        
    return False


def bots_in_cube(bots, cube):
    return sum(
        1 for bot
        in bots
        if bot_intersects_cube(bot, cube) or cube_intersects_bot(cube, bot)
    )


def add_search_cube(queue, nbots, x, y, z, sz):
    heappush(queue, (-nbots, sz, abs(x) + abs(y) + abs(z), x, y, z))


def part_two(input_str):
    bots = list(parse_input(input_str))
    cube = calculate_initial_search_cube(bots)

    queue = []
    add_search_cube(queue, len(bots), *cube)
    # ~ print(queue)
    # ~ exit()

    while any(queue):
        bots_in_range, sz, _, x, y, z = heappop(queue)        
        
        if sz == 1:
            return x + y + z
            
        else:
            for nx, ny, nz, nsz in subdivide_search_cube(x, y, z, sz):
                nb = bots_in_cube(bots, (nx, ny, nz, nsz))
                if nb != 0:
                    add_search_cube(queue, nb, nx, ny, nz, nsz)
    
    return None

print("part two:", part_two(puzzle_input_str))
