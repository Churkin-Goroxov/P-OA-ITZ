from src.models.load_record import LoadRecord


class LoadAggregator:
    """
    Объединяет одинаковые записи нагрузки
    и суммирует их часы.
    """

    def aggregate(self, records: list[LoadRecord]) -> list[LoadRecord]:

        records_by_key: dict[
            tuple[str, str, str],
            float
        ] = {}

        for record in records:

            key = record.get_match_key()

            if key not in records_by_key:
                records_by_key[key] = 0.0

            records_by_key[key] += record.hours

        result: list[LoadRecord] = []

        for key, hours in records_by_key.items():

            group, discipline, load_type = key

            result.append(
                LoadRecord(
                    group=group,
                    discipline=discipline,
                    load_type=load_type,
                    teacher="",
                    hours=hours
                )
            )

        return result
