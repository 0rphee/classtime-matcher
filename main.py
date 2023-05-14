

class Time:
    def __init__(self, hour: int, minute: int):
        self.hour = hour
        self.minute = minute
    def __str__(self):
        return f"{self.hour}:{self.minute}"

class Class:
    __match_args__ = ("start_time", "end_time")
    def __init__(self, start_time: Time, end_time: Time):
        self.start_time = start_time
        self.end_time = end_time
    def __build__str__(self, day: str):
        return f"{day}: {self.start_time} - {self.end_time}"

class MondayClass(Class):
    def __str__(self):
        return super().__build__str__("Monday")

class TuesdayClass(Class):
    def __str__(self):
        return super().__build__str__("Tuesday")

class WednesdayClass(Class):
    def __str__(self):
        return super().__build__str__("Wednesday")

class ThursdayClass(Class):
    def __str__(self):
        return super().__build__str__("Thursday")

class FridayClass(Class):
    def __str__(self):
        return super().__build__str__("Friday")

class SaturdayClass(Class):
    def __str__(self):
        return super().__build__str__("Saturday")

class SundayClass(Class):
    def __str__(self):
        return super().__build__str__("Sunday")

class Subject:
    def __init__(self, name: str, professor: str, classes: list[Class]):
        self.name = name
        self.professor = professor
        self.classes = classes

def main():
    print(MondayClass(Time(10, 30), Time(12, 20)))
    pass


# execute ONLY if the module is not imported:
# ex. python3 main.py
if __name__ == "__main__":
    main()
