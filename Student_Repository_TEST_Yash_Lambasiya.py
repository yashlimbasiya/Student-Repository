import unittest
from Student_Repository_Yash_Limbasiya import UniversityLoader


"""
Unit test class.
"""


class Student_Repo_test (unittest.TestCase):

    """
    Tests if the student pretty table is correct.
    """

    def test_student_table(self):

        # Expected value
        expected =  [['10103', 'Baldwin, C', 'SFEN', [{'CS 501': 'B'}, {'SSW 564': 'A-'}, {'SSW 567': 'A'}, {'SSW 687': 'B'}], ['SSW 540', 'SSW 555'], ['CS 513', 'CS 545']],
         ['10115', 'Wyatt, X', 'SFEN', [{'CS 545': 'A'}, {'SSW 564': 'B+'}, {
             'SSW 567': 'A'}, {'SSW 687': 'A'}], ['SSW 540', 'SSW 555'], ['CS 501', 'CS 513']],
         ['10172', 'Forbes, I', 'SFEN', [{'SSW 555': 'A'}, {
             'SSW 567': 'A-'}], ['SSW 540', 'SSW 564'], ['CS 501', 'CS 513', 'CS 545']],
         ['10175', 'Erickson, D', 'SFEN', [{'SSW 564': 'A'}, {'SSW 567': 'A'}, {
             'SSW 687': 'B-'}], ['SSW 540', 'SSW 555'], ['CS 501', 'CS 513', 'CS 545']],
         ['10183', 'Chapman, O', 'SFEN', [{'SSW 689': 'A'}], [
             'SSW 540', 'SSW 564', 'SSW 555', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545']],
         ['11399', 'Cordova, I', 'SYEN', [{'SSW 540': 'B'}], [
             'SYS 671', 'SYS 612', 'SYS 800'], ['SSW 810', 'SSW 565']],
         ['11461', 'Wright, U', 'SYEN', [{'SYS 611': 'A'}, {'SYS 750': 'A-'}, {
             'SYS 800': 'A'}], ['SYS 671', 'SYS 612'], ['SSW 810', 'SSW 565', 'SSW 540']],
         ['11658', 'Kelly, P', 'SYEN', [{'SSW 540': 'F'}], [
             'SYS 671', 'SYS 612', 'SYS 800'], ['SSW 810', 'SSW 565']],
         ['11714', 'Morton, A', 'SYEN', [{'SYS 611': 'A'}, {'SYS 645': 'C'}], [
             'SYS 671', 'SYS 612', 'SYS 800'], ['SSW 810', 'SSW 565', 'SSW 540']],
         ['11788', 'Fuller, E', 'SYEN', [{'SSW 540': 'A'}], ['SYS 671', 'SYS 612', 'SYS 800'], ['SSW 810', 'SSW 565']]]
        university = UniversityLoader(
            path='files_HW10', name='Stevens',header='0')  # Creates the university loader.

        # Actual value as in the pretty table.
        actual = university.get_table_data_student()
        self.assertEqual(expected, actual)

    """
    Tests if the instructor pretty table is correct.
    """

    def test_instructor_table(self):

        # Expected value.
        expected = [['98760', 'Darwin, C', 'SYEN', 'SYS 800', 1],
                    ['98760', 'Darwin, C', 'SYEN', 'SYS 750', 1],
                    ['98760', 'Darwin, C', 'SYEN', 'SYS 611', 2],
                    ['98760', 'Darwin, C', 'SYEN', 'SYS 645', 1],
                    ['98763', 'Newton, I', 'SFEN', 'SSW 555', 1],
                    ['98763', 'Newton, I', 'SFEN', 'SSW 689', 1],
                    ['98764', 'Feynman, R', 'SFEN', 'SSW 564', 3],
                    ['98764', 'Feynman, R', 'SFEN', 'SSW 687', 3],
                    ['98764', 'Feynman, R', 'SFEN', 'CS 501', 1],
                    ['98764', 'Feynman, R', 'SFEN', 'CS 545', 1],
                    ['98765', 'Einstein, A', 'SFEN', 'SSW 567', 4],
                    ['98765', 'Einstein, A', 'SFEN', 'SSW 540', 3]]
        university = UniversityLoader(
            path='files_HW10', name='Stevens',header='0')
        # Actual value
        actual = university.get_table_data_instructors()
        self.assertEqual(expected, actual)


    """
    Tests if the major pretty table is correct.
    """
    def test_major_table(self):
        # Expected value
        expected = [['SFEN', ['SSW 540', 'SSW 564', 'SSW 555', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545']],
                    ['SYEN', ['SYS 671', 'SYS 612', 'SYS 800'], ['SSW 810', 'SSW 565', 'SSW 540']]]
        university = UniversityLoader(
            path='files_HW10', name='Stevens',header = '0')
        # Actual value
        actual = university.get_table_data_majors()
        self.assertEqual(expected, actual)                    

    """
    Checks if the file not found is raised.
    """
    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            UniversityLoader(
                path='files_HW101', name='Stevens',header='0')

    """
    Checks if the instructor or student is not present.
    """
    def test_instructor_or_student_not_found(self):
        with self.assertRaises(KeyError):
            UniversityLoader(
                path='files_data_not_found', name='Stevens',header='0')

    """
    Checks if all the files are correct.
    """
    def test_wrong_no_of_fields(self):
        with self.assertRaises(ValueError):
            UniversityLoader(
                path='files_wrong_no_fileds', name='Stevens',header='0')

    """
    Checks if any duplicate values are present in the files.
    """
    def test_duplicate_student_instructors(self):
        with self.assertRaises(KeyError):
            UniversityLoader(
                path='files_duplicate', name='Stevens', header='0')


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
