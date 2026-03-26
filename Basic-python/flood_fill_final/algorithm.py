from constants import FILLED_COLOR, UNFILLED_COLOR


def read_pbm_file(filename):
    """
    this func returns a dict with all the file data,
    format, width, height and rows (picture data)
    in the list lines:
        [0] - format
        [1] - width and height
        [1][0] - width
        [1][1] - height
        [2:] - rows and pic data
    :param filename:
    :return: list, each index is a row of the pbm file
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]  #ניקוי התוכן מרווחים ותווים מיוחדים + הכנסה לרשימה כל שורה באיבר
    data = {"format": lines[0], "width": int(lines[1][0]), "height": int(lines[1][1]), "rows": lines[2:]}
    if data["format"] != "P1":
        print("please input correct format")
        return {}  #מחזיר מילון ריק לכן הפעולה בהמשך לא תתקיים עם מילון ריק
    return data

def write_pbm_file(filename, data, x, y):
    """
    this func writes to the pbm file
    :param filename: the filename of the pbm file
    :param data: format, width, height and rows (picture data)
    :param x: x of the given point
    :param y: y of the given point
    :return: none
    """
    matrix = add_color(data, int(x), int(y))

    with open(filename, 'w') as f:
        f.write(f"{data["format"]}\n")  #format  # f.write("P1\n")  #יש פורמט קבוע ובדקתי למעלה שהוא מתקיים
        f.write(f"{data["width"]} {data["height"]}\n")  #width and height
        for row in matrix:
            f.write( "".join(row) + "\n")

def add_color(data, x, y):
    """
    this func adds color to the matrix,
    and paint all the points around (x, y), until its the edge of the page
    or the point is already filled
    :param data: format, width, height and rows (picture data)
    :param x: x of the given point
    :param y: y of the given point
    :return: new list with others
    """
    rows = data["rows"]
    matrix = [list(row) for row in rows]  # הכנסה לרשימה דו ממדית
    check_list = [(x, y)]  # אינדקסים של נק' הבדיקה הראשונית שקיבלתי מהמשתמש

    while check_list:
        x, y = check_list.pop()
        if 0 <= x < data["width"] and 0 <= y < data["height"]:  # בודק שהנקודה נמצאת בתחום
            if matrix[y][x] == UNFILLED_COLOR:
                matrix[y][x] = FILLED_COLOR
                check_list.append((x, y + 1))  # מוסיף שכנים אם הנק רלוונטית וצבעתי אותה
                check_list.append((x, y - 1))
                check_list.append((x + 1, y))
                check_list.append((x - 1, y))
    return matrix