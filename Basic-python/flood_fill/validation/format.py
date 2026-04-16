from validation.file_validation import check_files_inputs
from validation.args_validation import check_x_y_inputs


def check_args(input_file, output_file, x, y):
    check_files_inputs(input_file, output_file)
    check_x_y_inputs(input_file, x, y)
