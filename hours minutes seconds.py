def digits(val):
    s = str(val)
    if len(s) == 1:
        s = "0" + s
    return s

class clock:
    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __str__(self):
        return digits(self.__hour) + ":" + \
               digits(self.__minute) + ":" + \
               digits(self.__second)

    def next_second(self):
        self.__second += 1
        if self.__second > 59:
            self.__second = 0
            self.__minute += 1
            if self.__minute >  59:
                self.__minute = 0
                self.__hour += 1
                if self.__hour > 23:
                    self.__hour = 0

    def previous_second(self):
        self.__second -= 1
        if self.__second < 0:
            self.__second = 59
            self.__minute -=1
            if self.__minute < 0:
                self.__minute = 59
                self.__hour -= 1
                if self.__hour < 0:
                    self.__hour = 23

Timer = clock(23, 59, 59)
print(Timer)
Timer.next_second()
print(Timer)
Timer.previous_second()
print(Timer)

            
                
