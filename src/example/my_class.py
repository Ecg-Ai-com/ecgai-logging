from typing import Tuple

from src.ecgai_logging.log_decorator import log


class MyClass(object):

    def __init__(self):
        pass

    @log
    def just_testing(self, a, b, c) -> Tuple[int, int, int]:
        return c * 10, b * 10, a * 10

    @log
    def just_testing2(self, a, b, c):
        return c * 10, b * 10, a * 10

    @log
    def just_testing3(self, a, b, c):
        return c * 10 * b * 10 * a * 10

    @log
    def just_testing4(self, a, b, c) -> None:
        return

    @log
    def just_testing5(self, a, b, c):
        return

    @log
    def just_testing6(self, a, b, c):
        return self.just_testing8(self.just_testing7(a, b, c))

    @log
    def just_testing7(self, a, b, c):
        return c * 10 * b * 10 * a * 10

    @log
    def just_testing8(self, m):
        return m * 562145 / 12.3

    @log
    def just_testing9(self, j):
        try:
            g = j / 0
            return g
        except ZeroDivisionError:
            pass

    @log
    def just_testing10(self, j):
        g = j / 0


@log
def just_another_test(a, b, c):
    return c, b, a
