from dataObjects import *
import glob
from prettytable import PrettyTable
import sys
import getopt

"""
The initail loader class.

"""
class UniversityLoader:
    def __init__(self, path: str, name: str, header: int = 0):
        self.__path = path
        self.__university = University(name)
        self.__header = header
        self.create_uni()

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path):
        self.__path = path

    @property
    def header(self):
        return self.__header

    @header.setter
    def header(self, header):
        self.__header = header        

    @property
    def university(self):
        return self.__university

    @university.setter
    def university(self, uni):
        self.__university = uni


    """
    Reads the file path and sends the fields back.

    """
    def read_file_custom(self, path: str, fields_num: int, sep: str = '\t',header='1'):
        try:
            with open(path, 'r') as file_open:
                count = 0
                line=''
                if header == '0':
                    line = file_open.readline()            
                while True:
                    line = file_open.readline()
                    count = count + 1
                    if line != '':
                        line_divided = line.strip('\n').split(sep)
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
        major_files = glob.glob(folder_path+"/majors.txt") #Gets all the files with name majors.txt
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
        if(len(major_files) != 1):
            raise FileNotFoundError("Number of major files is not equal to 1")
            exit()        


        #Reads the major files.
        if(len(major_files) == 1):
            major_dict = {}
            # student_file_path: str = student_files.pop()
            for major, req, course in self.read_file_custom(path=major_files.pop(), fields_num=3,header=self.header):
                majorobj = Majors(
                    major_name=major, required=req, course_name=course)
                if major_dict.get(major) is None:
                    course_dict ={}
                    course_dict[course] = req
                    major_dict[major] = course_dict
                else:
                    course_dict = major_dict[major]
                    if course_dict.get(course) is not None:
                        raise KeyError("Duplicate major values.")
                    else:
                        course_dict[course] = req
                        major_dict[major] = course_dict
            university_obj.major_dict = major_dict #Sets the major dict.            

        #Reads the student files.
        if(len(student_files) == 1):
            student_dict = {}
            # student_file_path: str = student_files.pop()
            for student_id, student_name, student_major in self.read_file_custom(path=student_files.pop(), fields_num=3,sep=';',header=self.header):
                studentobj = Student(
                    student_id=student_id, student_major=student_major, student_name=student_name)
                if student_dict.get(student_id) is None:
                    student_dict[student_id] = studentobj
                else:
                    raise KeyError("Duplicate student values.")
            university_obj.student_dict = student_dict #Sets the student dict.
            university_obj.init_student()


        #Reads the instructor files
        if(len(instructor_files) == 1):
            instructor_dict = {}
            for instructor_id, instructor_name, instructor_dept in self.read_file_custom(path=instructor_files.pop(), fields_num=3,sep='|',header=self.header):
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
            for student_id, course_name, grade_val, instructor_id in self.read_file_custom(path=grade_files.pop(), fields_num=4,sep='|',header=self.header):
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
            studentlist.append(studentdetail.remaining_course)
            studentlist.append(studentdetail.elective_course)
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
    Gets the data for majors pretty table.
    """
    def get_table_data_majors(self):
        university_obj = self.university
        majors_dict = university_obj.init_all_majors()
        major_list_table = []
        for major in majors_dict:
            major_list = []
            major_list.append(major)
            major_list.append(majors_dict[major]['R'])
            major_list.append(majors_dict[major]['E'])
            major_list_table.append(major_list)
        return major_list_table
        
    """
    Creates the pretty table.
    """
    def create_table(self):
        student_table = PrettyTable()
        student_table.field_names = [
            "CWID", "NAME", "Major", "COMPLETED COURSES", "REQUIRED COURSES LEFT","ELECTIVE COURSES AVAILABLE"]
        student_table.add_rows(self.get_table_data_student())
        print(student_table)
        instructor_table = PrettyTable()
        instructor_table.field_names = ["CWID", "NAME",
                                        "Dept", "Courses", "Number of students"]
        instructor_table.add_rows(self.get_table_data_instructors())
        print(instructor_table)
        majors_table = PrettyTable()
        majors_table.field_names = ["Major", "Required course", "Electives"]
        majors_table.add_rows(self.get_table_data_majors())
        print(majors_table)


"""
Main function.
"""
def main(arglist):
    if len(arglist) != 3:
        print("The syntax for running the file: \npython hw09.py <file_path> <univ_name> <header_flag> (0 - for header / 1 - for no header \n")
    else:
        file_path = arglist[0]
        uni_name = arglist[1]
        header = arglist[2]
        
        univ = UniversityLoader(
            path=file_path, name=uni_name, header = header)
        univ.create_table()


if __name__ == '__main__':
    main(sys.argv[1:])
