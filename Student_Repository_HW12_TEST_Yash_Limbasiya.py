import unittest
from Student_Repository_HW12_Yash_Limbasiya import UniversityLoader


"""
Unit test class.
"""


class Student_Repo_test (unittest.TestCase):

    """
    Tests if the student pretty table is correct.
    """

    def test_student_table(self):

        # Expected value
        expected = [
            ['10103', 'Jobs, S', 'SFEN', [{'CS 501': 'B'}, {'SSW 810': 'A-'}], ['SSW 540', 'SSW 555'], ['CS 546'], 3.5],
            ['10115', 'Bezos, J', 'SFEN', [{'CS 546': 'F'}, {'SSW 810': 'A'}], ['SSW 540', 'SSW 555'], ['CS 501'], 2.6666666666666665],
            ['10183', 'Musk, E', 'SFEN', [{'SSW 555': 'A'}, {'SSW 810': 'A'}], ['SSW 540'], ['CS 501', 'CS 546'], 4.0], 
            ['11714', 'Gates, B', 'CS', [{'CS 546': 'A'}, {'CS 570': 'A-'}, {'SSW 810': 'B-'}], [], ['SSW 565'], 3.3125]]
        university = UniversityLoader(
            path='files_HW11', name='Stevens',header = '0',db='StudentRepository.db')  # Creates the university loader.

        # Actual value as in the pretty table.
        actual = university.get_table_data_student()
        self.assertEqual(expected, actual)

    """
    Tests if the instructor pretty table is correct.
    """

    def test_instructor_table(self):

        # Expected value.
        expected =  [['98762', 'Hawking, S', 'CS', 'CS 501', 1], 
        ['98762', 'Hawking, S', 'CS', 'CS 546', 1],
        ['98762', 'Hawking, S', 'CS', 'CS 570', 1], 
        ['98763', 'Rowland, J', 'SFEN', 'SSW 810', 4], 
        ['98763', 'Rowland, J', 'SFEN', 'SSW 555', 1], 
        ['98764', 'Cohen, R', 'SFEN', 'CS 546', 1]]
        university = UniversityLoader(
            path='files_HW11', name='Stevens',header = '0',db='StudentRepository.db')
        # Actual value
        actual = university.get_table_data_instructors()
        self.assertEqual(expected, actual)


    def test_grades_summary(self):
        #Expected
        expected = [
            ('Bezos, J', '10115', 'A', 'SSW 810', 'Rowland, J'),
            ('Bezos, J', '10115', 'F', 'CS 546', 'Hawking, S'), 
            ('Gates, B', '11714', 'B-', 'SSW 810', 'Rowland, J'), 
            ('Gates, B', '11714', 'A', 'CS 546', 'Cohen, R'), 
            ('Gates, B', '11714', 'A-', 'CS 570', 'Hawking, S'),
            ('Jobs, S', '10103', 'A-', 'SSW 810', 'Rowland, J'), 
            ('Jobs, S', '10103', 'B', 'CS 501', 'Hawking, S'),
            ('Musk, E', '10183', 'A', 'SSW 555', 'Rowland, J'),
            ('Musk, E', '10183', 'A', 'SSW 810', 'Rowland, J')] 

        university = UniversityLoader(
            path='files_HW11', name='Stevens',header = '0',db='StudentRepository.db')

        actual = university.student_grades_table_db('StudentRepository.db')
        self.assertEqual(expected,actual)
        

    """
    Tests if the major pretty table is correct.
    """
    def test_major_table(self):
        # Expected value
        expected = [['SFEN', ['SSW 540', 'SSW 810', 'SSW 555'], ['CS 501', 'CS 546']],
         ['CS', ['CS 570', 'CS 546'], ['SSW 810', 'SSW 565']]]
        university = UniversityLoader(
            path='files_HW11', name='Stevens',header = '0',db='StudentRepository.db')
        # Actual value
        actual = university.get_table_data_majors()
        self.assertEqual(expected, actual)                    

    """
    Checks if the file not found is raised.
    """
    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            university = UniversityLoader(
                path='files_HW1', name='Stevens',header = '0',db='StudentRepository.db')

    """
    Checks if the instructor or student is not present.
    """
    def test_instructor_or_student_not_found(self):
        with self.assertRaises(KeyError):
            university = UniversityLoader(
                path='files_data_not_found', name='Stevens',header = '0',db='StudentRepository.db')

    """
    Checks if all the files are correct.
    """
    def test_wrong_no_of_fields(self):
        with self.assertRaises(ValueError):
            university = UniversityLoader(
                path='files_wrong_no_fileds', name='Stevens',header = '0',db='StudentRepository.db')

    """
    Checks if any duplicate values are present in the files.
    """
    def test_duplicate_student_instructors(self):
        with self.assertRaises(KeyError):
            university = UniversityLoader(
                path='files_duplicate', name='Stevens',header = '0',db='StudentRepository.db')


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
