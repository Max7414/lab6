from datetime import datetime

from app.logging_utils import build_audit_message


def test_build_audit_message_defaults_to_utcnow(monkeypatch):
    fixed = datetime(2024, 1, 2, 3, 4, 5)

    class DummyDatetime:
        @staticmethod
        def utcnow():
            return fixed

    monkeypatch.setattr("app.logging_utils.datetime", DummyDatetime)
    message = build_audit_message("Alice", "updated CI pipeline")
    assert message == "[2024-01-02T03:04:05Z] Alice: updated CI pipeline"


def test_build_audit_message_fills_blanks():
    fixed = datetime(2024, 5, 6, 7, 8, 9)
    message = build_audit_message("  ", "  ", timestamp=fixed)
    assert message == "[2024-05-06T07:08:09Z] <unknown>: <no-action>"
