import logging
import sys
from pathlib import Path

from freezegun import freeze_time

import colorlog
import pytest
from fluentcheck import Is

from src.ecgai_logging.log_decorator import log
from tests.mocks import (
    mocks_module_name,
    input_int_return_none,
    input_int_return_typed_int,
    input_int_return_untyped_int,
    input_int_return_typed_str,
    input_int_return_untyped_str,
    MockClass, input_int_return_none_call_sub_function, input_int_return_typed_int_call_sub_function,
)

# @pytest.fixture
# def root_logger():
from tests.test_log_decorator import remove_spaces_from_caplog

logger = logging.getLogger(mocks_module_name())
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
    def test_debug_function_input_int_return_none(self, caplog):
        with caplog.at_level(level=logging.DEBUG, logger=mocks_module_name()):
            input_int_return_none(3, 3)
        assert_debug_test(
            caplog=caplog,
            method_name="input_int_return_none",
            variables="value1: int = 3, value2: int = 3",
            returns="NoneType = None",
        )

    @freeze_time(FREEZE_TIME)
    def test_debug_function_input_int_return_typed_int(self, caplog):
        with caplog.at_level(level=logging.DEBUG, logger=mocks_module_name()):
            input_int_return_typed_int(3, 3)
        assert_debug_test(
            caplog=caplog,
            method_name="input_int_return_typed_int",
            variables="value1: int = 3, value2: int = 3",
            returns="int = 6",
        )

    @freeze_time(FREEZE_TIME)
    def test_debug_function_input_int_return_untyped_int(self, caplog):
        with caplog.at_level(level=logging.DEBUG, logger=mocks_module_name()):
            input_int_return_untyped_int(3, 3)
        assert_debug_test(
            caplog=caplog,
            method_name="input_int_return_untyped_int",
            variables="value1: int = 3, value2: int = 3",
            returns="int = 6",
        )

    @freeze_time(FREEZE_TIME)
    def test_debug_function_input_int_return_typed_str(self, caplog):
        with caplog.at_level(level=logging.DEBUG, logger=mocks_module_name()):
            input_int_return_typed_str(3, 3)
        assert_debug_test(
            caplog=caplog,
            method_name=f"input_int_return_typed_str",
            variables=f"value1: int = 3, value2: int = 3",
            returns=f"str = total return value",
        )

    @freeze_time(FREEZE_TIME)
    def test_debug_function_input_int_return_untyped_str(self, caplog):
        with caplog.at_level(level=logging.DEBUG, logger=mocks_module_name()):
            input_int_return_untyped_str(3, 3)
        assert_debug_test(
            caplog=caplog,
            method_name=f"input_int_return_untyped_str",
            variables=f"value1: int = 3, value2: int = 3",
            returns=f"str = total return value",
        )

    @freeze_time(FREEZE_TIME)
    def test_debug_function_call_sub_function__input_int_return_none(self, caplog):
        with caplog.at_level(level=logging.DEBUG, logger=mocks_module_name()):
            input_int_return_none_call_sub_function(3, 3)
        assert_debug_test(
            caplog=caplog,
            method_name="input_int_return_none",
            variables="value1: int = 3, value2: int = 3",
            returns="NoneType = None",
        )
        assert_debug_test(
            caplog=caplog,
            method_name="input_int_return_none_call_sub_function",
            variables="value1: int = 3, value2: int = 3",
            returns="NoneType = None",
        )

    @freeze_time(FREEZE_TIME)
    def test_debug_function_call_sub_function_input_int_return_typed_int(self, caplog):
        with caplog.at_level(level=logging.DEBUG, logger=mocks_module_name()):
            input_int_return_typed_int_call_sub_function(3, 3)
        assert_debug_test(
            caplog=caplog,
            method_name="input_int_return_typed_int_call_sub_function",
            variables="value1: int = 3, value2: int = 3",
            returns="int = 6",
        )
        assert_debug_test(
            caplog=caplog,
            method_name="input_int_return_typed_int",
            variables="value1: int = 3, value2: int = 3",
            returns="int = 6",
        )


class TestDebugClassLogDecorator:
    @freeze_time(FREEZE_TIME)
    def test_debug_class_input_int_return_none(self, caplog):
        with caplog.at_level(level=logging.DEBUG, logger=mocks_module_name()):
            mock = MockClass()
            mock.input_int_return_none(3, 3)
        assert_debug_test(
            caplog=caplog,
            method_name="MockClass.input_int_return_none",
            variables="value1: int = 3, value2: int = 3",
            returns="NoneType = None",
        )

    @freeze_time(FREEZE_TIME)
    def test_debug_class_input_int_return_typed_int(self, caplog):
        with caplog.at_level(level=logging.DEBUG, logger=mocks_module_name()):
            mock = MockClass()
            mock.input_int_return_typed_int(3, 3)
        assert_debug_test(
            caplog=caplog,
            method_name="MockClass.input_int_return_typed_int",
            variables="value1: int = 3, value2: int = 3",
            returns="int = 6",
        )

    @freeze_time(FREEZE_TIME)
    def test_debug_class_input_int_return_untyped_int(self, caplog):
        with caplog.at_level(level=logging.DEBUG, logger=mocks_module_name()):
            mock = MockClass()
            mock.input_int_return_untyped_int(3, 3)
        assert_debug_test(
            caplog=caplog,
            method_name="MockClass.input_int_return_untyped_int",
            variables="value1: int = 3, value2: int = 3",
            returns="int = 6",
        )

    @freeze_time(FREEZE_TIME)
    def test_debug_class_input_int_return_typed_str(self, caplog):
        with caplog.at_level(level=logging.DEBUG, logger=mocks_module_name()):
            mock = MockClass()
            mock.input_int_return_typed_str(3, 3)
        assert_debug_test(
            caplog=caplog,
            method_name=f"MockClass.input_int_return_typed_str",
            variables=f"value1: int = 3, value2: int = 3",
            returns=f"str = total return value",
        )

    @freeze_time(FREEZE_TIME)
    def test_debug_class_input_int_return_untyped_str(self, caplog):
        with caplog.at_level(level=logging.DEBUG, logger=mocks_module_name()):
            mock = MockClass()
            mock.input_int_return_untyped_str(3, 3)
        assert_debug_test(
            caplog=caplog,
            method_name=f"MockClass.input_int_return_untyped_str",
            variables=f"value1: int = 3, value2: int = 3",
            returns=f"str = total return value",
        )

    @freeze_time(FREEZE_TIME)
    def test_debug_function_call_sub_function__input_int_return_none(self, caplog):
        with caplog.at_level(level=logging.DEBUG, logger=mocks_module_name()):
            mock = MockClass()
            mock.input_int_return_none_call_sub_function(3, 3)
        assert_debug_test(
            caplog=caplog,
            method_name="MockClass.input_int_return_none",
            variables="value1: int = 3, value2: int = 3",
            returns="NoneType = None",
        )
        assert_debug_test(
            caplog=caplog,
            method_name="MockClass.input_int_return_none_call_sub_function",
            variables="value1: int = 3, value2: int = 3",
            returns="NoneType = None",
        )

    @freeze_time(FREEZE_TIME)
    def test_debug_function_call_sub_function_input_int_return_typed_int(self, caplog):
        with caplog.at_level(level=logging.DEBUG, logger=mocks_module_name()):
            mock = MockClass()
            mock.input_int_return_typed_int_call_sub_function(3, 3)
        assert_debug_test(
            caplog=caplog,
            method_name="MockClass.input_int_return_typed_int_call_sub_function",
            variables="value1: int = 3, value2: int = 3",
            returns="int = 6",
        )
        assert_debug_test(
            caplog=caplog,
            method_name="MockClass.input_int_return_typed_int",
            variables="value1: int = 3, value2: int = 3",
            returns="int = 6",
        )
