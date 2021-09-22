import asyncio
from pathlib import Path

import pytest

from src.ecgai_logging.log_decorator import log


def mocks_async_module_name():
    return __name__


def mocks_async_working_directory():
    return Path.cwd()


@log
async def async_input_int_return_untyped_int(value1: int, value2: int) -> int:
    total = value1 + value2
    return total


@log
async def async_input_int_return_untyped_str(value1: int, value2: int):
    _ = value1 + value2
    return 'total return value'
