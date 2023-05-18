from abc import ABC

from app.studentInterface import StudentInterface
from app.models import *


class StudentGradesRepository(StudentInterface, ABC):

    def student_marks(self, id_student: int, lst):
        """Возращает все оценочки студента по предмету и айди"""
        lst1 = self.binary_search(lst[0], id_student)
        lst2 = self.binary_search(lst[1], id_student)
        grades = []
        for i in range(len(lst1)):
            if lst1[i] == '+' or lst1[i] == '-':
                grades.append(
                    GradeModel(
                        day=lst[0][1][i],
                        theme=lst[0][0][i],
                        mark=lst1[i + 1]
                    ))
        for i in range(len(lst2)):
            if lst2[i].isdigit() and i != 0:
                theme = lst[1][0][i - 1]
                if theme == '':
                    theme = lst[1][0][i]
                grades.append(
                    GradeModel(
                        day=lst[1][1][i],
                        theme=theme,
                        mark=lst2[i]
                    ))
            # if lst2[i - 1] == '' and lst2[i] == '':
            # Я ФИГ ЗНАЕТ ЗАЧЕМ ЭТО, НО ВРОДЕ БЕЗ ЭТОГО ЩАС РАБОТАЕТ, ЛУЧШЕ ОСТАВИТЬ.
            # ЕСЛИ КОГДА ТО БЫЛО НАПИСАНО, ЗНАЧИТЬ НУЖНО
            #     theme = lst[1][0][i - 1]
            #     if theme == '':
            #         theme = lst[1][0][i]
            #     grades['marks'].append({
            #         'theme': theme,
            #         'mark': ''
            #     })

        return StudentGradesModel(
            student_id=lst1[0],
            student_name=lst1[1],
            student_grades=grades
        )

    def students_marks(self, lst):
        """Возращает все оценочки студентов по предмету"""
        students = []
        for j in range(len(lst[0])):
            if lst[0][j][0].isdigit():
                id_student = lst[0][j][0]
                students.append(
                    self.student_marks(id_student=id_student, lst=lst)
                )
        return StudentsGradeModel(
            subject=lst[0][0][1],
            subject_description="Описание",
            group_name=lst[0][0][0],
            students=students
        )
