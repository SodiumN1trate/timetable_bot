import datetime
from bs4 import BeautifulSoup as bs
from datetime import datetime
from time import sleep
def get_class_name(file_name):
    soup = bs(file_name.read(), 'html.parser')
    return soup.find('text', attrs={"x": "1485", "font-size": "77.35"}).get_text()


def get_subjects(file_name, y_coords):
    soup = bs(file_name.read(), 'html.parser')
    lesson_0 = soup.find('rect', attrs={"x": "345", "y": y_coords})
    lesson_1 = soup.find('rect', attrs={"x": "542.3076923076924", "y": y_coords})
    lesson_2 = soup.find('rect', attrs={"x": "739.6153846153846", "y": y_coords})
    lesson_3 = soup.find('rect', attrs={"x": "936.9230769230769", "y": y_coords})
    lesson_4 = soup.find('rect', attrs={"x": "1134.2307692307693", "y": y_coords})
    lesson_5 = soup.find('rect', attrs={"x": "1331.5384615384617", "y": y_coords})
    lesson_6 = soup.find('rect', attrs={"x": "1528.8461538461538", "y": y_coords})
    lesson_7 = soup.find('rect', attrs={"x": "1726.1538461538462", "y": y_coords})
    lesson_8 = soup.find('rect', attrs={"x": "1923.4615384615386", "y": y_coords})
    lesson_9 = soup.find('rect', attrs={"x": "2120.769230769231", "y": y_coords})
    lesson_10 = soup.find('rect', attrs={"x": "2318.0769230769233", "y": y_coords})
    lesson_11 = soup.find('rect', attrs={"x": "2515.3846153846157", "y": y_coords})
    lesson_12 = soup.find('rect', attrs={"x": "2712.6923076923076", "y": y_coords})
    lessons = [lesson_0, lesson_1, lesson_2, lesson_3, lesson_4, lesson_5,
               lesson_6, lesson_7, lesson_8, lesson_9, lesson_10, lesson_11, lesson_12]
    for lesson in lessons:
        if lesson == None:
            lessons[lessons.index(lesson)] = "Stundas nav, apskaties stundu sarakstā!"
        else:
            lessons[lessons.index(lesson)] = lesson.get_text().replace("\t", "")
    return lessons


alert_time = ["7:40", "8:25", "9:10", "10:5", "10:50", "17:24", "17:22", "17:23", "14:0", "14:45", "15:30", "16:15", "16:55" ]
lesson_start_time = ["7:45", "8:30", "9:15", "10:10", "10:55", "11:45", "12:30", "13:20", "14:5", "14:50", "15:35", "16:20", "17:0"]
lesson_finish_time = ["8:25", "9:10", "9:55", "10:50", "11:35", "12:25", "13:10", "14:0", "14:45", "15:30", "16:15", "17:0", "17:40"]


# print(get_subjects(open("DP2_3_timetable.html", "r", encoding="utf8"), "1644"))
