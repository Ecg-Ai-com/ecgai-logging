import logging

from freezegun import freeze_time

from tests.mocks import (
    mocks_module_name,
    exception_not_caught,
    exception_caught_and_not_raised,
    exception_caught_and_raised,
    MockClass,
    mocks_working_directory,
)
from tests.test_log_decorator import FREEZE_TIME, assert_exception_test


# logger = logging.getLogger(mocks_module_name())
# handler = colorlog.StreamHandler(sys.stdout)
# handler.setFormatter(
#     colorlog.ColoredFormatter("%(log_color)s%(levelname)s:%(name)s:%(message)s")
# )
#
# logger.addHandler(handler)
# caplog,
# module_name,
# method_name,
# variables,
# returns,
# working_directory,
# is_async,
# exception_name,


class TestExceptionFunctionLogDecorator:
    @freeze_time(FREEZE_TIME)
    def test_exception_not_caught(self, caplog):
        with caplog.at_level(level=logging.ERROR, logger=mocks_module_name()):
            try:
                exception_not_caught(3, 3)
            except ZeroDivisionError:
                pass
        assert_exception_test(
            caplog=caplog,
            module_name=mocks_module_name(),
            method_name="exception_not_caught",
            variables="value1: int = 3, value2: int = 3",
            working_directory=mocks_working_directory(),
            is_async=False,
            exception_name="ZeroDivisionError",
        )

    @freeze_time(FREEZE_TIME)
    def test_exception_caught_and_not_raised(self, caplog):
        with caplog.at_level(level=logging.ERROR, logger=mocks_module_name()):
            try:
                exception_caught_and_not_raised(3, 3)
            except ZeroDivisionError:
                pass
        assert caplog.text == ""

    @freeze_time(FREEZE_TIME)
    def test_exception_caught_and_raised(self, caplog):
        with caplog.at_level(level=logging.ERROR, logger=mocks_module_name()):
            try:
                exception_caught_and_raised(3, 3)
            except ZeroDivisionError:
                pass
        assert_exception_test(
            caplog=caplog,
            module_name=mocks_module_name(),
            method_name="exception_caught_and_raised",
            variables="value1: int = 3, value2: int = 3",
            working_directory=mocks_working_directory(),
            is_async=False,
            exception_name="ZeroDivisionError",
        )


class TestExceptionClassLogDecorator:
    @freeze_time(FREEZE_TIME)
    def test_exception_not_caught(self, caplog):
        with caplog.at_level(level=logging.ERROR, logger=mocks_module_name()):
            try:
                mock = MockClass()
                mock.exception_not_caught(3, 3)
            except ZeroDivisionError:
                pass
        assert_exception_test(
            caplog=caplog,
            module_name=mocks_module_name(),
            method_name="MockClass.exception_not_caught",
            variables="value1: int = 3, value2: int = 3",
            working_directory=mocks_working_directory(),
            is_async=False,
            exception_name="ZeroDivisionError",
        )

    @freeze_time(FREEZE_TIME)
    def test_exception_caught_and_not_raised(self, caplog):
        with caplog.at_level(level=logging.ERROR, logger=mocks_module_name()):
            try:
                mock = MockClass()
                mock.exception_caught_and_not_raised(3, 3)
            except ZeroDivisionError:
                pass
        assert caplog.text == ""

    @freeze_time(FREEZE_TIME)
    def test_exception_caught_and_raised(self, caplog):
        with caplog.at_level(level=logging.ERROR, logger=mocks_module_name()):
            try:
                mock = MockClass()
                mock.exception_caught_and_raised(3, 3)
            except ZeroDivisionError:
                pass
        assert_exception_test(
            caplog=caplog,
            module_name=mocks_module_name(),
            method_name="MockClass.exception_caught_and_raised",
            variables="value1: int = 3, value2: int = 3",
            working_directory=mocks_working_directory(),
            is_async=False,
            exception_name="ZeroDivisionError",
        )
