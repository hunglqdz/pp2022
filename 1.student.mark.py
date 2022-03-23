student = {"id":None,"name":None,"DoB":None}
course = {"id":None,"name":None}
stu_list = []
crs_list = []

def add_stu():
    """this function adds students' information to the student list"""
    while(True):
        n = int(input("enter number of students: "))
        if(n>0): break
    for i in range(n):
        print("student "+str(i+1))
        student["id"] = input("enter id: ")
        student["name"] = input("enter name: ")
        student["DoB"] = input("enter date of birth: ")
        stu_list.append(student.copy())

def list_stu():
    """this function prints the student list"""
    print("here is student list:")
    print("STT\t id\t name\t DoB")
    for i in range(len(stu_list)):
        s = stu_list[i]
        print((i+1),"\t",s["id"],"\t",s["name"],"\t",s["DoB"])

def add_crs():
    """this function adds courses' information to the course list"""
    while(True):
        n = int(input("enter number of courses: "))
        if(n>0): break
    for i in range(n):
        print("course "+str(i+1))
        course["id"] = input("enter id: ")
        course["name"] = input("enter name: ")
        crs_list.append(course.copy())

def list_crs():
    """this function prints the course list"""
    print("here is course list:")
    print("STT\t id\t name")
    for i in range(len(crs_list)):
        c = crs_list[i]
        print((i+1),"\t",c["id"],"\t",c["name"])

def add_mark():
    """this function adds students' mark in a specific course"""
    a = input("choose a course: ")
    for i in range(len(stu_list)):
        print("student "+str(i+1))
        mark = input("enter mark: ")
        stu_list[i].update({"mark":mark})
    print("-----")
    print("students' mark in",a,"course:")
    print("STT\t id\t name\t mark")
    for i in range(len(stu_list)):
        s = stu_list[i]
        print((i+1),"\t",s["id"],"\t",s["name"],"\t",s["mark"])

add_stu()
print("-----")
add_crs()
print("-----")
list_stu()
print("-----")
list_crs()
print("-----")
add_mark()
