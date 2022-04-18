class CustomError(Exception):
    pass


class NameTooShortError(CustomError):
    pass


class MustContainAtSymbolError(CustomError):
    pass


class InvalidDomainError(CustomError):
    pass