from logic.algorithm import add_color
from logic.reading_file import get_file_format, get_width_and_height


def write_pbm_file(input_file, output_file, x, y):
    matrix: list[list[str]] = add_color(input_file, int(x), int(y))
    format: str = get_file_format(input_file)
    width, height = get_width_and_height(input_file)

    with open(output_file, 'w') as f:
        f.write(f"{format}\n")
        f.write(f"{width} {height}\n")
        for row in matrix:
            f.write( "".join(row) + "\n")
