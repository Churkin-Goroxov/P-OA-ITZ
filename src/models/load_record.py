class LoadRecord:
    """
    Запись учебной нагрузки.

    Параметры:
        group       - учебная группа
        discipline  - дисциплина
        load_type   - вид нагрузки
        teacher     - преподаватель
        hours       - количество часов
    """

    def __init__(
        self, group: str, discipline: str, load_type: str, teacher: str, hours: float
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

        return (self.group, self.discipline, self.load_type)

    def has_teacher(self) -> bool:
        """
        Проверяет наличие преподавателя.
        """

        return self.teacher != ""

    # Инструмент для отладки
    def __repr__(self) -> str:
        return (
            f"LoadRecord("
            f"group='{self.group}', "
            f"discipline='{self.discipline}', "
            f"load_type='{self.load_type}', "
            f"teacher='{self.teacher}', "
            f"hours={self.hours}"
            f")"
        )
