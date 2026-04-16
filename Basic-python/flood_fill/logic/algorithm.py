from constants import FILLED_COLOR, UNFILLED_COLOR
from logic.reading_file import get_other_rows, get_width_and_height

def add_color(input_file, x, y):
    rows = get_other_rows(input_file)
    width, height = get_width_and_height(input_file)
    matrix = [list(row) for row in rows]
    check_points = [(x, y)]

    return painting(matrix, check_points, width, height)


def painting(matrix, check_points, width, height):
    while check_points:
        x, y = check_points.pop()
        if 0 <= x < width and 0 <= y < height:
            if matrix[y][x] == UNFILLED_COLOR:
                matrix[y][x] = FILLED_COLOR
                check_points.append((x, y + 1))
                check_points.append((x, y - 1))
                check_points.append((x + 1, y))
                check_points.append((x - 1, y))

    return matrix
