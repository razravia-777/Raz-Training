from typing import TextIO
from constants import FILE_FORMAT


def read_pbm_file(filename: TextIO) -> list[str]:
    with open(filename, 'r') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]

    return lines


def get_file_format(filename: TextIO) -> str:
    lines: list[str] = read_pbm_file(filename)
    file_format: str = lines[0]

    if file_format != FILE_FORMAT:
        raise ValueError("the format must be P1!! other formats are not supported")

    return file_format


def get_width_and_height(filename: TextIO) -> tuple[int, int]:
    lines: list[str] = read_pbm_file(filename)
    width: int = int(lines[1][0])
    height: int = int(lines[1][1])

    return width, height


def get_other_rows(filename: TextIO) -> list[str]:
    lines: list[str] = read_pbm_file(filename)

    return lines[2:]
