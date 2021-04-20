class Instructors:
    def __init__(self,instructor_id=0,instructor_dept="",instructor_name=""):
        self.__instructor_id = instructor_id
        self.__instructor_dept = instructor_dept
        self.__instructor_name = instructor_name

    @property
    def instructor_id(self):
        return self.__instructor_id

    @instructor_id.setter
    def instructor_id(self,id):
        self.__instructor_id = id        

    @property
    def instructor_dept(self):
        return self.__instructor_dept

    @instructor_dept.setter
    def instructor_dept(self,dept):
        self.__instructor_dept = dept        

    @property
    def instructor_name(self):
        return self.__instructor_name

    @instructor_name.setter
    def instructor_name(self,name):
        self.__instructor_name = name                
