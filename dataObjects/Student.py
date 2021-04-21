class Student:
    def __init__(self,student_id=0,student_major="",student_name="", gpa=0):
        self.__student_id = 0
        self.__student_major = student_major
        self.__student_name = student_name
        self.__gpa = gpa
        self.__completed_course = {}
        self.__remaining_course = []
        self.__elective_course = []

    @property
    def gpa(self):
        return self.__student_id

    @gpa.setter
    def gpa(self,gpa):
        self.__gpa = gpa

    @property
    def completed_course(self):
        return self.__completed_course

    @completed_course.setter
    def gpa(self,completed_course):
        self.__completed_course = completed_course

    @property
    def remaining_course(self):
        return self.__remaining_course

    @remaining_course.setter
    def gpa(self,remaining_course):
        self.__remaining_course = remaining_course        

    @property
    def student_id(self):
        return self.__student_id

    @property
    def elective_course(self):
        return self.__elective_course

    @elective_course.setter
    def gpa(self,elective_course):
        self.__elective_course = elective_course        

    @student_id.setter
    def student_id(self,id):
        self.__student_id = id        

    @property
    def student_major(self):
        return self.__student_major

    @student_major.setter
    def student_major(self,major):
        self.__student_major = major

    @property
    def student_name(self):
        return self.__student_name

    @student_name.setter
    def student_name(self,name):
        self.__student_name = name        

