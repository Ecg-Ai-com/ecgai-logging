import logging
from datetime import timezone

from freezegun import freeze_time

from tests.mocks import (
    mocks_module_name,
    input_int_return_none,
    input_int_return_typed_int,
    input_int_return_untyped_int,
    input_int_return_typed_str,
    input_int_return_untyped_str,
    MockClass,
    input_int_return_none_call_sub_function,
    input_int_return_typed_int_call_sub_function,
    mocks_working_directory,
)
# @pytest.fixture
# def root_logger():
from tests.test_log_decorator import assert_debug_test, FREEZE_TIME


# logger = logging.getLogger(mocks_module_name())
# handler = colorlog.StreamHandler(sys.stdout)
# handler.setFormatter(
#     colorlog.ColoredFormatter("%(log_color)s%(levelname)s:%(name)s:%(message)s")
# )
#
# logger.addHandler(handler)

class TestDebugFunctionLogDecorator:
    @freeze_time(FREEZE_TIME)
    def test_debug_function_input_int_return_none(self, caplog):
        with caplog.at_level(level=logging.DEBUG, logger=mocks_module_name()):
            input_int_return_none(3, 3)
        assert_debug_test(
            caplog=caplog,
            module_name=mocks_module_name(),
            method_name="input_int_return_none",
            variables="value1: int = 3, value2: int = 3",
            returns="NoneType = None",
            working_directory=mocks_working_directory(),
            is_async=False,
        )

    @freeze_time(FREEZE_TIME)
    def test_debug_function_input_int_return_typed_int(self, caplog):
        with caplog.at_level(level=logging.DEBUG, logger=mocks_module_name()):
            input_int_return_typed_int(3, 3)
        assert_debug_test(
            caplog=caplog,
            module_name=mocks_module_name(),
            method_name="input_int_return_typed_int",
            variables="value1: int = 3, value2: int = 3",
            returns="int = 6",
            working_directory=mocks_working_directory(),
            is_async=False,
        )

    @freeze_time(FREEZE_TIME)
    def test_debug_function_input_int_return_untyped_int(self, caplog):
        with caplog.at_level(level=logging.DEBUG, logger=mocks_module_name()):
            input_int_return_untyped_int(3, 3)
        assert_debug_test(
            caplog=caplog,
            module_name=mocks_module_name(),
            method_name="input_int_return_untyped_int",
            variables="value1: int = 3, value2: int = 3",
            returns="int = 6",
            working_directory=mocks_working_directory(),
            is_async=False,
        )

    @freeze_time(FREEZE_TIME)
    def test_debug_function_input_int_return_typed_str(self, caplog):
        with caplog.at_level(level=logging.DEBUG, logger=mocks_module_name()):
            input_int_return_typed_str(3, 3)
        assert_debug_test(
            caplog=caplog,
            module_name=mocks_module_name(),
            method_name=f"input_int_return_typed_str",
            variables=f"value1: int = 3, value2: int = 3",
            returns=f"str = total return value",
            working_directory=mocks_working_directory(),
            is_async=False,
        )

    @freeze_time(FREEZE_TIME)
    def test_debug_function_input_int_return_untyped_str(self, caplog):
        with caplog.at_level(level=logging.DEBUG, logger=mocks_module_name()):
            input_int_return_untyped_str(3, 3)
        assert_debug_test(
            caplog=caplog,
            module_name=mocks_module_name(),
            method_name=f"input_int_return_untyped_str",
            variables=f"value1: int = 3, value2: int = 3",
            returns=f"str = total return value",
            working_directory=mocks_working_directory(),
            is_async=False,
        )

    @freeze_time(FREEZE_TIME)
    def test_debug_function_call_sub_function__input_int_return_none(self, caplog):
        with caplog.at_level(level=logging.DEBUG, logger=mocks_module_name()):
            input_int_return_none_call_sub_function(3, 3)
        assert_debug_test(
            caplog=caplog,
            module_name=mocks_module_name(),
            method_name="input_int_return_none",
            variables="value1: int = 3, value2: int = 3",
            returns="NoneType = None",
            working_directory=mocks_working_directory(),
            is_async=False,
        )
        assert_debug_test(
            caplog=caplog,
            module_name=mocks_module_name(),
            method_name="input_int_return_none_call_sub_function",
            variables="value1: int = 3, value2: int = 3",
            returns="NoneType = None",
            working_directory=mocks_working_directory(),
            is_async=False,
        )

    @freeze_time(FREEZE_TIME)
    def test_debug_function_call_sub_function_input_int_return_typed_int(self, caplog):
        with caplog.at_level(level=logging.DEBUG, logger=mocks_module_name()):
            input_int_return_typed_int_call_sub_function(3, 3)
        assert_debug_test(
            caplog=caplog,
            module_name=mocks_module_name(),
            method_name="input_int_return_typed_int_call_sub_function",
            variables="value1: int = 3, value2: int = 3",
            returns="int = 6",
            working_directory=mocks_working_directory(),
            is_async=False,
        )
        assert_debug_test(
            caplog=caplog,
            module_name=mocks_module_name(),
            method_name="input_int_return_typed_int",
            variables="value1: int = 3, value2: int = 3",
            returns="int = 6",
            working_directory=mocks_working_directory(),
            is_async=False,
        )


class TestDebugClassLogDecorator:
    @freeze_time(FREEZE_TIME)
    def test_debug_class_input_int_return_none(self, caplog):
        with caplog.at_level(level=logging.DEBUG, logger=mocks_module_name()):
            mock = MockClass()
            mock.input_int_return_none(3, 3)
        assert_debug_test(
            caplog=caplog,
            module_name=mocks_module_name(),
            method_name="MockClass.input_int_return_none",
            variables="value1: int = 3, value2: int = 3",
            returns="NoneType = None",
            working_directory=mocks_working_directory(),
            is_async=False,
        )

    @freeze_time(FREEZE_TIME)
    def test_debug_class_input_int_return_typed_int(self, caplog):
        with caplog.at_level(level=logging.DEBUG, logger=mocks_module_name()):
            mock = MockClass()
            mock.input_int_return_typed_int(3, 3)
        assert_debug_test(
            caplog=caplog,
            module_name=mocks_module_name(),
            method_name="MockClass.input_int_return_typed_int",
            variables="value1: int = 3, value2: int = 3",
            returns="int = 6",
            working_directory=mocks_working_directory(),
            is_async=False,
        )

    @freeze_time(FREEZE_TIME)
    def test_debug_class_input_int_return_untyped_int(self, caplog):
        with caplog.at_level(level=logging.DEBUG, logger=mocks_module_name()):
            mock = MockClass()
            mock.input_int_return_untyped_int(3, 3)
        assert_debug_test(
            caplog=caplog,
            module_name=mocks_module_name(),
            method_name="MockClass.input_int_return_untyped_int",
            variables="value1: int = 3, value2: int = 3",
            returns="int = 6",
            working_directory=mocks_working_directory(),
            is_async=False,
        )

    @freeze_time(FREEZE_TIME)
    def test_debug_class_input_int_return_typed_str(self, caplog):
        with caplog.at_level(level=logging.DEBUG, logger=mocks_module_name()):
            mock = MockClass()
            mock.input_int_return_typed_str(3, 3)
        assert_debug_test(
            caplog=caplog,
            module_name=mocks_module_name(),
            method_name=f"MockClass.input_int_return_typed_str",
            variables=f"value1: int = 3, value2: int = 3",
            returns=f"str = total return value",
            working_directory=mocks_working_directory(),
            is_async=False,
        )

    @freeze_time(FREEZE_TIME)
    def test_debug_class_input_int_return_untyped_str(self, caplog):
        with caplog.at_level(level=logging.DEBUG, logger=mocks_module_name()):
            mock = MockClass()
            mock.input_int_return_untyped_str(3, 3)
        assert_debug_test(
            caplog=caplog,
            module_name=mocks_module_name(),
            method_name=f"MockClass.input_int_return_untyped_str",
            variables=f"value1: int = 3, value2: int = 3",
            returns=f"str = total return value",
            working_directory=mocks_working_directory(),
            is_async=False,
        )

    @freeze_time(FREEZE_TIME)
    def test_input_int_return_untyped_tuple_str_and_int(self, caplog):
        with caplog.at_level(level=logging.DEBUG, logger=mocks_module_name()):
            mock = MockClass()
            mock.input_int_return_untyped_tuple_str_and_int(3, 3)
        assert_debug_test(
            caplog=caplog,
            module_name=mocks_module_name(),
            method_name=f"MockClass.input_int_return_untyped_tuple_str_and_int",
            variables=f"value1: int = 3, value2: int = 3",
            returns=f"tuple[str = total return value, int = 6]",
            working_directory=mocks_working_directory(),
            is_async=False,
        )

    @freeze_time(FREEZE_TIME)
    def test_debug_function_call_sub_function__input_int_return_none(self, caplog):
        with caplog.at_level(level=logging.DEBUG, logger=mocks_module_name()):
            mock = MockClass()
            mock.input_int_return_none_call_sub_function(3, 3)
        assert_debug_test(
            caplog=caplog,
            module_name=mocks_module_name(),
            method_name="MockClass.input_int_return_none",
            variables="value1: int = 3, value2: int = 3",
            returns="NoneType = None",
            working_directory=mocks_working_directory(),
            is_async=False,
        )
        assert_debug_test(
            caplog=caplog,
            module_name=mocks_module_name(),
            method_name="MockClass.input_int_return_none_call_sub_function",
            variables="value1: int = 3, value2: int = 3",
            returns="NoneType = None",
            working_directory=mocks_working_directory(),
            is_async=False,
        )

    @freeze_time(FREEZE_TIME)
    def test_debug_function_call_sub_function_input_int_return_typed_int(self, caplog):
        with caplog.at_level(level=logging.DEBUG, logger=mocks_module_name()):
            mock = MockClass()
            mock.input_int_return_typed_int_call_sub_function(3, 3)
        assert_debug_test(
            caplog=caplog,
            module_name=mocks_module_name(),
            method_name="MockClass.input_int_return_typed_int_call_sub_function",
            variables="value1: int = 3, value2: int = 3",
            returns="int = 6",
            working_directory=mocks_working_directory(),
            is_async=False,
        )
        assert_debug_test(
            caplog=caplog,
            module_name=mocks_module_name(),
            method_name="MockClass.input_int_return_typed_int",
            variables="value1: int = 3, value2: int = 3",
            returns="int = 6",
            working_directory=mocks_working_directory(),
            is_async=False,
        )
