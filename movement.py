

initial_pos=[0,0,0]
initial_direction='S'


def move_forward(position,direction):
    if direction == 'N':
        position[1] += 1
    elif direction == 'S':
        position[1] -= 1
    elif direction == 'E':
        position[0] += 1
    elif direction == 'W':
        position[0] -= 1
    elif direction == 'Up':
        position[2] += 1
    elif direction == 'Down':
        position[2] -= 1


def move_backward(position, direction):
    if direction == 'N':
        position[1] -= 1
    elif direction == 'S':
        position[1] += 1
    elif direction == 'E':
        position[0] -= 1
    elif direction == 'W':
        position[0] += 1
    elif direction == 'Up':
        position[2] -= 1
    elif direction == 'Down':
        position[2] += 1


def turn_left(direction):
    if direction == 'N':
        direction = 'W'
    elif direction == 'S':
        direction = 'E'
    elif direction == 'E':
        direction = 'N'
    elif direction == 'W':
        direction = 'S'


def turn_right(direction):
    if direction == 'N':
        direction = 'E'
    elif direction == 'S':
        direction = 'W'
    elif direction == 'E':
        direction = 'S'
    elif direction == 'W':
        direction = 'N'


def turn_up(direction):
    if direction == 'N':
        direction = 'Up'
    elif direction == 'S':
        direction = 'Down'
    elif direction == 'E' or direction == 'W':
         pass


def turn_down(direction):
    if direction == 'N':
        direction = 'Down'
    elif direction == 'S':
        direction = 'Up'
    elif direction == 'E' or direction == 'W':
        pass


def execute_commands(array):
    for command in array:
        if command == 'f':
            move_forward(initial_pos,initial_direction)
        elif command == 'b':
            move_backward(initial_pos,initial_direction)
        elif command == 'l':
            turn_left(initial_direction)
        elif command == 'r':
            turn_right(initial_direction)
        elif command == 'u':
            turn_up(initial_direction)
        elif command == 'd':
            turn_down(initial_direction)


execute_commands(['f', 'b', 'r', 'b', 'f'])
print(initial_pos)
print(initial_direction)