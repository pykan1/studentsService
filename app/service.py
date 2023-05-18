from models import *
from repositories.StudentGradesRepository import StudentGradesRepository
from repositories.StudentMiddleGradeRepository import StudentMiddleGradesRepository


class StudentService:
    def __init__(
            self,
            grades_repository: StudentGradesRepository,
            middle_grades_repository: StudentMiddleGradesRepository
    ):
        self._studentMiddleGrades: StudentMiddleGradesRepository = middle_grades_repository
        self._studentGrades: StudentGradesRepository = grades_repository

    def student_middle_grade(self, id_student, link_table) -> StudentMiddleGradeModel:
        """Средняя оценка студента по айди и предмету"""
        lst = self._studentGrades.list_page(link_table)
        return self._studentMiddleGrades.student_marks(
            id_student=id_student,
            lst=lst
        )

    def students_middle_grade(self, link_table) -> StudentMiddleGradesModel:
        """Средние оценки студентов по предмету"""
        lst = self._studentGrades.list_page(link_table)
        return self._studentMiddleGrades.students_marks(lst=lst)

    def student_grades(self, id_student, link_table) -> StudentGradesModel:
        """Все оценки студента по айди и предмету"""
        lst = self._studentGrades.list_page(link_table)
        return self._studentGrades.student_marks(
            id_student=id_student,
            lst=lst
        )

    def students_grades(self, link_table) -> StudentsGradeModel:
        """Оценки всех студентов по предмету"""
        lst = self._studentGrades.list_page(link_table)
        return self._studentGrades.students_marks(lst=lst)
