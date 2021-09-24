import logging

import pytest
from freezegun import freeze_time

from tests.mocks import mocks_module_name
from tests.mocks_async import (
    async_exception_not_caught,
    async_exception_caught_and_not_raised,
    async_exception_caught_and_raised,
    mocks_async_module_name,
    mocks_async_working_directory,
    MockAsyncClass,
)
from tests.test_log_decorator import FREEZE_TIME, assert_exception_test


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
            module_name=mocks_module_name(),
            method_name="async_exception_not_caught",
            variables="value1: int = 3, value2: int = 3",
            working_directory=mocks_async_working_directory(),
            is_async=True,
            exception_name="ZeroDivisionError",
        )

    @freeze_time(FREEZE_TIME)
    @pytest.mark.asyncio
    async def test_exception_caught_and_not_raised(self, caplog):
        with caplog.at_level(level=logging.ERROR, logger=mocks_async_module_name()):
            try:
                await async_exception_caught_and_not_raised(3, 3)
            except ZeroDivisionError:
                pass
        assert caplog.text == ""

    @freeze_time(FREEZE_TIME)
    @pytest.mark.asyncio
    async def test_exception_caught_and_raised(self, caplog):
        with caplog.at_level(level=logging.ERROR, logger=mocks_async_module_name()):
            try:
                await async_exception_caught_and_raised(3, 3)
            except ZeroDivisionError:
                pass
        assert_exception_test(
            caplog=caplog,
            module_name=mocks_module_name(),
            method_name="async_exception_caught_and_raised",
            variables="value1: int = 3, value2: int = 3",
            working_directory=mocks_async_working_directory(),
            is_async=True,
            exception_name="ZeroDivisionError",
        )


class TestExceptionClassLogDecorator:
    @freeze_time(FREEZE_TIME)
    @pytest.mark.asyncio
    async def test_exception_not_caught(self, caplog):
        with caplog.at_level(level=logging.ERROR, logger=mocks_module_name()):
            try:
                mock = MockAsyncClass()
                await mock.async_exception_not_caught(3, 3)
            except ZeroDivisionError:
                pass
        assert_exception_test(
            caplog=caplog,
            module_name=mocks_module_name(),
            method_name="MockAsyncClass.async_exception_not_caught",
            variables="value1: int = 3, value2: int = 3",
            working_directory=mocks_async_working_directory(),
            is_async=True,
            exception_name="ZeroDivisionError",
        )

    @freeze_time(FREEZE_TIME)
    @pytest.mark.asyncio
    async def test_exception_caught_and_not_raised(self, caplog):
        with caplog.at_level(level=logging.ERROR, logger=mocks_module_name()):
            try:
                mock = MockAsyncClass()
                await mock.async_exception_caught_and_not_raised(3, 3)
            except ZeroDivisionError:
                pass
        assert caplog.text == ""

    @freeze_time(FREEZE_TIME)
    @pytest.mark.asyncio
    async def test_exception_caught_and_raised(self, caplog):
        with caplog.at_level(level=logging.ERROR, logger=mocks_module_name()):
            try:
                mock = MockAsyncClass()
                await mock.async_exception_caught_and_raised(3, 3)
            except ZeroDivisionError:
                pass
        assert_exception_test(
            caplog=caplog,
            module_name=mocks_module_name(),
            method_name="MockAsyncClass.async_exception_caught_and_raised",
            variables="value1: int = 3, value2: int = 3",
            working_directory=mocks_async_working_directory(),
            is_async=True,
            exception_name="ZeroDivisionError",
        )
