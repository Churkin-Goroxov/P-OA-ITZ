from src.excel.reader import Reader
from src.excel.writer import Writer
from src.logic.load_aggregator import LoadAggregator
from src.logic.load_assigner import LoadAssigner


def main() -> None:
    """
    Точка входа программы.

    Алгоритм работы:

    1. Чтение нагрузки прошлого года.
    2. Чтение осеннего и весеннего семестров текущего года.
    3. Объединение нагрузок текущего года.
    4. Агрегация одинаковых записей.
    5. Поиск соответствий с прошлым годом.
    6. Пропорциональное распределение нагрузки между преподавателями.
    7. Сохранение результата в Excel-файл.
    """

    # Чтение исходных данных
    reader = Reader()
    old_records = reader.read("src/data/15 вариант.xls")
    autumn_records = reader.read("src/data/Список 15вар - осень.xls")
    spring_records = reader.read("src/data/Список 15вар - весна.xls")

    # Формирование нагрузки текущего года
    current_records = (autumn_records + spring_records)

    # Объединение одинаковых записей
    aggregator = LoadAggregator()
    current_records = aggregator.aggregate(current_records)

    # Перенос распределения преподавателей
    assigner = LoadAssigner(old_records)
    result_records = assigner.assign(current_records)

    # Сохранение результата
    writer = Writer()
    writer.write(result_records, "src/data/result.xlsx")
    print("Файл result.xlsx сохранен")


if __name__ == "__main__":
    main()
