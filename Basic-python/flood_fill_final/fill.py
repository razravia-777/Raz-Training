import argparse
from algorithm import read_pbm_file, write_pbm_file
from format import check_args
import os
from PIL import Image


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="input file from user")
    parser.add_argument("output_file", help="output file from user")
    parser.add_argument("x", help="x num (still a string like '0')")  # אפשר לשנות את המשתנה ממחרוזת לINT בעזרת TYPE=INT
    parser.add_argument("y", help="y num")
    args = parser.parse_args()
    input_file = args.input_file
    output_file = args.output_file
    x = args.x
    y = args.y

    if check_args(input_file, output_file, x, y):  # בדיקת תקינות של הקלט מהמשתמש
        picture_data = read_pbm_file(input_file)  # הוצאת הDATA מהקובץ
        write_pbm_file(output_file, picture_data, x, y)  # צביעה של החלקים הרצויים
        with open (output_file, "r") as f:
            print(f.read())
        img = Image.open(output_file)
        img.show()


if __name__ == '__main__':
    main()