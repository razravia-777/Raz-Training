import os
import argparse
from logic.algorithm import read_pbm_file


def get_all_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="input file from user")
    parser.add_argument("output_file", help="output file from user")
    parser.add_argument("x", help="x num (still a string like '0')")  # אפשר לשנות את המשתנה ממחרוזת לINT  בעזרת TYPE=INT
    parser.add_argument("y", help="y num")
    args = parser.parse_args()

    check_args(args.input_file, args.output_file, args.x, args.y)  # בדיקת תקינות של הקלט מהמשתמש

    return args.input_file, args.output_file, args.x, args.y


def check_args(input_file, output_file, x, y):
    check_files_inputs(input_file, output_file)
    check_x_y_inputs(input_file, x, y)


def check_files_inputs(input_file, output_file):
    if not files_endswith_pbm(input_file, output_file):
        raise ValueError("please input a .pbm file \n try again")
    if not os.path.exists(input_file):
        raise FileNotFoundError("file path doesnt exist, please input correct file, \n try again")


def check_x_y_inputs(input_file, x, y):
    if not x.isdigit() or not y.isdigit():
        raise TypeError("please input correct format, x and y must be *Numbers* \n try again")
    if not check_file_bounderys(input_file, int(x), int(y)):
        raise ValueError("x and y must be in the picture bounderys \n try again")


def files_endswith_pbm(filename1, filename2):
    return filename1.endswith(".pbm") and filename2.endswith(".pbm")


def check_file_bounderys(filename, x, y):
    x_boundery = read_pbm_file(filename)["width"]
    y_boundery = read_pbm_file(filename)["height"]

    return 0 <= x < x_boundery and 0 <= y < y_boundery