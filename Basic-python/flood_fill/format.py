import os


def check_args(input_file, output_file, x, y):
    # בודק שהקובץ קריאה שנתנו לי קיים ומסתיים בסיומת המתאימה
    # בנוסף בודק ששם הקובץ שנתנו לי מסתיים עם סיומת מתאימה PBM לא חייב להיות קיים מראש אני יכול ליצור כזה בהרצה עצמה
    if not input_file.endswith(".pbm") or not output_file.endswith(".pbm"):
        raise ValueError("please input a .pbm file \n try again")
    if not os.path.exists(input_file):
        raise FileNotFoundError("file path doesnt exist, please input correct file, \n try again")
    if not x.isdigit() or not y.isdigit():  # הקלט נקלט כמחרוזת אז אני בודק שהמחרוזת היא רק מספר
        raise TypeError("please input correct format, x and y must be *Numbers* \n try again")
    return True  #אם אין שגיאות כל הקלטים תקינים ואפשר להמשיך