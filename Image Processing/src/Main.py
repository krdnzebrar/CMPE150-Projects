inp_filename, operation, out_filename = input().split()


# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
def read_imagefile(f):
    type_ = f.readline().rstrip()
    type_list = type_.split()
    width , height , max_level = int(type_list[1]) , int(type_list[2]) , int(type_list[3])
    matrix = []
    for r in range(height):
        rest = f.readline().rstrip()
        row = [int(x) for x in rest.split()]
        matrix.append(row)
    return matrix

def write_imagefile(f,matrix):
    height = len(matrix)
    width = len(matrix[0])
    f.write(f'P2 {width} {height} 255\n')
    for r in range(height):
        for c in range(width):
            f.write(str(matrix[r][c]) + ' ')
        f.write('\n')

def misalign(matrix):
    height = len(matrix)
    width = len(matrix[0])

    new_matrix = [[0] * width for i in range(height)]
    for c in range(width):
        if c % 2 == 1:
            a = 0
            r = height - 1
            while r >= 0:
                new_matrix[a][c] = matrix[r][c]
                r -= 1
                a += 1
        else:
            for r in range(height):
                new_matrix[r][c] = matrix[r][c]
    return new_matrix


def sort_columns(matrix):
    height = len(matrix)
    width = len(matrix[0])
    trans_matrix = [[0]*height for i in range(width)]
    for r in range(height):
        for c in range(width):
            trans_matrix[r][c] = matrix[c][r]
    for r in range(height):
        trans_matrix[r].sort()
    matrix = [[0]*width for i in range(height)]
    for r in range(height):
        for c in range(width):
            matrix[r][c] = trans_matrix[c][r]
    return matrix

def sort_rows_border(matrix):
    height = len(matrix)
    width = len(matrix[0])
    result = [[0] * width for i in range(height)]
    for r in range(height):
        row = []
        till0 = []
        c = 0
        while c < width:
            if matrix[r][c] == 0:
                if len(till0) > 0:
                    till0.sort()
                    row.extend(till0)
                    till0 = []
                row.append(0)
                c += 1
            else:
                till0.append(matrix[r][c])
                c += 1
        if len(till0) > 0:
            till0.sort()
            row.extend(till0)
        result[r] = row
    return result

def convolution(matrix,kernel):
    height = len(matrix)
    width = len(matrix[0])
    extended_matrix = []
    extended_matrix.append([0 for i in range(width+2)])
    for r in range(height):
        row = [0]
        row.extend(matrix[r])
        row.append(0)
        extended_matrix.append(row)
    extended_matrix.append([0 for i in range(width + 2)])
    for y in range(1,height+1):
        for x in range(1,width+1):
            sum_ = 0
            for i in range(3):
                for j in range(3):
                    mul = kernel[i][j] * extended_matrix[y-1+i][x-1+j]
                    sum_ += mul
            if sum_ > 255:
                matrix[y - 1][x - 1] = 255
            elif sum_ < 0:
                matrix[y - 1][x - 1] = 0
            else:
                matrix[y-1][x-1] = sum_
    return matrix


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
f = open(inp_filename, "r")
img_matrix = read_imagefile(f)
f.close()

if operation == "misalign":
    img_matrix = misalign(img_matrix)

elif operation == "sort_columns":
    img_matrix = sort_columns(img_matrix)

elif operation == "sort_rows_border":
    img_matrix = sort_rows_border(img_matrix)

elif operation == "highpass":
    kernel = [
        [-1, -1, -1],
        [-1, 9, -1],
        [-1, -1, -1]
    ]
    img_matrix = convolution(img_matrix, kernel)

f = open(out_filename, "w")
write_imagefile(f, img_matrix)
f.close()
