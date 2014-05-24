# time.py
#
# class to manipulate times


class Time(object):
    """represents a time of day in hours, minutes, and seconds"""

    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        """initialize a new time object"""
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def init(time, hours, minutes, seconds):
        time.hours = hours
        time.minutes = minutes
        time.seconds = seconds

    def __str__ (self):
        return ("<time: "
                + str(self.hours) + ":" 
                + str(self.minutes) + ":"
                + str(self.seconds) + ">")


def init_time(time, hour, minutes, seconds):
    time.hours = hours
    time.minutes = minutes
    time.seconds = seconds
