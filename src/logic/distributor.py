from src.models.load_record import LoadRecord


class Distributor:
    """
    Распределяет нагрузку пропорционально
    прошлогоднему распределению часов.
    """

    def distribute(self, current_record: LoadRecord, old_records: list[LoadRecord]) -> list[LoadRecord]:
        """
        Распределяет часы текущей записи между
        преподавателями из прошлогодних записей.

        Возвращает список новых записей
        с рассчитанными часами.
        """

        valid_records = self._get_valid_records(old_records)

        if not valid_records:
            return []

        total_hours = self._get_total_hours(valid_records)

        if total_hours <= 0:
            return []

        result: list[LoadRecord] = []

        teacher_hours: dict[str, float] = {}

        for record in valid_records:

            if record.teacher not in teacher_hours:
                teacher_hours[record.teacher] = 0.0

            teacher_hours[record.teacher] += record.hours

        # Основное условие задания по количеству преподавателей
        if len(teacher_hours) <= 2:
            return []

        for teacher, hours in teacher_hours.items():
            share = hours / total_hours

            new_hours = current_record.hours * share

            new_record = LoadRecord(
                group=current_record.group,
                discipline=current_record.discipline,
                load_type=current_record.load_type,
                teacher=teacher,
                hours=new_hours
            )

            result.append(new_record)

        return result

    def _get_valid_records(self, records: list[LoadRecord]) -> list[LoadRecord]:
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

    def _get_total_hours(self, records: list[LoadRecord]) -> float:
        """
        Возвращает суммарное количество часов.
        """

        total_hours = 0.0

        for record in records:
            total_hours += record.hours

        return total_hours
