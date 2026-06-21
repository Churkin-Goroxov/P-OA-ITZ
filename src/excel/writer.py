import pandas as pd

from src.models.load_record import LoadRecord


class Writer:

    def write(self, records: list[LoadRecord], file_path: str) -> None:

        data = []

        for record in records:

            data.append(
                {
                    "Группы": record.group,
                    "Дисциплина": record.discipline,
                    "Вид нагрузки": record.load_type,
                    "ФИО": record.teacher,
                    "Нагрузка": record.hours
                }
            )

        dataframe = pd.DataFrame(data)

        dataframe.to_excel(file_path, index=False)
