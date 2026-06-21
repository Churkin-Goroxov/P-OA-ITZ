import pandas as pd

from src.models.load_record import LoadRecord


class Writer:
    """
    Сохраняет список записей нагрузки в Excel-файл
    """

    def write(self, records: list[LoadRecord], file_path: str) -> None:
        """
        Записывает список нагрузок в Excel-файл
        """

        data: list[dict[str, str | float]] = []

        for record in records:
            data.append(
                {
                    "Группы": record.group,
                    "Дисциплина": record.discipline,
                    "Вид нагрузки": record.load_type,
                    "ФИО": record.teacher,
                    "Нагрузка": record.hours,
                }
            )

        dataframe = pd.DataFrame(data)

        dataframe.to_excel(file_path, index=False)
