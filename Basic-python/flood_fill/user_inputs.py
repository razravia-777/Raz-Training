import argparse
from validation.format import check_args


def get_user_inputs():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="input file from user")
    parser.add_argument("output_file", help="output file from user")
    parser.add_argument("x", help="x num (still a string like '0')")
    parser.add_argument("y", help="y num")
    args = parser.parse_args()

    check_args(args.input_file, args.output_file, args.x, args.y)

    return args.input_file, args.output_file, args.x, args.y
