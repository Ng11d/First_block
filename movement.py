from position import move_forward,move_backward,turn_left,turn_right,turn_up,turn_down

    n=int(input("Print the number of inputs"))
    print("Series of movement forward/backward (f, b),left/right (l, r),up/down (u, d)")
    array=[]
    for i in range(n):
        array.append(input(array[i]))
    initial_pos=[0,0,0]
    initial_direction='N'
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

