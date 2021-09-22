from pathlib import Path

from src.ecgai_logging.log_decorator import log


def mocks_module_name():
    return __name__


def mocks_working_directory():
    return Path.cwd()


@log
def input_int_return_none(value1: int, value2: int) -> None:
    _ = value1 + value2
    return


@log
def input_int_return_none_call_sub_function(value1: int, value2: int) -> None:
    input_int_return_none(value1, value2)
    return


@log
def input_int_return_typed_int(value1: int, value2: int) -> int:
    total = value1 + value2
    return total


@log
def input_int_return_typed_int_call_sub_function(value1: int, value2: int) -> int:
    return input_int_return_typed_int(value1, value2)


@log
def input_int_return_untyped_int(value1: int, value2: int) -> int:
    total = value1 + value2
    return total


@log
def input_int_return_untyped_str(value1: int, value2: int):
    _ = value1 + value2
    return 'total return value'


@log
def input_int_return_typed_str(value1: int, value2: int) -> str:
    _ = value1 + value2
    return 'total return value'


# noinspection PyUnusedLocal
@log
def exception_caught_and_raised(value1: int, value2: int):
    try:
        _ = 5 / 0
    except ZeroDivisionError as e:
        raise


# noinspection PyUnusedLocal
@log
def exception_caught_and_not_raised(value1: int, value2: int):
    try:
        _ = 5 / 0
    except ZeroDivisionError as e:
        pass


# noinspection PyUnusedLocal
@log
def exception_not_caught(value1: int, value2: int):
    _ = 5 / 0


class MockClass:
    @log
    def input_int_return_none(self, value1: int, value2: int) -> None:
        _ = value1 + value2
        return

    @log
    def input_int_return_none_call_sub_function(self, value1: int, value2: int) -> None:
        self.input_int_return_none(value1, value2)
        return

    @log
    def input_int_return_typed_int(self, value1: int, value2: int) -> int:
        total = value1 + value2
        return total

    @log
    def input_int_return_untyped_int(self, value1: int, value2: int) -> int:
        total = value1 + value2
        return total

    @log
    def input_int_return_untyped_str(self, value1: int, value2: int):
        _ = value1 + value2
        return 'total return value'

    @log
    def input_int_return_typed_str(self, value1: int, value2: int) -> str:
        _ = value1 + value2
        return 'total return value'

    @log
    def input_int_return_typed_int_call_sub_function(self, value1: int, value2: int) -> int:
        return self.input_int_return_typed_int(value1, value2)

    # noinspection PyUnusedLocal
    @log
    def exception_caught_and_raised(self, value1: int, value2: int):
        try:
            _ = 5 / 0
        except ZeroDivisionError as e:
            raise

    # noinspection PyUnusedLocal
    @log
    def exception_caught_and_not_raised(self, value1: int, value2: int):
        try:
            _ = 5 / 0
        except ZeroDivisionError as e:
            pass

    # noinspection PyUnusedLocal
    @log
    def exception_not_caught(self, value1: int, value2: int):
        _ = 5 / 0
