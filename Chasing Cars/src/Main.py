car_height = int(input())
car_length = int(input())
man_height = int(input())
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

frames = 16 + car_length

for frame in range(frames):
    matrix = []
    for i in range(man_height + 8):
        row = []
        for i in range(car_length + 15):
            row.append(' ')
        matrix.append(row)
    matrix[0][:5] = ['X', 'X', 'X', 'X', 'X']
    matrix[1][0] = 'X'
    matrix[1][4] = 'X'
    matrix[2][0] = 'X'
    matrix[2][4] = 'X'
    matrix[3][:5] = ['X', 'X', 'X', 'X', 'X']
    matrix[4][2] = 'X'
    matrix[5][:5] = ['X', 'X', 'X', 'X', 'X']
    for i in range(man_height):
        matrix[6 + i][2] = 'X'
    matrix[6 + man_height][1] = 'X'
    matrix[6 + man_height][3] = 'X'
    matrix[7 + man_height][0] = 'X'
    matrix[7 + man_height][4] = 'X'

    for x in range(car_length):
        if 15 - frame + x >= 0:
            matrix[5 + man_height - car_height][15 - frame + x] = 'X'
    for y in range(car_height-2):
        if 15 - frame >= 0:
            matrix[6 + man_height - car_height + y][15 - frame] = 'X'
        for i in range(car_length-2):
            if 16 - frame + i >= 0:
                matrix[6 + man_height - car_height + y][16 - frame + i] = ' '
        if 14 - frame + car_length >= 0:
            matrix[6 + man_height - car_height + y][14 - frame + car_length] = 'X'
    for x in range(car_length):
        if 15 - frame + x >= 0:
            matrix[5 + man_height -1][15 - frame + x] = 'X'

    for i in range(man_height + 8):
        for j in range(car_length + 15):
            print(matrix[i][j], end='')
        print()
    print()
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
