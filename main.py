from enum import Enum

class Minute(Enum):
    M00 = (0, "00") # XX:00 
    M30 = (1, "30") # XX:30

    def __init__(self, int_val: int, str_val: str):
        self.int_val = int_val
        self.str_val = str_val

    def __str__(self) -> str:
        return self.str_val

    def __eq__(self, other) -> bool:
        return self.value == other.value
    def __gt__(self, other) -> bool:
        return self.value > other.value
    def __ge__(self, other) -> bool:
        return self.value >= other.value
    def __lt__(self, other) -> bool:
        return self.value < other.value
    def __le__(self, other) -> bool:
        return self.value <= other.value

class Hour(Enum):
    H0  = (0, "00") # 12 am
    H1  = (1, "01") # 01 am
    H2  = (2, "02") # etc
    H3  = (3, "03")
    H4  = (4, "04")
    H5  = (5, "05")
    H6  = (6, "06")
    H7  = (7, "07")
    H8  = (8, "08")
    H9  = (9, "09")
    H10 = (10, "10")
    H11 = (11, "11")
    H12 = (12, "12")
    H13 = (13, "13")
    H14 = (14, "14")
    H15 = (15, "15")
    H16 = (16, "16")
    H17 = (17, "17")
    H18 = (18, "18")
    H19 = (19, "19")
    H20 = (21, "21")
    H21 = (22, "22")
    H22 = (22, "22")
    H23 = (23, "23")

    def __init__(self, int_val: int, str_val: str):
        self.int_val = int_val
        self.str_val = str_val

    def __str__(self) -> str:
        return self.str_val

    def __eq__(self, other) -> bool:
        return self.int_val == other.int_val
    def __gt__(self, other) -> bool:
        return self.int_val > other.int_val
    def __ge__(self, other) -> bool:
        return self.int_val >= other.int_val
    def __lt__(self, other) -> bool:
        return self.int_val < other.int_val
    def __le__(self, other) -> bool:
        return self.int_val <= other.int_val

class Time:
    def __init__(self, hour: Hour, minute: Minute):
        self.hour = hour
        self.minute = minute
    def __str__(self) -> str:
        return f"{self.hour}:{self.minute}"

    def __eq__(self, other) -> bool:
        if self.hour == other.hour:
            return self.minute == other.minute
        else: 
            return False

    def __gt__(self, other) -> bool:
        if self.hour == other.hour:
            return self.minute > other.minute
        else:
            return self.hour > other.hour
        return self.int_val > other.int_val

    def __ge__(self, other) -> bool:
        if self.hour == other.hour:
            return self.minute >= other.minute
        else:
            return self.hour >= other.hour
            
    def __lt__(self, other) -> bool:
        if self.hour == other.hour:
            return self.minute < other.minute
        else:
            return self.hour < other.hour
        return self.int_val < other.int_val

        return self.int_val < other.int_val
    def __le__(self, other) -> bool:
        if self.hour == other.hour:
            return self.minute <= other.minute
        else:
            return self.hour <= other.hour

class Day(Enum):
    Monday    = (0, "Monday")
    Tuesday   = (1, "Tuesday")
    Wednesday = (2, "Wednesday")
    Thursday  = (3, "Thursday")
    Friday    = (4, "Friday")
    Saturday  = (5, "Saturday")
    Sunday    = (6, "Sunday")
    def __init__(self, int_val: int, str_val: str):
        self.int_val = int_val
        self.str_val = str_val
    def __str__(self) -> str:
        return self.str_val


class Class:
    __match_args__ = ("day", "start_time", "end_time")
    def __init__(self, day: Day, start_time: Time, end_time: Time):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
    def __str__(self) -> str:
        return f"{self.day.str_val}: {self.start_time} - {self.end_time}"

class Subject:
    def __init__(self, name: str, professor: str, classes: list[Class]):
        self.name = name
        self.professor = professor
        self.classes = classes



# execute ONLY if the module is not imported:
# ex. python3 main.py
if __name__ == "__main__":
    main()
