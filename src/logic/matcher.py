from src.models import LoadRecord


class Matcher:
    """
    Поиск соответствий между нагрузкой
    текущего и прошлого учебного года.
    """

    def __init__(
            self,
            old_records: list[LoadRecord]
    ) -> None:
        """
        Создает индекс записей прошлого года
        для быстрого поиска.
        """

        self.records_by_key: dict[
            tuple[str, str, str],
            list[LoadRecord]
        ] = {}

        self._build_index(old_records)

    def _build_index(
            self,
            records: list[LoadRecord]
    ) -> None:
        """
        Строит словарь вида:
        {
            (group, discipline, load_type): [
                LoadRecord,
                LoadRecord,
                ...
            ]
        }
        """

        for record in records:

            key = record.get_match_key()

            if key not in self.records_by_key:
                self.records_by_key[key] = []

            self.records_by_key[key].append(record)

    def find_matches(
            self,
            current_record: LoadRecord
    ) -> list[LoadRecord]:
        """
        Возвращает все совпадающие записи
        прошлого года.
        """

        key = current_record.get_match_key()

        return self.records_by_key.get(key, [])
