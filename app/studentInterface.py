from abc import ABC, abstractmethod

from pydantic import BaseModel

from repositories.SheetRepository import SheetRepository


class StudentInterface(SheetRepository, ABC, BaseModel):

    def list_page(self, link_table):  # вывод массива из двух листов(посещаемость и дз)
        group_n_visitingeating = self.sheet_service().values().get(spreadsheetId=link_table,
                                                                  range=f"Посещаемость!a:z").execute()
        group_n_visitingeating_values = group_n_visitingeating.get('values', [])

        group_n_homework = self.sheet_service().values().get(spreadsheetId=link_table,
                                                            range=f"дз!a:z").execute()
        group_n_homework_values = group_n_homework.get('values', [])
        for i in group_n_visitingeating_values:
            if i[0].isdigit():
                if len(i) == len(group_n_visitingeating_values[0]):
                    i.append('')
        for i in group_n_homework_values:
            if i[0].isdigit():
                if len(i) == len(group_n_homework_values[0]):
                    i.append('')
        return [group_n_visitingeating_values, group_n_homework_values]

    @staticmethod
    def binary_search(list_table, id_student):
        low = 0
        high = len(list_table) - 1

        while low <= high:
            mid = (low + high) // 2
            if int(list_table[mid][0]) == int(id_student):
                return list_table[mid]
            elif int(list_table[mid][0]) < int(id_student):
                low = mid + 1
            else:
                high = mid - 1
        return -1

    @abstractmethod
    def student_marks(self, id_student, lst):
        pass

    @abstractmethod
    def students_marks(self, lst):
        pass
