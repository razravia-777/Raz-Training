import os


def check_files_inputs(input_file, output_file):
    if not files_endswith_pbm(input_file, output_file):
        raise ValueError("please input a .pbm file \n try again")
    if not os.path.exists(input_file):
        raise FileNotFoundError("file path doesnt exist, please input correct file, \n try again")


def files_endswith_pbm(filename1, filename2):
    return filename1.endswith(".pbm") and filename2.endswith(".pbm")
