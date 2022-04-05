from math import floor

class Student:
    def __init__(self,id,name,date):
        self.__id = id
        self.__name = name
        self.__DoB = date
    def set_id(self,id):
        self.__id = id
    def get_id(self):
        return self.__id
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_DoB(self,date):
        self.__DoB = date
    def get_DoB(self):
        return self.__DoB
    def show_info(self):
        print(f'{self.get_id()}\t{self.get_name()}\t{self.get_DoB()}')
        
class Course:
    def __init__(self,id,name):
        self.__id = id
        self.__name = name
    def set_id(self,id):
        self.__id = id
    def get_id(self):
        return self.__id
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
    def show_info(self):
        print(f'{self.get_id()}\t{self.get_name()}')

class Mark:
    def __init__(self,stuid,crsid,mark):
        self.__studentID = stuid
        self.__courseID = crsid
        self.__mark = mark
    def set_stuid(self,stuid):
        self.__studentID = stuid
    def get_stuid(self):
        return self.__studentID
    def set_crsid(self,crsid):
        self.__courseID = crsid
    def get_crsid(self):
        return self.__courseID
    def set_mark(self,mark):
        self.__mark = mark
    def get_mark(self):
        return self.__mark

stu_list = []
crs_list = []
mark_list = []

run = True
while(run):
    print(f'''
        0. Quit program
        1. Add student
        2. Add course
        3. Update mark
        4. Show student list
        5. Show course list
        6. Show mark list
    ''')
    select = int(input('Choose the action: '))
    if(select == 0): run = False
    if(select == 1):
        n = int(input('Enter number of students you want to add: '))
        print('Enter student info:')
        for i in range(n):
            id = input('ID: ')
            name = input('Name: ')
            DoB = input('Birthday: ')
            stu = Student(id,name,DoB)
            stu_list.append(stu)
    if(select == 2):
        n = int(input('Enter number of courses you want to add: '))
        print('Enter course info:')
        for i in range(n):
            id = input('ID: ')
            name = input('Name: ')
            crs = Course(id,name)
            crs_list.append(crs)
    if(select == 3):
        courseid = input('Enter the course ID you want to add mark: ')
        for c in range(len(crs_list)):
            if crs_list[c].get_id() == courseid:
                id = c
                print('Enter mark for each student:')
                for s in range(len(stu_list)):
                    mark = floor(float(input(f'Student {stu_list[s].get_id()}: ')))
                    o = Mark(stu_list[s].get_id(),crs_list[id].get_id(),mark)
                    mark_list.append(o)
    if(select == 4):
        print('Here is the student list: ')
        print('ID\tName\tDoB')
        for stu in stu_list:
            stu.show_info()
    if(select == 5):
        print('Here is the course list: ')
        print('ID\tName')
        for crs in crs_list:
            crs.show_info()
    if(select == 6):
        courseid = input('Enter the course ID you want to show mark: ')
        print('StudentID\tCourseID\tMark')
        for i in mark_list:
            if i.get_crsid() == courseid:
                print(f'{i.get_stuid()}\t{i.get_crsid()}\t{i.get_mark()}')