

class Time:
    def __init__(self, hour: int, minute: int):
        self.hour = hour
        self.minute = minute


class Interval:
    def __init__(self, start_time: Time, end_time: Time):
        self.start_time = start_time
        self.end_time = end_time


class Class:
    def __init__(self, day: str, interval: Interval):
        self.day = day
        self.interval = interval


class Subject:
    def __init__(self, name: str, professor: str, classes: [Class]):
        self.name = name
        self.professor = professor
        self.classes = classes


def main():
    pass


# execute ONLY if the module is not imported:
# ex. python3 main.py
if __name__ == "__main__":
    main()
