from pathlib import Path

from fluentcheck import Is

from tests.mocks import mocks_module_name, mocks_working_directory

FREEZE_TIME = "2021-09-14 03:21:34"


def remove_spaces_from_caplog(caplog):
    log_text = caplog.text.replace(" ", "")
    return log_text


def assert_debug_test(caplog, module_name, method_name, variables, returns, working_directory, is_async):
    log_text = remove_spaces_from_caplog(caplog=caplog)
    assert_info_test(
        caplog=caplog,
        module_name=module_name,
        method_name=method_name,
        variables=variables,
        returns=returns,
    )
    if is_async:
        assert f'Method type:           asynchronous)'
    else:
        assert f'Method type:           synchronous)'

    assert f"Working directory:     {working_directory}"
    assert "Start time: 2021-09-14 03:21:34".replace(" ", "") in log_text
    assert "End time: 2021-09-14 03:21:34".replace(" ", "") in log_text
    assert "Elapsed time: 0.0".replace(" ", "") in log_text


def assert_info_test(caplog, module_name, method_name, variables, returns):
    log_text = remove_spaces_from_caplog(caplog=caplog)
    assert module_name in log_text
    assert f"Method name: {method_name}".replace(" ", "") in log_text
    assert f"Variables: {variables}".replace(" ", "") in log_text
    assert f"Returns: {returns}".replace(" ", "") in log_text
    assert "Elapsed time: 0.0".replace(" ", "") in log_text


def test_mock_module_name():
    actual_name = mocks_module_name()
    Is(actual_name).matches("tests.mocks")


def test_mocks_working_directory():
    actual_path = mocks_working_directory()
    expected_path = Path.cwd()
    assert actual_path == expected_path


def test_mocks_working_directory_not_matching():
    actual_path = mocks_working_directory()
    expected_path = Path.joinpath(Path.cwd(), "test")
    assert actual_path != expected_path
