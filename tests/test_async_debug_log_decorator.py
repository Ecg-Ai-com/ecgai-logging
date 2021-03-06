import asyncio
import logging

import pytest
from freezegun import freeze_time

from tests.mocks_async import (
    async_input_int_return_untyped_int,
    mocks_async_module_name,
    async_input_int_return_untyped_str,
    mocks_async_working_directory,
)
from tests.test_log_decorator import assert_debug_test, FREEZE_TIME


class TestDebugFunctionLogDecorator:
    @freeze_time(FREEZE_TIME)
    @pytest.mark.asyncio
    async def test_debug_function_async_input_int_return_untyped_int(self, caplog):
        with caplog.at_level(level=logging.DEBUG, logger=mocks_async_module_name()):
            _ = await asyncio.create_task(async_input_int_return_untyped_int(3, 3))
        assert_debug_test(
            caplog=caplog,
            module_name=mocks_async_module_name(),
            method_name="async_input_int_return_untyped_int",
            variables="value1: int = 3, value2: int = 3",
            returns="int = 6",
            working_directory=mocks_async_working_directory(),
            is_async=True,
        )

    @freeze_time(FREEZE_TIME)
    @pytest.mark.asyncio
    async def test_debug_function_async_input_int_return_untyped_str(self, caplog):
        # result = await record_task
        f = mocks_async_module_name()
        with caplog.at_level(level=logging.DEBUG, logger=mocks_async_module_name()):
            _ = await async_input_int_return_untyped_str(3, 3)

        assert_debug_test(
            caplog=caplog,
            module_name=mocks_async_module_name(),
            method_name="async_input_int_return_untyped_str",
            variables="value1: int = 3, value2: int = 3",
            returns=f"str = total return value",
            working_directory=mocks_async_working_directory(),
            is_async=True,
        )
