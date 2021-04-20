from dataObjects import *
import glob
from prettytable import PrettyTable
import sys
import getopt

"""
The initail loader class.

"""
class UniversityLoader:
    def __init__(self, path: str, name: str):
        self.__path = path
        self.__university = University(name)
        self.create_uni()

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path):
        self.__path = path

    @property
    def university(self):
        return self.__university

    @university.setter
    def university(self, uni):
        self.__university = uni


    """
    Reads the file path and sends the fields back.

    """
    def read_file_custom(self, path: str, fields_num: int, sep: str = '\t'):
        try:
            with open(path, 'r') as file_open:
                count = 0
                while True:
                    line = file_open.readline()
                    count = count + 1
                    if line != '':
                        line_divided = line.strip('\n').split('\t')
                        if len(line_divided) == fields_num:  #Checks if all the fields are present.
                            yield line_divided #Returns a single line at a time.
                        else:
                            file_open.close() 
                            raise ValueError(
                                f'The file at path {path} has invalid number of fileds at line number {count}')

                    else: #Checks if is the last line or empty line is present.
                        line = file_open.readline()
                        file_open.close()
                        if line != '':
                            raise ValueError(
                                f'The file at path {path} has empty line at line number {count}')
                        else:
                            break
        except FileNotFoundError:
            raise FileNotFoundError(f"No file found with the path {path}")


    """
    Initialializes the university.
    """
    def create_uni(self):
        folder_path = self.path #Sets the path
        university_obj = self.university  #Sets the university
        student_files = glob.glob(folder_path+"/students.txt")  #Gets all the files with name student.txt
        instructor_files = glob.glob(folder_path+"/instructors.txt") #Gets all the files with name student.txt
        grade_files = glob.glob(folder_path+"/grades.txt") #Gets all the files with name student.txt
        
        #Raises the file not found exception.
        if(len(student_files) != 1):
            raise FileNotFoundError(
                "Number of student files is not equal to 1")
            exit()
        if(len(instructor_files) != 1):
            raise FileNotFoundError(
                "Number of instructor files is not equal to 1")
            exit()
        if(len(grade_files) != 1):
            raise FileNotFoundError("Number of grade files is not equal to 1")
            exit()

        #Reads the student files.
        if(len(student_files) == 1):
            student_dict = {}
            student_file_path: str = student_files.pop()
            for student_id, student_name, student_major in self.read_file_custom(student_file_path, 3):
                studentobj = Student(
                    student_id=student_id, student_major=student_major, student_name=student_name)
                if student_dict.get(student_id) is None:
                    student_dict[student_id] = studentobj
                else:
                    raise KeyError("Duplicate student values.")
            university_obj.student_dict = student_dict #Sets the student dict.

        #Reads the instructor files
        if(len(instructor_files) == 1):
            instructor_dict = {}
            for instructor_id, instructor_name, instructor_dept in self.read_file_custom(path=instructor_files.pop(), fields_num=3):
                instructorobj = Instructors(
                    instructor_id=instructor_id, instructor_dept=instructor_dept, instructor_name=instructor_name)
                if instructor_dict.get(instructor_id) is  None:
                    instructor_dict[instructor_id] = instructorobj
                else:
                    raise KeyError("Duplicate intructor values.")
            university_obj.instructor_dict = instructor_dict #sets the instructor dict.

        #Reads the grade files.
        if len(grade_files) == 1:
            grade_list = []
            for student_id, course_name, grade_val, instructor_id in self.read_file_custom(path=grade_files.pop(), fields_num=4):
                if university_obj.student_dict.get(student_id) is not None and university_obj.instructor_dict.get(instructor_id) is not None:
                    gradeobj = Grades(student_id=student_id, course=course_name,
                                      grade=grade_val, instructor_id=instructor_id)
                    grade_list.append(gradeobj)
                elif university_obj.student_dict.get(student_id) is None: #Checks if the student id is present
                    raise KeyError(
                        f"Student with id {student_id} not currently present.")
                elif university_obj.instructor_dict.get(instructor_id) is None: #Checks if the instructor id is present.
                    raise KeyError(
                        f"Instructor with id {instructor_id} not currently present.")

            university_obj.grade_list = grade_list

        self.university = university_obj


    """
    Gets the data for student pretty table.
    """
    def get_table_data_student(self):
        university_obj = self.university
        university_obj.init_all_courses_to_student_id()
        listfortable = []
        for studentids in university_obj.student_course_dict:
            studentlist = []
            coursesandgrades = university_obj.student_course_dict.get(
                studentids)
            studentdetail = university_obj.student_dict.get(studentids)
            studentlist.append(studentids)
            studentlist.append(studentdetail.student_name)
            studentlist.append(studentdetail.student_major)
            studentlist.append(coursesandgrades)
            listfortable.append(studentlist)
        return listfortable


    """
    Gets the data for instructor pretty table.
    """
    def get_table_data_instructors(self):
        university_obj = self.university
        university_obj.init_all_courses_to_instructor_id()
        intlistfortable = []
        for instructorids in university_obj.instructor_course_dict:
            coursesandgrades = university_obj.instructor_course_dict.get(
                instructorids)
            instructordetail = university_obj.instructor_dict.get(
                instructorids)
            for course_name in coursesandgrades:
                instructorlist = []
                instructorlist.append(instructorids)
                instructorlist.append(instructordetail.instructor_name)
                instructorlist.append(instructordetail.instructor_dept)
                instructorlist.append(course_name)
                instructorlist.append(coursesandgrades.get(course_name))
                intlistfortable.append(instructorlist)                
        return intlistfortable


    """
    Creates the pretty table.
    """
    def create_table(self):
        student_table = PrettyTable()
        student_table.field_names = [
            "CWID", "NAME", "Major", "COMPLETED COURSES"]
        student_table.add_rows(self.get_table_data_student())
        print(student_table)
        instructor_table = PrettyTable()
        instructor_table.field_names = ["CWID", "NAME",
                                        "Dept", "Courses", "Number of students"]
        instructor_table.add_rows(self.get_table_data_instructors())
        print(instructor_table)


"""
Main function.
"""
def main(arglist):
    if len(arglist) != 2:
        print("The syntax for running the file: \npython hw09.py <file_path> <univ_name>\n")
    else:
        file_path = arglist[0]
        uni_name = arglist[1]
        univ = UniversityLoader(
            path=file_path, name=uni_name)
        univ.create_table()


if __name__ == '__main__':
    main(sys.argv[1:])
