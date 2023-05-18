from abc import ABC

from app.models import *
from app.studentInterface import StudentInterface


class StudentMiddleGradesRepository(StudentInterface, ABC):
    def student_marks(self, id_student: int, lst) -> StudentMiddleGradeModel:
        """Возращает студента с его средним баллом по предмету"""
        middle_grade = StudentMiddleGradeModel()
        list_point = []
        for i in lst:
            j = self.binary_search(i, id_student)
            middle_grade.student_id = id_student
            middle_grade.student_name = j[1]
            list_point.extend(list(map(lambda x: int(x), list(filter(lambda x: x.isdigit(), j[1:])))))
        middle_grade.middle_grade = round(sum(list_point) / len(list_point), 2)
        return middle_grade

    def students_marks(self, lst) -> StudentMiddleGradesModel:
        """Возращает список всех учащихся группы с их средним баллом по предмету"""
        middle_grades = StudentMiddleGradesModel()
        ListOfMiddleGrades = []
        for j in range(len(lst[0])):
            if lst[0][j][0].isdigit():
                ListOfMiddleGrades.append(
                    self.student_marks(
                        id_student=lst[0][j][0],
                        lst=lst
                    ))
        middle_grades.list_grade = ListOfMiddleGrades
        return middle_grades
