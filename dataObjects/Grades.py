import sys
class Grades:
    def __init__(self,student_id:str="",course:str="",grade:str="",instructor_id:str=""):
        self.__student_id = student_id
        self.__course = course
        self.__grade = grade
        self.__instructor_id = instructor_id

    @property
    def instructor_id(self):
        return self.__instructor_id

    @instructor_id.setter
    def instructor_id(self,id:str):
        self.__instructor_id = id        

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def instructor_dept(self,id:str):
        self.__student_id = id        

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self,course:str):
        self.__course = course    

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self,grade:str):
        self.__grade = grade
        

