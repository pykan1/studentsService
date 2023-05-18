from pydantic import BaseModel


class StudentMiddleGradeModel(BaseModel):
    student_id: str | None
    student_name: str | None
    middle_grade: str | None


class StudentMiddleGradesModel(BaseModel):
    list_grade: list[StudentMiddleGradeModel] | None


class GradeModel(BaseModel):
    day: str | None
    theme: str | None
    mark: str | None

    def __init__(self, day, theme, mark, **kwargs):
        super().__init__(**kwargs)
        self.day = day
        self.theme = theme
        self.mark = mark


class StudentGradesModel(BaseModel):
    student_id: str | None
    student_name: str | None
    student_grades: list[GradeModel] | None

    def __init__(self, student_id, student_name, student_grades, **kwargs):
        super().__init__(**kwargs)
        self.student_id = student_id
        self.student_name = student_name
        self.student_grades = student_grades


class StudentsGradeModel(BaseModel):
    subject: str | None
    subject_description: str | None
    group_name: str | None
    students: list[StudentGradesModel] | None

    def __init__(self, subject, subject_description, group_name, students: list[StudentGradesModel], **kwargs):
        super().__init__(**kwargs)
        self.subject = subject
        self.subject_description = subject_description
        self.group_name = group_name
        self.students = students