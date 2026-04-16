from logic.reading_file import get_width_and_height


def check_x_y_inputs(input_file, x, y):
    if not x.isdigit() or not y.isdigit():
        raise TypeError("please input correct format, x and y must be *Numbers* \n try again")
    if not check_file_bounderys(input_file, int(x), int(y)):
        raise ValueError("x and y must be in the picture bounderys \n try again")


def check_file_bounderys(filename, x, y):
    x_boundery, y_boundery = get_width_and_height(filename)

    return 0 <= x < x_boundery and 0 <= y < y_boundery
