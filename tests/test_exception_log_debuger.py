import logging

from freezegun import freeze_time

from tests.mocks import mocks_module_name, exception_not_caught, exception_caught_and_not_raised, \
    exception_caught_and_raised, MockClass
from tests.test_log_decorator import remove_spaces_from_caplog, FREEZE_TIME


# logger = logging.getLogger(mocks_module_name())
# handler = colorlog.StreamHandler(sys.stdout)
# handler.setFormatter(
#     colorlog.ColoredFormatter("%(log_color)s%(levelname)s:%(name)s:%(message)s")
# )
#
# logger.addHandler(handler)


def assert_exception_test(caplog, method_name, variables, returns):
    log_text = remove_spaces_from_caplog(caplog=caplog)
    assert mocks_module_name() in log_text
    assert f"Traceback (most recent call last):".replace(" ", "") in log_text
    assert f"ZeroDivisionError: division by zero".replace(" ", "") in log_text


class TestExceptionFunctionLogDecorator:
    @freeze_time(FREEZE_TIME)
    def test_exception_not_caught(self, caplog):
        with caplog.at_level(level=logging.ERROR, logger=mocks_module_name()):
            try:
                exception_not_caught(3, 3)
            except ZeroDivisionError as e:
                pass
        assert_exception_test(
            caplog=caplog,
            method_name="exception_not_caught",
            variables="value1: int = 3, value2: int = 3",
            returns="NoneType = None",
        )

    @freeze_time(FREEZE_TIME)
    def test_exception_caught_and_not_raised(self, caplog):
        with caplog.at_level(level=logging.ERROR, logger=mocks_module_name()):
            try:
                exception_caught_and_not_raised(3, 3)
            except ZeroDivisionError as e:
                pass
        assert caplog.text == ''

    @freeze_time(FREEZE_TIME)
    def test_exception_caught_and_raised(self, caplog):
        with caplog.at_level(level=logging.ERROR, logger=mocks_module_name()):
            try:
                exception_caught_and_raised(3, 3)
            except ZeroDivisionError as e:
                pass
        assert_exception_test(
            caplog=caplog,
            method_name="exception_caught_and_raised",
            variables="value1: int = 3, value2: int = 3",
            returns="NoneType = None",
        )


class TestExceptionClassLogDecorator:
    @freeze_time(FREEZE_TIME)
    def test_exception_not_caught(self, caplog):
        with caplog.at_level(level=logging.ERROR, logger=mocks_module_name()):
            try:
                mock = MockClass()
                mock.exception_not_caught(3, 3)
            except ZeroDivisionError as e:
                pass
        assert_exception_test(
            caplog=caplog,
            method_name="MockClass.exception_not_caught",
            variables="value1: int = 3, value2: int = 3",
            returns="NoneType = None",
        )

    @freeze_time(FREEZE_TIME)
    def test_exception_caught_and_not_raised(self, caplog):
        with caplog.at_level(level=logging.ERROR, logger=mocks_module_name()):
            try:
                mock = MockClass()
                mock.exception_caught_and_not_raised(3, 3)
            except ZeroDivisionError as e:
                pass
        assert caplog.text == ''

    @freeze_time(FREEZE_TIME)
    def test_exception_caught_and_raised(self, caplog):
        with caplog.at_level(level=logging.ERROR, logger=mocks_module_name()):
            try:
                mock = MockClass()
                mock.exception_caught_and_raised(3, 3)
            except ZeroDivisionError as e:
                pass
        assert_exception_test(
            caplog=caplog,
            method_name="MockClass.exception_caught_and_raised",
            variables="value1: int = 3, value2: int = 3",
            returns="NoneType = None",
        )
