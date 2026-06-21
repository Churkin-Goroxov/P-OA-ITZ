from src.models import LoadRecord


class Distributor:
    """
    Распределяет нагрузку пропорционально
    прошлогоднему распределению часов.
    """

    def distribute(
            self,
            current_record: LoadRecord,
            old_records: list[LoadRecord]
    ) -> list[LoadRecord]:
        """
        Распределяет часы текущей записи между
        преподавателями из прошлогодних записей.

        Возвращает список новых записей
        с рассчитанными часами.
        """

        valid_records = self._get_valid_records(old_records)

        if not valid_records:
            return []

        if len(valid_records) <= 2:
            return []

        total_hours = self._get_total_hours(valid_records)

        if total_hours <= 0:
            return []

        result: list[LoadRecord] = []

        for old_record in valid_records:

            share = old_record.hours / total_hours

            new_hours = current_record.hours * share

            new_record = LoadRecord(
                semester=current_record.semester,
                group=current_record.group,
                discipline=current_record.discipline,
                load_type=current_record.load_type,
                teacher=old_record.teacher,
                hours=new_hours
            )

            result.append(new_record)

        return result

    def _get_valid_records(
            self,
            records: list[LoadRecord]
    ) -> list[LoadRecord]:
        """
        Оставляет только записи с преподавателем
        и положительным количеством часов.
        """

        valid_records = []

        for record in records:

            if not record.has_teacher():
                continue

            if record.hours <= 0:
                continue

            valid_records.append(record)

        return valid_records

    def _get_total_hours(
            self,
            records: list[LoadRecord]
    ) -> float:
        """
        Возвращает суммарное количество часов.
        """

        total_hours = 0.0

        for record in records:
            total_hours += record.hours

        return total_hours