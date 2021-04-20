from .Grades import Grades
from .Student import Student
from .Instructors import Instructors
from collections import OrderedDict

class University:
    def __init__(self, university_name: str = "", grade_list=None, instructor_dict=None, student_dict=None):
        self.__university_name = university_name
        self.__grade_list = grade_list
        self.__instructor_dict = instructor_dict
        self.__student_dict = student_dict
        self.__student_course_dict = {}
        self.__instructor_course_dict = {}

    @property
    def university_name(self):
        return self.__university_name

    @university_name.setter
    def university_name(self, name):
        self.__university_name = name

    @property
    def grade_list(self):
        return self.__grade_list

    @grade_list.setter
    def grade_list(self, glist):
        self.__grade_list = glist

    @property
    def instructor_dict(self):
        return self.__instructor_dict

    @instructor_dict.setter
    def instructor_dict(self, ilist):
        self.__instructor_dict = ilist

    @property
    def student_dict(self):
        return self.__student_dict

    @student_dict.setter
    def student_dict(self, slist):
        self.__student_dict = slist

    @property
    def student_course_dict(self):
        return self.__student_course_dict

    @student_course_dict.setter
    def student_course_dict(self, dict_s):
        self.__student_course_dict = dict_s

    @property
    def instructor_course_dict(self):
        return self.__instructor_course_dict

    @instructor_course_dict.setter
    def instructor_course_dict(self, dict_i):
        self.__instructor_course_dict = dict_i

    """
    Maps the courses to students in the University.
    """
    def init_all_courses_to_student_id(self):
        student_course_dict = {}
        for grades in self.grade_list:
            id = grades.student_id
            if student_course_dict.get(id) is None:
                course_list = []
                course_grade = {}
                course_grade[grades.course] = grades.grade
                course_list.append(course_grade)
                # course_list = course_list.sort()
                student_course_dict[id] = course_list
            else:
                course_list = student_course_dict[id]
                course_grade = {}
                course_grade[grades.course] = grades.grade
                course_list.append(course_grade)
                # course_list = course_list.sort()
                student_course_dict[id] = course_list
        for id in student_course_dict:
            c_list = student_course_dict[id]
            c_list = sorted(c_list, key=lambda d: list(d.keys()))
            student_course_dict[id] = c_list
        student_course_dict=OrderedDict(sorted(student_course_dict.items()))                           
        self.student_course_dict = student_course_dict


    """
    Maps the courses to instructors in University.
    """
    def init_all_courses_to_instructor_id(self):
        intructor_course_dict = {}
        for grades in self.grade_list:
            id = grades.instructor_id
            if intructor_course_dict.get(id) is None:
                course_list = {}
                course_list[grades.course] = 1
                intructor_course_dict[id] = course_list
            else:
                course_list = intructor_course_dict[id]
                if course_list.get(grades.course) is None:
                    course_list[grades.course] = 1
                else:
                    student_count = course_list[grades.course]
                    student_count = student_count + 1
                    course_list[grades.course] = student_count
                intructor_course_dict[id] = course_list
        intructor_course_dict=OrderedDict(sorted(intructor_course_dict.items()))
        self.instructor_course_dict = intructor_course_dict
