from src.logic.distributor import Distributor
from src.logic.matcher import Matcher
from src.models.load_record import LoadRecord


class LoadAssigner:
    """
    Переносит распределение преподавателей
    из прошлого года в текущий.
    """

    def __init__(
            self,
            old_records: list[LoadRecord]
    ) -> None:

        self.matcher = Matcher(old_records)
        self.distributor = Distributor()

    def assign(
            self,
            current_records: list[LoadRecord]
    ) -> list[LoadRecord]:

        result: list[LoadRecord] = []

        found_matches = 0
        not_found_matches = 0
        skipped_special = 0

        for current_record in current_records:

            if self._is_special_load(current_record):
                skipped_special += 1
                result.append(current_record)
                continue

            matches = self.matcher.find_matches(
                current_record
            )

            if not matches:
                not_found_matches += 1
                result.append(current_record)
                continue

            found_matches += 1

            distributed_records = (
                self.distributor.distribute(
                    current_record,
                    matches
                )
            )

            if distributed_records:
                result.extend(distributed_records)
            else:
                result.append(current_record)

        print()
        print("===== СТАТИСТИКА НАЗНАЧЕНИЯ =====")
        print(f"Найдено совпадений: {found_matches}")
        print(f"Не найдено совпадений: {not_found_matches}")
        print(f"Пропущено специальных нагрузок: {skipped_special}")
        print(f"Всего обработано: {len(current_records)}")
        print()

        return result

    def _is_special_load(
            self,
            record: LoadRecord
    ) -> bool:
        """
        Определяет нагрузки,
        которые должны обрабатываться
        отдельно на этапе добалансировки.
        """

        text = (
            record.discipline.lower()
            + " "
            + record.load_type.lower()
        )

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
