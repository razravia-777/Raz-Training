from logic.algorithm import read_pbm_file, write_pbm_file
from validation.format import get_all_args
from PIL import Image


def main():
    input_file, output_file, x, y = get_all_args()
    picture_data = read_pbm_file(input_file)   # הוצאת הDATA מהקובץ
    write_pbm_file(output_file, picture_data, x, y)  # צביעה של החלקים הרצויים

    img = Image.open(output_file)
    img.show()


if __name__ == '__main__':
    main()