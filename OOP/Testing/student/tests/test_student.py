import unittest

from project.student import Student


class TestStudent(unittest.TestCase):
    name = "Pesho"
    courses = {"Math": [4, 5, 6], "IT": [5.5, 6]}

    def setUp(self):
        self.student = Student(self.name, self.courses)

    def test_student_init__when_initialized__expect_correct_attributes(self):
        self.assertEqual(self.name, self.student.name)
        self.assertEqual(self.courses, self.student.courses)

    def test_student_init__when_no_courses__expect_empty_dict(self):
        self.student_1 = Student(self.name)
        self.assertEqual(0, len(self.student_1.courses))

    def test_student_enroll__when_course_exist__expected_notes_update(self):
        result = self.student.enroll("Math", [5, 6], "N")
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual([4, 5, 6, 5, 6], self.student.courses["Math"])

    def test_student_enroll__when_course_not_exist__expected_course_notes_update(self):
        result = self.student.enroll("English", [4, 4.5], "Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual([4, 4.5], self.student.courses["English"])

    def test_student_enroll__when_course_not_exist_default_str_notes__expected_course_notes_update(self):
        result = self.student.enroll("Chemistry", [4, 4.5])
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual([4, 4.5], self.student.courses["Chemistry"])

    def test_student_enroll__when_course_not_exist__expected_new_course(self):
        result = self.student.enroll("French", [4, 4.5], "N")
        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.student.courses["French"])

    def test_student_add_notes__when_no_course__expected_error(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Spanish", [4, 4.5])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_student_add_notes__when_exist_course__expected_notes_update(self):
        result = self.student.add_notes("IT", 6)
        self.assertEqual("Notes have been updated", result)
        self.assertEqual([5.5, 6, 6], self.student.courses["IT"])

    def test_student_leave_course__course_not_exist__expected_error(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Japanese")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_student_leave_course__course_exist__expected_pop_course(self):
        result = self.student.leave_course("Math")
        self.assertEqual("Course has been removed", result)
        self.assertNotIn("Math", self.student.courses)


if __name__ == "__main__":
    unittest.main()
