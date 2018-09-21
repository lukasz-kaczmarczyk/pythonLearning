'''tasks source:
https://www.codesdope.com/practice/python-your-class/
'''

'''Create a Cricle class and intialize it with radius. Make two methods getArea and getCircumference inside this class.'''
print("--------------exercise1---------------------")

class Circle:
    def __init__(self, r):
        self.radius = r

    def getArea(self):
        return 3.14 * self.radius ** 2

    def getCircumference(self):
        return 2 * 3.14 * self.radius


myCircle = Circle(2)
res = myCircle.getArea()
print("area: {}, circumference {}".format(myCircle.getArea(), myCircle.getCircumference()))

'''
Create a Temprature class. Make two methods :
1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
'''
class Temperature:
    @staticmethod
    def convertFahrenheit(celsius):
        return celsius * 1.8 + 32

    @staticmethod
    def convertCelsius(fahrenheit):
        return (fahrenheit-32)/1.8

print("celsius to fahr: {}, fahr to celsius: {}".format(Temperature.convertFahrenheit(11), Temperature.convertCelsius(60)))

print("--------------exercise2---------------------")
'''
Create a Student class and initialize it with name and roll number. Make methods to :
1. Display - It should display all informations of the student.
2. setAge - It should assign age to student
3. setMarks - It should assign marks to the student.
'''

class Student:
    def __init__(self, n, r):
        self.name = n
        self.roll = r

    def display(self):
        print(self.__dict__)

    def setAge(self, a):
        self.age = a

    def setMarks(self, *args):
        self.marks = list(args)

    def addMark(self, m):
        self.marks.append(m)

student1 = Student("mark", 11)
student1.display()
student1.setAge(24)
student1.display()
student1.setMarks(3,4,5,3,5,3)
student1.display()
student1.addMark(3)
student1.display()

print("--------------exercise3---------------------")
'''
Create a Time class and initialize it with hours and minutes.
1. Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
2. Make a method displayTime which should print the time.
3. Make a method DisplayMinute which should display the total minutes in the Time. E.g.- (1 hr 2 min) should display 62 minute.
'''


class Time:
    def __init__(self, h, m):
        self.hours = h
        self.minutes = m
        self.days = 0

    def __add__(self, other):
        h = self.hours + other.hours
        m = self.minutes + other.minutes
        d = 0
        if m >= 60:
            h += 1
            m -= 60

        if h >= 24:
            d += h // 24
            h %= 24
        result = str(self.hours) + ' : ' + str(self.minutes) + ' + ' + str(other.hours) + ' : '+ str(other.minutes) + ' = ' \
                 + str(d) + ' days ' + str(h)+' hours '+str(m) + 'minutes'
        return result


time1 = Time(2, 15)
time2 = Time(1,15)

print(time1+time2)
print(Time(24,15)+Time(24,35))
print(Time(23,27) + Time(5,42))
