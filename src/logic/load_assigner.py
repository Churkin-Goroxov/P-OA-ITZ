from src.logic.distributor import Distributor
from src.logic.matcher import Matcher
from src.models.load_record import LoadRecord


class LoadAssigner:
    """
    Координирует процесс поиска соответствий и распределения
    нагрузки между преподавателями на основе данных прошлого года.
    """

    def __init__(self, old_records: list[LoadRecord]) -> None:

        self.matcher = Matcher(old_records)
        self.distributor = Distributor()

    def assign(self, current_records: list[LoadRecord]) -> list[LoadRecord]:
        """
        Обрабатывает записи текущего года, находит соответствующие записи
        прошлого года и выполняет распределение нагрузки.
        """

        result: list[LoadRecord] = []

        for current_record in current_records:

            if self._is_special_load(current_record):
                continue

            matches = self.matcher.find_matches(current_record)

            if not matches:
                continue

            distributed_records = (
                self.distributor.distribute(
                    current_record,
                    matches
                )
            )

            if distributed_records:
                result.extend(distributed_records)

        return result

    def _is_special_load(self, record: LoadRecord) -> bool:
        """
        Определяет нагрузки, которые должны обрабатываться
        отдельно на этапе добалансировки.
        """

        text = (record.discipline.lower() + " " + record.load_type.lower())

        keywords = [
            "диплом",
            "руководство",
            "магистр",
            "магистрант",
            "вкр"
        ]

        for keyword in keywords:
            if keyword in text:
                return True

        return False
