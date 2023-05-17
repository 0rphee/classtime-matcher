from enum import Enum
# enum docs: https://docs.python.org/3/howto/enum.html#when-to-use-new-vs-init

class Minute(Enum):
    # the int value is for comparing with <, ==, <=, >=
    # the str value is for printing the value
    M00 = (0, "00") # XX:00 
    M30 = (1, "30") # XX:30

    def __init__(self, int_val: int, str_val: str):
        # makes (0, "00") accessible individually
        self.int_val = int_val
        self.str_val = str_val

# Enables obtaining a string representation of a Minute object
# used in 'print(Minute.M00)', f"time: {Minute.M00}"
    def __str__(self) -> str:
        return self.str_val

# Enables using the '==' operator to compare two Minute objects for equality
    def __eq__(self, other) -> bool:
        return self.value == other.value

# Enables using the '>' operator to compare if one Minute object is greater than another
# Comparisons are based on hours and minutes
    def __gt__(self, other) -> bool:
        return self.value > other.value

# Enables using the '>=' operator to compare if one Minute object is greater than or equal to another
# Comparisons are based on hours and minutes
    def __ge__(self, other) -> bool:
        return self.value >= other.value

# Enables using the '<' operator to compare if one Minute object is less than another
# Comparisons are based on hours and minutes            
    def __lt__(self, other) -> bool:
        return self.value < other.value

# Enables using the '<=' operator to compare if one Minute object is less than another
# Comparisons are based on hours and minutes            
    def __le__(self, other) -> bool:
        return self.value <= other.value

class Hour(Enum):
    # the int value is for comparing with <, ==, <=, >=
    # the str value is for printing the value
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
        # makes (0, "00") accessible individually
        self.int_val = int_val
        self.str_val = str_val

# Enables obtaining a string representation of an Hour object
# Returns the string value of the hour, e.g., "01" for Hour.H1
    def __str__(self) -> str:
        return self.str_val

# Enables using the '==' operator to compare two Hour objects for equality
    def __eq__(self, other) -> bool:
        return self.int_val == other.int_val

# Enables using the '>' operator to compare if one Hour object is greater than another
    def __gt__(self, other) -> bool:
        return self.int_val > other.int_val

# Enables using the '>=' operator to compare if one Hour object is greater than or equal to another
    def __ge__(self, other) -> bool:
        return self.int_val >= other.int_val

# Enables using the '<' operator to compare if one Hour object is less than another
    def __lt__(self, other) -> bool:
        return self.int_val < other.int_val

# Enables using the '<=' operator to compare if one Hour object is less than or equal to another
    def __le__(self, other) -> bool:
        return self.int_val <= other.int_val

# Define a class to represent time (xx:yy, 10:30)
class Time:
    def __init__(self, hour: Hour, minute: Minute):
        self.hour = hour
        self.minute = minute
    def __str__(self) -> str:
        return f"{self.hour}:{self.minute}"

# Enables using the '==' operator to compare two Time objects for equality
    def __eq__(self, other) -> bool:
        if self.hour == other.hour:
            return self.minute == other.minute
        else: 
            return False

# Enables using the '>' operator to compare if one Time object is greater than another
# Comparisons are based on hours and minutes
    def __gt__(self, other) -> bool:
        if self.hour == other.hour:
            return self.minute > other.minute
        else:
            return self.hour > other.hour

# Enables using the '>=' operator to compare if one Time object is greater than or equal to another
# Comparisons are based on hours and minutes
    def __ge__(self, other) -> bool:
        if self.hour == other.hour:
            return self.minute >= other.minute
        else:
            return self.hour >= other.hour

# Enables using the '<' operator to compare if one Time object is less than another
# Comparisons are based on hours and minutes            
    def __lt__(self, other) -> bool:
        if self.hour == other.hour:
            return self.minute < other.minute
        else:
            return self.hour < other.hour

# Enables using the '<=' operator to compare if one Time object is less than or equal to another
# Comparisons are based on hours and minutes
    def __le__(self, other) -> bool:
        if self.hour == other.hour:
            return self.minute <= other.minute
        else:
            return self.hour <= other.hour

# Define an enumeration for days
class Day(Enum):
    Monday    = "Monday"
    Tuesday   = "Tuesday"
    Wednesday = "Wednesday"
    Thursday  = "Thursday"
    Friday    = "Friday"
    Saturday  = "Saturday"
    Sunday    = "Sunday"
    def __init__(self, str_val: str):
        self.str_val = str_val
    def __str__(self) -> str:
        return self.str_val

# Define a class to represent a class (class session, monday 10:30 - 11:30)
class Class:
    __match_args__ = ("day", "start_time", "end_time")
    def __init__(self, day: Day, start_time: Time, end_time: Time):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
    def __str__(self) -> str:
        return f"{self.day.str_val}: {self.start_time} - {self.end_time}"

# Define a class to represent a subject (name: poo, prof: ivan, classes: [monday 10:00-11:00, etc]))
class Subject:
    def __init__(self, name: str, professor: str, key: str, classes: list[Class]):
        self.name = name
        self.professor = professor
        self.key = key
        self.classes = classes
    def __str__(self) -> str:
        return f"{self.name}, {self.professor}, {self.key}, [{','.join(map(lambda x: x.__str__(), self.classes))}]"

# Check if two classes overlap in time 
def classesOverlap(class1: Class, class2: Class):

    # checks if the classes are on the same day: Monday - Monday, etc.
    if class1.day is class2.day:
        # if they start at the same time and end at the same time, they overlap
        cond1 = (class1.start_time == class2.start_time) & (class1.end_time  == class2.end_time)
        # if the starting time of class2 is between de start_time and end_time of class1 
        cond2 = (class1.start_time <  class2.start_time) & (class2.start_time < class1.end_time)
        # if the ending time of class2 is between de start_time and end_time of class1 
        cond3 = (class1.start_time <  class2.end_time)   & (class2.end_time   < class1.end_time)
        # if the starting time of class1 is between de start_time and end_time of class2
        cond4 = (class2.start_time <  class1.start_time) & (class1.start_time < class2.end_time)
        # if the ending time of class1 is between de start_time and end_time of class2
        cond5 = (class2.start_time <  class1.end_time)   & (class1.end_time   < class2.end_time)

        # if any of this conditions is True, then the classes overlap
        return (cond1 | cond2 | cond3 | cond4 | cond5 | cond5) 
    else:
        return False


# tests
def main() -> None:
    print(Class(Day.Monday, Time(Hour.H10, Minute.M00), Time(Hour.H11, Minute.M30))) # testing
    print(Hour.H1.str_val)
    print(Hour.H0 < Hour.H1)
    print(Hour.H0, Hour.H0 >= Hour.H0, Hour.H0)
    print(Time(Hour.H10, Minute.M30))
    print(Time(Hour.H10, Minute.M00) > Time(Hour.H11, Minute.M30))
    print("Classes overlap ", classesOverlap(
        Class(Day.Friday, Time(Hour.H10, Minute.M00), Time(Hour.H11, Minute.M30)),
        Class(Day.Friday, Time(Hour.H0, Minute.M30), Time(Hour.H11, Minute.M30)),
    ))


# execute ONLY if the module is not imported:
# ex. python3 main.py
if __name__ == "__main__":
    main()
