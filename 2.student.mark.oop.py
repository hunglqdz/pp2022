class Student:
    def __init__(self,id,name,date):
        self.__id = id
        self.__name = name
        self.__DoB = date
        self.__mark = None
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
    def set_mark(self,mark):
        self.__mark = mark
    def get_mark(self):
        return self.__mark
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

stu_list = []
crs_list = []
run = True
while(run):
    print(f'''
        0. quit program
        1. add student
        2. add course
        3. update mark
        4. show student list
        5. show course list
    ''')
    select = int(input('choose the action: '))
    if(select == 0): run = False
    if(select == 1):
        print('enter student info:')
        id = input('id: ')
        name = input('name: ')
        DoB = input('birthday: ')
        stu = Student(id,name,DoB)
        stu_list.append(stu)
    if(select == 2):
        print('enter course info:')
        id = input('id: ')
        name = input('name: ')
        crs = Course(id,name)
        crs_list.append(crs)
    if(select == 3):
        a = input('choose a course: ')
        print('enter mark for each student:')
        for i in range(len(stu_list)):
            print(f'student {stu_list[i].get_id()}:')
            mark = input('mark: ')
            stu_list[i].set_mark(mark)
        print('-----')
        print("students' mark in",a,'course:')
        print('id\tname\tmark')
        for i in stu_list:
            print(f'{i.get_id()}\t{i.get_name()}\t{i.get_mark()}')
    if(select == 4):
        print('here is student list: ')
        print('id\tname\tDoB')
        for i in stu_list:
            i.show_info()
    if(select == 5):
        print('here is course list: ')
        print('id\tname')
        for i in crs_list:
            i.show_info()
