from fastapi import APIRouter, Depends
from app.service import StudentService
from app.models import *
from app.studentInterface import StudentInterface

student_route = APIRouter(
    prefix="/student",
    tags=["google table"],
    responses={404: {"description": "Not found"}},
)


@student_route.post("/student_middle_grade/{link_table}/{id_student}", response_model=StudentMiddleGradeModel)
async def middle_grade(
        link_table: str,
        id_student,
        student_service: StudentService = Depends(),

):
    return student_service.student_middle_grade(id_student, link_table)


@student_route.post("/students_middle_grades/{link_table}", response_model=StudentMiddleGradesModel)
async def middles_grade(
        link_table: str,
        student_service: StudentService = Depends(),

):
    return student_service.students_middle_grade(link_table)


@student_route.post("/student_marks/{link_table}/{id_student}", response_model=StudentGradesModel)
async def grade(
        link_table: str,
        id_student: str,
        student_service: StudentService = Depends()
):
    return student_service.student_grades(link_table, id_student)


@student_route.post("/students_marks/{link_table}", response_model=StudentsGradeModel)
async def grades(
        link_table: str,
        student_service: StudentService = Depends()
):
    return student_service.students_grades(link_table)
