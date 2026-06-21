import pandas as pd

from src.models.load_record import LoadRecord


class Reader:
    """
    Читает Excel-файлы нагрузки
    и преобразует строки таблицы
    в объекты LoadRecord.
    """

    def read(self, file_path: str, sheet_name: str | int = 0) -> list[LoadRecord]:
        """
        Загружает Excel-файл
        и возвращает список записей.
        """

        dataframe = pd.read_excel(file_path, sheet_name=sheet_name)

        records: list[LoadRecord] = []

        for _, row in dataframe.iterrows():
            if self._is_empty_row(row):
                break

            if (
                self._get_string_value(row["Группы"]) == ""
                and self._get_string_value(row["Дисциплина"]) == ""
                and self._get_string_value(row["Вид нагрузки"]) == ""
            ):
                continue

            record = LoadRecord(
                group=self._get_string_value(row["Группы"]),
                discipline=self._get_string_value(row["Дисциплина"]),
                load_type=self._get_string_value(row["Вид нагрузки"]),
                teacher=self._get_string_value(row["ФИО"]),
                hours=self._get_float_value(row["Нагрузка"]),
            )

            records.append(record)

        return records

    def _is_empty_row(self, row) -> bool:
        """
        Проверяет, является ли строка
        полностью пустой.
        """

        return (
            pd.isna(row["Дисциплина"])
            and pd.isna(row["Вид нагрузки"])
            and pd.isna(row["Группы"])
            and pd.isna(row["Нагрузка"])
        )

    def _get_string_value(self, value) -> str:
        """
        Возвращает строку без пробелов.
        Для пустых ячеек возвращает "".
        """

        if pd.isna(value):
            return ""

        return str(value).strip()

    def _get_float_value(self, value) -> float:
        """
        Возвращает числовое значение.
        Для пустых ячеек возвращает 0.0
        """

        if pd.isna(value):
            return 0.0

        return float(value)
