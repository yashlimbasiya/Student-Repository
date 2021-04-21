from .Grades import Grades
from .Student import Student
from .Instructors import Instructors
from collections import OrderedDict


class University:
    def __init__(self, university_name: str = "", grade_list=None, instructor_dict=None, student_dict=None, major_dict=None):
        self.__university_name = university_name
        self.__grade_list = grade_list
        self.__instructor_dict = instructor_dict
        self.__major_dict = major_dict
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
    def major_dict(self):
        return self.__major_dict

    @major_dict.setter
    def major_dict(self, ilist):
        self.__major_dict = ilist

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
                course_grade = {}
                course_list = []
                course_grade[grades.course] = grades.grade
                gpa_curr = grades.convert_gpa(grades.grade)
                # print(gpa_curr)
                # major_dict = self.major_dict[grades.major]
                # if major_dict.get(grades.course) is not None:
                if grades.course in self.student_dict[id].remaining_course:
                    self.student_dict[id].remaining_course.remove(
                        grades.course)
                elif grades.course in self.student_dict[id].elective_course:
                    self.student_dict[id].elective_course.remove(grades.course)
                course_list.append(course_grade)
                # self.student_dict[id].gpa = gpa_curr
                # course_list = course_list.sort()
                self.student_dict[id].gpa = gpa_curr
                student_course_dict[id] = course_list
            else:
                course_list = student_course_dict[id]
                course_grade = {}
                course_grade[grades.course] = grades.grade
                gpa_curr = grades.convert_gpa(grades.grade)
                if grades.course in self.student_dict[id].remaining_course:
                    self.student_dict[id].remaining_course.remove(
                        grades.course)
                elif grades.course in self.student_dict[id].elective_course:
                    self.student_dict[id].elective_course.remove(grades.course)
                course_list.append(course_grade)
                course_len = len(course_list)
                gpa_curr = gpa_curr + (self.student_dict[id].gpa * course_len)
                course_len = course_len + 1
                gpa_curr = gpa_curr/course_len
                self.student_dict[id].gpa = gpa_curr
                # course_list = course_list.sort()
                student_course_dict[id] = course_list
        for id in student_course_dict:
            c_list = student_course_dict[id]
            c_list = sorted(c_list, key=lambda d: list(d.keys()))
            student_course_dict[id] = c_list
        student_course_dict = OrderedDict(sorted(student_course_dict.items()))
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
        intructor_course_dict = OrderedDict(
            sorted(intructor_course_dict.items()))
        self.instructor_course_dict = intructor_course_dict

    def init_student(self):
        for student_id in self.student_dict:
            student_obj = self.student_dict[student_id]
            major = student_obj.student_major
            major_dict = self.major_dict[major]
            for course_name in major_dict:
                if major_dict[course_name] == 'R':
                    student_obj.remaining_course.append(course_name)
                else:
                    student_obj.elective_course.append(course_name)
            self.student_dict[student_id] = student_obj
    
    def init_all_majors(self):
        major = {}
        for majors in self.major_dict:
            req = []
            ele = []
            major[majors] = {}
            for course in self.major_dict[majors]:
                if self.major_dict[majors][course] == 'R':
                    req.append(course)
                else:
                    ele.append(course)
            major[majors]['R'] = req
            major[majors]['E'] = ele
        
        return major
