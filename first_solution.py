import numpy as np
import copy

# travel cost on each type of terrain
PATH_COST = {"#": None, "~": 800, "*": 200, "+": 150, "X": 120, "_": 100, "H": 70, "T": 50, "O": 0}

# moves definition
MOVES = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}


def read_map(path):
    m_array = []
    c_dict = {}
    with open(path, "r") as f:
        n, m, c, r = map(int, f.readline().strip("\n").split(" "))
        for i in range(c):
            line = list(map(int, f.readline().split(" ")))
            # key: (x, y) value: reward points
            c_dict[(line[1], line[0])] = line[2]
        # create map object
        for line in f.readlines():
            row = []
            for char in line.strip("\n"):
                row.append(char)
            m_array.append(row)
    return n, m, c, r, c_dict, np.array(m_array)


def insert_C(m, coord):
    for c in coord:
        m[c[0], c[1]] = "C"
    return m


def reverse_seq(seq):
    res = ""
    dic = {"R": "L", "L": "R", "U": "D", "D": "U"}
    for s in seq:
        res += dic[s]
    return res


class Node:
    def __init__(self, pos, seq, g):
        self.x = pos[1]
        self.y = pos[0]
        self.seq = seq
        self.g = g


# uniform cost search to build office
def ucs_office(root, mapp, checked, n, m):
    frontier = [root]
    visited = []

    while(frontier):
        # find most promising node
        min_cost = 100000000000
        min_index = None
        for i in range(len(frontier)):
            if frontier[i].g < min_cost:
                min_cost = frontier[i].g
                min_index = i
        # pop and return best node
        node = frontier.pop(min_index)
        # elimination of repeated states
        if (node.y, node.x) not in visited:
            visited.append((node.y, node.x))
            # goal test
            if mapp[node.y, node.x] not in ["#", "C"] and checked[node.y, node.x] != "O":
                return node
            # expand node
            for move, direc in MOVES.items():
                posx = node.x + direc[1]
                posy = node.y + direc[0]
                if posx >= 0 and posx < n and posy >= 0 and posy < m:
                    terrain = mapp[posy, posx]
                    # if terrain is walkable
                    if terrain not in ["#", "C"]:
                        seq = node.seq + move
                        cost = node.g + PATH_COST[terrain]
                        frontier.append(Node(pos=(posy, posx), seq=seq, g=cost))


# uniform cost search to reach nearest office
def ucs_customer(root, mapp, n, m):
    frontier = [root]
    visited = []

    while(frontier):
        # find most promising node
        min_cost = 100000000000
        min_index = None
        for i in range(len(frontier)):
            if frontier[i].g < min_cost:
                min_cost = frontier[i].g
                min_index = i
        # pop and return best node
        node = frontier.pop(min_index)
        # elimination of repeated states
        if (node.y, node.x) not in visited:
            visited.append((node.y, node.x))
            # goal test
            if mapp[node.y, node.x] == "O":
                return node
            # expand node
            for move, direc in MOVES.items():
                posx = node.x + direc[1]
                posy = node.y + direc[0]
                if posx >= 0 and posx < n and posy >= 0 and posy < m:
                    terrain = mapp[posy, posx]
                    # if terrain is walkable
                    if terrain not in ["#", "C"]:
                        seq = node.seq + move
                        cost = node.g + PATH_COST[terrain]
                        frontier.append(Node(pos=(posy, posx), seq=seq, g=cost))
    return None


if __name__ == "__main__":

    path_1 = "1_victoria_lake.txt"
    path_2 = "2_himalayas.txt"
    path_3 = "3_budapest.txt"
    path_4 = "4_manhattan.txt"
    path_5 = "5_oceania.txt"

    # extract variables of interest from txt file
    N, M, C, R, COORD, MAP = read_map(path_5)

    # update map with customer office "C"
    MAP = insert_C(MAP, COORD.keys())

    # copy of map to check locations
    C_MAP = copy.deepcopy(MAP)

    # first naive solution
    offices = []
    for i in range(R):
        # find best location for office
        max_reward = -100000000000
        max_pos = None
        max_seq = None
        max_place = None
        for pos, reward in COORD.items():
            root = Node(pos=pos, seq="", g=0)
            node = ucs_office(root, MAP, C_MAP, N, M)
            val = reward - node.g
            if val > max_reward:
                max_reward = val
                max_pos = (node.y, node.x)
                max_seq = reverse_seq(node.seq)
                max_place = pos
        # update map with office
        C_MAP[max_pos[0], max_pos[1]] = "O"
        offices.append((max_pos[0], max_pos[1]))

        print(max_pos[1], max_pos[0], max_seq)
