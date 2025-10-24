import pytest

from app import add_numbers, format_message


def test_add_numbers():
    assert add_numbers(2, 3) == 5


def test_format_message_strips_whitespace():
    assert format_message("  Alice  ") == "Hello from both collaborators, Alice!"


def test_format_message_rejects_empty():
    with pytest.raises(ValueError):
        format_message("   ")
