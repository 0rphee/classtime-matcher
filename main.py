import itertools
from enum import Enum
from typing import Tuple
import csv
# enum docs: https://docs.python.org/3/howto/enum.html#when-to-use-new-vs-init
# csv docs: https://docs.python.org/3/library/csv.html

class Minute(Enum):
    # the int value is for comparing with <, ==, <=, >=
    # the str value is for printing the value
    M00 = "00" # XX:00 
    M30 = "30" # XX:30

    def __init__(self, str_val: str):
        # makes "00" accessible
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
    # the str value is for printing the value
    H0  = "00" # 12 am
    H1  = "01" # 01 am
    H2  = "02" # etc
    H3  = "03"
    H4  = "04"
    H5  = "05"
    H6  = "06"
    H7  = "07"
    H8  = "08"
    H9  = "09"
    H10 = "10"
    H11 = "11"
    H12 = "12"
    H13 = "13"
    H14 = "14"
    H15 = "15"
    H16 = "16"
    H17 = "17"
    H18 = "18"
    H19 = "19"
    H20 = "21"
    H21 = "22"
    H22 = "22"
    H23 = "23"

    def __init__(self, str_val: str):
        # makes (0, "00") accessible individually
        self.str_val = str_val

# Enables obtaining a string representation of an Hour object
# Returns the string value of the hour, e.g., "01" for Hour.H1
    def __str__(self) -> str:
        return self.str_val

# Enables using the '==' operator to compare two Hour objects for equality
    def __eq__(self, other) -> bool:
        return self.str_val == other.str_val

# Enables using the '>' operator to compare if one Hour object is greater than another
    def __gt__(self, other) -> bool:
        return self.str_val > other.str_val

# Enables using the '>=' operator to compare if one Hour object is greater than or equal to another
    def __ge__(self, other) -> bool:
        return self.str_val >= other.str_val

# Enables using the '<' operator to compare if one Hour object is less than another
    def __lt__(self, other) -> bool:
        return self.str_val < other.str_val

# Enables using the '<=' operator to compare if one Hour object is less than or equal to another
    def __le__(self, other) -> bool:
        return self.str_val <= other.str_val

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

def parseHour(text: str) -> Hour:
    # Parses the hour from a given text and returns the corresponding Hour object
    match text[0]:
        case "0":
            return eval(f"Hour.H{text[1]}")
        case "1":
            return eval(f"Hour.H{text}")
        case "2":
            match text[1]:
                case "0" | "1" | "2" | "3":
                    return eval(f"Hour.H{text}")
    raise ValueError(f"parseHour error: {text}")

            
def parseMinute(text: str) -> Minute:
    # Parses the minute from a given text and returns the corresponding Minute object
    match text:
        case "00":
            return Minute.M00
        case "30":
            return Minute.M30
    raise ValueError("parseHour error")


# Parses the start and end times from a given text and returns them as Time objects
# Returns a tuple of two Time objects if the text is not "NULL", otherwise returns None
def parseTime(text: str) -> Tuple[Time, Time] | None:
    if text != "NULL":
        start_hour: Hour = parseHour(text[:2])
        start_min: Minute = parseMinute(text[3:5])
        end_hour: Hour = parseHour(text[6:8])
        end_min: Minute = parseMinute(text[9:11])
        return Time(start_hour, start_min), Time(end_hour, end_min)
    return None
#Parses the list of class schedules for each day and returns a list of Class objects
# Returns a list of Class objects if at least one class is parsed, otherwise returns None
def parseClasses(days: list[str]) -> list[Class] | None:
    classes: list[Class] = []
    for i, val in zip(range(7),days):
        if i == 0:
            const = Day.Monday
        elif i == 1:
            const = Day.Tuesday
        elif i == 2:
            const = Day.Wednesday
        elif i == 3:
            const = Day.Thursday
        elif i == 4:
            const = Day.Friday
        elif i == 5:
            const = Day.Saturday
        elif i == 6:
            const = Day.Sunday
        if (interval := parseTime(val)) is not None:
            classes.append(Class(const, interval[0], interval[1]))
    if classes:
        return classes
    return None

# Reads a subject file from the given filepath and extracts the subject data
# Returns a list of Subject objects containing the subject name, professor, key, and class schedules
def readSubjectFile(filepath: str) -> list[Subject] | None:
    subjects : list[Subject] = []
    with open(filepath, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            name, prof, key = row[0], row[1], row[2]
            classes = parseClasses(row[3:])
            if classes is not None:
                subjects.append(Subject(name, prof, key, classes))
    if subjects:
        return subjects
    return None

# Possible schedules generated from the classes. This will be done with the itertools function
# called 'product()' which is going to give us all the possible iterations of the schedules available.
# To validate that each schedule is valid, the function 'classesOverlap' is called to check if
# each possible pair of classes overlap.

# Creates a class which is going to produce all the possile iterations of the schedules posible.
def possibleIterations(subjects: list[Subject]) -> list[list[Subject]] | None:
    # Creates a list of all the possible iterations of the schedules
    possibleSchedules = list(itertools.product(*[subject.classes for subject in subjects]))
    # Checks if the schedules overlap
    possibleSchedules = [schedule for schedule in possibleSchedules if not any(classesOverlap(*classes) for classes in itertools.combinations(schedule, 2))]
    # Returns a list of lists of Subject objects if at least one schedule is possible, otherwise returns None
    if possibleSchedules:
        return possibleSchedules
    return None

# Finally, it will return a list and show of all the possible schedules which do not overlap.
# Prints all the possible schedules
def printPossibleSchedules(subjects: list[Subject]) -> None:
    if (possibleSchedules := possibleIterations(subjects)) is not None:
        for schedule in possibleSchedules:
            print(*schedule, sep="\n")
    else:
        print("No possible schedules")

        
# tests
def main() -> None:
    for subj in readSubjectFile("intermedio.csv"):
        print(subj)


# execute ONLY if the module is not imported:
# ex. python3 main.py
if __name__ == "__main__":
    main()
