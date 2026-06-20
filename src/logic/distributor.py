from src.models import LoadRecord


class Distributor:
    """
    Распределяет нагрузку пропорционально
    прошлогоднему распределению часов.
    """

    def distribute(
            self,
            current_hours: float,
            old_records: list[LoadRecord]
    ) -> dict[str, float]:
        """
        Возвращает распределение часов
        между преподавателями.

        Формат результата:

        {
            "Иванов": 80.0,
            "Петров": 60.0
        }
        """

        total_hours = self._get_total_hours(old_records)

        if total_hours == 0:
            raise ValueError("Невозможно распределить нагрузку: сумма часов равна нулю.")

        result = {}

        for record in old_records:

            share = record.hours / total_hours

            result[record.teacher] = current_hours * share

        return result

    def _get_total_hours(
            self,
            records: list[LoadRecord]
    ) -> float:
        """
        Возвращает суммарное количество часов.
        """

        total_hours = 0

        for record in records:
            total_hours += record.hours

        return total_hours
