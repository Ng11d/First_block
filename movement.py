class Spacecraft:
    def __init__(self, int_pos, int_dir):
        self.position = int_pos
        self.direction = int_dir

    def move_forward(self):
        if self.direction == 'N':
            self.position[1] += 1
        elif self.direction == 'S':
            self.position[1] -= 1
        elif self.direction == 'E':
            self.position[0] += 1
        elif self.direction == 'W':
            self.position[0] -= 1
        elif self.direction == 'Up':
            self.position[2] += 1
        elif self.direction == 'Down':
            self.position[2] -= 1

    def move_backward(self):
        if self.direction == 'N':
            self.position[1] -= 1
        elif self.direction == 'S':
            self.position[1] += 1
        elif self.direction == 'E':
            self.position[0] -= 1
        elif self.direction == 'W':
            self.position[0] += 1
        elif self.direction == 'Up':
            self.position[2] -= 1
        elif self.direction == 'Down':
            self.position[2] += 1

    def turn_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'W':
            self.direction = 'S'

    def turn_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'W':
            self.direction = 'N'

    def turn_up(self):
        if self.direction == 'N':
            self.direction = 'Up'
        elif self.direction == 'S':
            self.direction = 'Down'
        elif self.direction == 'E' or self.direction == 'W':
            pass

    def turn_down(self):
        if self.direction == 'N':
            self.direction = 'Down'
        elif self.direction == 'S':
            self.direction = 'Up'
        elif self.direction == 'E' or self.direction == 'W':
            pass


def execute_commands(spacecraft, command_array):
    for command in command_array:
        if command == 'f':
            spacecraft.move_forward()
        elif command == 'b':
            spacecraft.move_backward()
        elif command == 'l':
            spacecraft.turn_left()
        elif command == 'r':
            spacecraft.turn_right()
        elif command == 'u':
            spacecraft.turn_up()
        elif command == 'd':
            spacecraft.turn_down()


initial_position = [0, 0, 0]
initial_direction = 'N'
commands = ['f', 'r', 'u', 'b', 'l']

cn = Spacecraft(initial_position, initial_direction)
execute_commands(cn, commands)

print("Final position:", cn.position)
print("Final direction:", cn.direction)
