class Student:
    def __init__(self,student_id=0,student_major="",student_name=""):
        self.__student_id = 0
        self.__student_major = student_major
        self.__student_name = student_name

    @property
    def student_id(self):
        return self.__student_id

    @student_id.setter
    def student_id(self,id):
        self.student_id = id

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

