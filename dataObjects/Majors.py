class Majors:
    def __init__(self,major_name="",required="",course_name=""):
        self.__major_name = major_name
        self.__required = required
        self.__course_name = course_name

    @property
    def major_name(self):
        return self.__major_name

    @major_name.setter
    def major_name(self,name):
        self.__major_name = name

    @property
    def required(self):
        return self.__required

    @required.setter
    def student_major(self,required):
        self.__required = required

    @property
    def course_name(self):
        return self.__course_name

    @course_name.setter
    def course_name(self,name):
        self.__course_name = name        

