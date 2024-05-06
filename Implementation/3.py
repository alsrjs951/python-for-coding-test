import sys

x_size, y_size = map(int, sys.stdin.readline().rstrip().split())
x, y, direction = map(int, sys.stdin.readline().rstrip().split())
game_map = [[] for _ in range(x_size)]
for i in range(x_size):
    game_map[i] = list(map(int, sys.stdin.readline().rstrip().split()))
steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited = list()
visited.append((x, y))
result = 1
rotate_num = 0


def turn_left():
    global direction
    direction -= 1
    if direction < 0:
        direction = 3


while True:
    turn_left()
    dx, dy = steps[direction][0], steps[direction][1]
    if game_map[x+dx][y+dy] == 0 and (x+dx, y+dy) not in visited:
        x += dx
        y += dy
        visited.append((x, y))
        result += 1
        rotate_num = 0
    else:
        rotate_num += 1
    
    if rotate_num >= 4:
        dx, dy = steps[direction][0], steps[direction][1]
        if game_map[x-dx][y-dy] == 1:
            break
        else:
            x -= dx
            y -= dy
            rotate_num = 0

print(result)
