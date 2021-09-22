import asyncio
import logging
import sys

import colorlog
import pytest
from freezegun import freeze_time

from tests.mocks import mocks_module_name
from tests.mocks_async import (
    async_input_int_return_untyped_int,
    mocks_async_module_name, async_input_int_return_untyped_str,
)
from tests.test_log_decorator import remove_spaces_from_caplog

logger = logging.getLogger(mocks_async_module_name())
# logger.level = logging.DEBUG
# stream_handler = logging.StreamHandler(sys.stdout)
# logger.addHandler(stream_handler)
handler = colorlog.StreamHandler(sys.stdout)
handler.setFormatter(
    colorlog.ColoredFormatter("%(log_color)s%(levelname)s:%(name)s:%(message)s")
)

logger.addHandler(handler)

FREEZE_TIME = "2021-09-14 03:21:34"


def assert_debug_test(caplog, method_name, variables, returns):
    log_text = remove_spaces_from_caplog(caplog=caplog)
    assert mocks_module_name() in log_text
    assert f"Method name: {method_name}".replace(" ", "") in log_text
    assert f"Variables: {variables}".replace(" ", "") in log_text
    assert f"Returns: {returns}".replace(" ", "") in log_text
    assert "Start time: 2021-09-14 03:21:34".replace(" ", "") in log_text
    assert "End time: 2021-09-14 03:21:34".replace(" ", "") in log_text
    assert "Elapsed time: 0.0".replace(" ", "") in log_text


class TestDebugFunctionLogDecorator:
    @freeze_time(FREEZE_TIME)
    @pytest.mark.asyncio
    async def test_debug_function_async_input_int_return_untyped_int(self, caplog):
        # result = await record_task
        with caplog.at_level(level=logging.DEBUG, logger=mocks_async_module_name()):
            # a = await async_input_int_return_untyped_int(3, 3)
            task = asyncio.create_task(async_input_int_return_untyped_int(3, 3))
            result = await task
        assert_debug_test(
            caplog=caplog,
            method_name="async_input_int_return_untyped_int",
            variables="value1: int = 3, value2: int = 3",
            returns="int = 6",
        )

    @freeze_time(FREEZE_TIME)
    @pytest.mark.asyncio
    async def test_debug_function_async_input_int_return_untyped_str(self, caplog):
        # result = await record_task
        with caplog.at_level(level=logging.DEBUG, logger=mocks_async_module_name()):
            a = await async_input_int_return_untyped_str(3, 3)
            # task = asyncio.create_task(async_input_int_return_untyped_int(3, 3))
            # result = await task
        assert_debug_test(
            caplog=caplog,
            method_name="async_input_int_return_untyped_str",
            variables="value1: int = 3, value2: int = 3",
            returns=f"str = total return value",
        )
