from logic.write_to_file import write_pbm_file
from user_inputs import get_user_inputs
from PIL import Image


def main():
    input_file, output_file, x, y = get_user_inputs()
    write_pbm_file(input_file, output_file, x, y)

    img = Image.open(output_file)
    img.show()


if __name__ == '__main__':
    main()
