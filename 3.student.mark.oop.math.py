from math import floor

class Student:
    def __init__(self, id, name, date):
        self.__id = id
        self.__name = name
        self.__dob = date

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_dob(self, date):
        self.__dob = date

    def get_DoB(self):
        return self.__dob

    def show_info(self):
        print(f'{self.get_id()}\t{self.get_name()}\t{self.get_DoB()}')
        
class Course:
    def __init__(self, id, name, cre):
        self.__id = id
        self.__name = name
        self.__credit = cre

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_credit(self, cre):
        self.__credit = cre

    def get_credit(self):
        return self.__credit

    def show_info(self):
        print(f'{self.get_id()}\t{self.get_name()}\t{self.get_credit()}')

class Mark:
    def __init__(self, stuid, crsid, mark):
        self.__studentID = stuid
        self.__courseID = crsid
        self.__mark = mark

    def set_stuid(self, stuid):
        self.__studentID = stuid

    def get_stuid(self):
        return self.__studentID

    def set_crsid(self, crsid):
        self.__courseID = crsid

    def get_crsid(self):
        return self.__courseID

    def set_mark(self, mark):
        self.__mark = mark

    def get_mark(self):
        return self.__mark

class Gpa:
    def __init__(self, stuid, gpa):
        self.__studentID = stuid
        self.__gpa = gpa

    def set_stuid(self, stuid):
        self.__studentID = stuid

    def get_stuid(self):
        return self.__studentID

    def set_gpa(self, gpa):
        self.__gpa = gpa

    def get_gpa(self):
        return self.__gpa

    def show_info(self):
        print(f'{self.get_stuid()}\t{self.get_gpa()}')

stu_list = []
crs_list = []
mark_list = []
gpa_list = []

run = True
while(run):
    print(f'''
        0. Quit program
        1. Add students
        2. Add courses
        3. Update marks (for 1 course)
        4. Show student list
        5. Show course list
        6. Show mark list (for 1 course)
        7. Calculate GPA (for 1 student)
        8. Show GPA list
    ''')
    select = int(input('Choose the action: '))
    if(select == 0): run = False
    if(select == 1):
        n = int(input('Enter number of students you want to add: '))
        print('Enter student info:')
        for i in range(n):
            id = input('ID: ')
            name = input('Name: ')
            dob = input('Birthday: ')
            stu = Student(id, name, dob)
            stu_list.append(stu)
    if(select == 2):
        n = int(input('Enter number of courses you want to add: '))
        print('Enter course info:')
        for i in range(n):
            id = input('ID: ')
            name = input('Name: ')
            cre = int(input('Credits: '))
            crs = Course(id, name, cre)
            crs_list.append(crs)
    if(select == 3):
        courseid = input('Enter the course ID you want to add mark: ')
        for c in range(len(crs_list)):
            if crs_list[c].get_id() == courseid:
                id = c
                print('Enter mark for each student:')
                for i in range(len(stu_list)):
                    mark = floor(float(input(f'Student {stu_list[i].get_id()}: ')))
                    o = Mark(stu_list[i].get_id(), crs_list[id].get_id(), mark)
                    mark_list.append(o)
    if(select == 4):
        print('Here is the student list: ')
        print('ID\t\tName\tDoB')
        for stu in stu_list:
            stu.show_info()
    if(select == 5):
        print('Here is the course list: ')
        print('ID\tName\tCredit')
        for crs in crs_list:
            crs.show_info()
    if(select == 6):
        courseid = input('Enter the course ID you want to show mark: ')
        print('StuID\t\tCrsID\tMark')
        for i in mark_list:
            if i.get_crsid() == courseid:
                print(f'{i.get_stuid()}\t{i.get_crsid()}\t{i.get_mark()}')
    if(select == 7):
        studentid = input('Choose the student ID you want to calculate GPA: ')
        point = total = 0
        for m in range(len(mark_list)):
            if mark_list[m].get_stuid() == studentid:
                for c in range(len(crs_list)):
                    if mark_list[m].get_crsid() == crs_list[c].get_id():
                        point += mark_list[m].get_mark() * crs_list[c].get_credit()
                        total += crs_list[c].get_credit()
        gpa = point / total
        print('His/Her GPA is:', gpa)
        o = Gpa(studentid, gpa)
        gpa_list.append(o)
    if(select == 8):
        gpa_list.sort(reverse=True)
        print('Here is student list sorted by GPA:')
        print('StuID\tGPA')
        for o in gpa_list:
            o.show_info()