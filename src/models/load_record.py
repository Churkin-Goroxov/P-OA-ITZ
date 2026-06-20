class LoadRecord:
    """
    Запись учебной нагрузки.

    Параметры:
        group       — учебная группа
        discipline  — дисциплина
        load_type   — вид нагрузки
        teacher     — преподаватель
        hours       — количество часов
    """

    def __init__(
            self,
            group,
            discipline,
            load_type,
            teacher,
            hours
    ):
        self.group = group
        self.discipline = discipline
        self.load_type = load_type
        self.teacher = teacher
        self.hours = hours

    def get_match_key(self) -> tuple[str, str, str]:
        """
        Возвращает ключ для поиска совпадений.
        """

        return (
            self.group,
            self.discipline,
            self.load_type
        )

    def has_teacher(self) -> bool:
        """
        Проверяет наличие преподавателя.
        """

        return bool(str(self.teacher).strip())

    def is_same_load(
            self,
            other: "LoadRecord"
    ) -> bool:
        """
        Проверяет совпадение нагрузки.
        """
        if not isinstance(other, LoadRecord):
            return False

        return self.get_match_key() == other.get_match_key()

    # Инструмент для отладки
    def __repr__(self) -> str:
        return (
            f"LoadRecord("
            f"group='{self.group}', "
            f"discipline='{self.discipline}', "
            f"load_type='{self.load_type}', "
            f"teacher='{self.teacher}', "
            f"hours={self.hours})"
        )
