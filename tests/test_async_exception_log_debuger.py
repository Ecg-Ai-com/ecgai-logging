import logging

import pytest
from freezegun import freeze_time

from tests.mocks import mocks_module_name, MockClass
from tests.mocks_async import async_exception_not_caught, async_exception_caught_and_not_raised, \
    async_exception_caught_and_raised, mocks_async_module_name
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


class TestAsyncExceptionFunctionLogDecorator:
    @freeze_time(FREEZE_TIME)
    @pytest.mark.asyncio
    async def test_exception_not_caught(self, caplog):
        with caplog.at_level(level=logging.ERROR, logger=mocks_async_module_name()):
            try:
                await async_exception_not_caught(3, 3)
            except ZeroDivisionError as e:
                print(e)
                pass
        assert_exception_test(
            caplog=caplog,
            method_name="exception_not_caught",
            variables="value1: int = 3, value2: int = 3",
            returns="NoneType = None",
        )

    @freeze_time(FREEZE_TIME)
    @pytest.mark.asyncio
    async def test_exception_caught_and_not_raised(self, caplog):
        with caplog.at_level(level=logging.ERROR, logger=mocks_async_module_name()):
            try:
                await async_exception_caught_and_not_raised(3, 3)
            except ZeroDivisionError as e:
                pass
        assert caplog.text == ''

    @freeze_time(FREEZE_TIME)
    @pytest.mark.asyncio
    async def test_exception_caught_and_raised(self, caplog):
        with caplog.at_level(level=logging.ERROR, logger=mocks_async_module_name()):
            try:
                await async_exception_caught_and_raised(3, 3)
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
