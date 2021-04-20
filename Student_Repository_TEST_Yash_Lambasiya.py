import unittest
from hw09 import UniversityLoader


"""
Unit test class.
"""


class hw09test (unittest.TestCase):

    """
    Tests if the student pretty table is correct.
    """

    def test_student_table(self):

        # Expected value
        expected = [['10103', 'Baldwin, C', 'SFEN', [{'CS 501': 'B'}, {'SSW 564': 'A-'}, {'SSW 567': 'A'}, {'SSW 687': 'B'}]],
                    ['10115', 'Wyatt, X', 'SFEN', [{'CS 545': 'A'}, {'SSW 564': 'B+'}, {'SSW 567': 'A'}, {'SSW 687': 'A'}]], ['10172', 'Forbes, I', 'SFEN', [{'SSW 555': 'A'}, {'SSW 567': 'A-'}]], ['10175', 'Erickson, D', 'SFEN', [{'SSW 564': 'A'}, {'SSW 567': 'A'}, {'SSW 687': 'B-'}]], [
            '10183', 'Chapman, O', 'SFEN', [{'SSW 689': 'A'}]], ['11399', 'Cordova, I', 'SYEN', [{'SSW 540': 'B'}]], ['11461', 'Wright, U', 'SYEN', [{'SYS 611': 'A'}, {'SYS 750': 'A-'}, {'SYS 800': 'A'}]], ['11658', 'Kelly, P', 'SYEN', [{'SSW 540': 'F'}]], ['11714', 'Morton, A', 'SYEN', [{'SYS 611': 'A'}, {'SYS 645': 'C'}]], ['11788', 'Fuller, E', 'SYEN', [{'SSW 540': 'A'}]]]
        university = UniversityLoader(
            path='files', name='Stevens')  # Creates the university loader.

        # Actual value as in the pretty table.
        actual = university.get_table_data_student()
        self.assertEqual(expected, actual)

    """
    Tests if the instructor pretty table is correct.
    """

    def test_instructor_table(self):

        # Expected value.
        expected = [['98760', 'Darwin, C', 'SYEN', 'SYS 800', 1], ['98760', 'Darwin, C', 'SYEN', 'SYS 750', 1], ['98760', 'Darwin, C', 'SYEN', 'SYS 611', 2], ['98760', 'Darwin, C', 'SYEN', 'SYS 645', 1], ['98763', 'Newton, I', 'SFEN', 'SSW 555', 1], ['98763', 'Newton, I', 'SFEN', 'SSW 689', 1], [
            '98764', 'Feynman, R', 'SFEN', 'SSW 564', 3], ['98764', 'Feynman, R', 'SFEN', 'SSW 687', 3], ['98764', 'Feynman, R', 'SFEN', 'CS 501', 1], ['98764', 'Feynman, R', 'SFEN', 'CS 545', 1], ['98765', 'Einstein, A', 'SFEN', 'SSW 567', 4], ['98765', 'Einstein, A', 'SFEN', 'SSW 540', 3]]
        university = UniversityLoader(
            path='files', name='Stevens')
        # Actual value
        actual = university.get_table_data_instructors()
        self.assertEqual(expected, actual)

    """
    Checks if the file not found is raised.
    """

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            UniversityLoader(
                path='file', name='Stevens')

    """
    Checks if the instructor or student is not present.
    """

    def test_instructor_or_student_not_found(self):
        with self.assertRaises(KeyError):
            UniversityLoader(
                path='files_data_not_found', name='Stevens')

    """
    Checks if all the files are correct.
    """

    def test_wrong_no_of_fields(self):
        with self.assertRaises(ValueError):
            UniversityLoader(
                path='files_wrong_no_fileds', name='Stevens')

    """
    Checks if any duplicate values are present in the files.
    """

    def test_duplicate_student_instructors(self):
        with self.assertRaises(KeyError):
            UniversityLoader(
                path='files_duplicate', name='Stevens')


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
