class VaccineError(Exception):
    """Базовий клас для помилок, пов'язаних із вакцинацією."""

    def __init__(self, message: str) -> None:
        super().__init__(message)


class NotVaccinatedError(VaccineError):
    """Помилка: відвідувач не вакцинований."""

    def __init__(self) -> None:
        super().__init__("Visitor is not vaccinated.")


class OutdatedVaccineError(VaccineError):
    """Помилка: вакцина прострочена."""

    def __init__(self) -> None:
        super().__init__("Visitor's vaccine is outdated.")


class NotWearingMaskError(Exception):
    """Помилка: відвідувач без маски."""

    def __init__(self) -> None:
        super().__init__("Visitor is not wearing a mask.")
