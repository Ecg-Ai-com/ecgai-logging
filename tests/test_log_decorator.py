from pathlib import Path

from fluentcheck import Is

from tests.mocks import mocks_module_name, mocks_working_directory


def remove_spaces_from_caplog(caplog):
    log_text = caplog.text.replace(" ", "")
    return log_text


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
