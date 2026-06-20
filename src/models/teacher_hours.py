class TeacherHours:
    """
    Нагрузка преподавателя.
    """

    def __init__(self, teacher, hours):
        self.teacher = teacher
        self.hours = hours

    def is_positive(self) -> bool:
        """
        Проверяет наличие нагрузки.
        """

        return self.hours > 0

    def share_from(
            self,
            total_hours: float
    ) -> float:
        """
        Возвращает долю преподавателя
        от общего количества часов.
        """

        if total_hours <= 0:
            raise ValueError(
                "Общее количество часов должно быть больше нуля."
            )

        return self.hours / total_hours

    # Инструмент для отладки
    def __repr__(self) -> str:
        return (
            f"TeacherHours("
            f"teacher='{self.teacher}', "
            f"hours={self.hours})"
        )