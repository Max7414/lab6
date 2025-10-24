"""Simple package used by CI merge experiments."""

from .main import (
    add_numbers,
    format_excited_message,
    format_message,
    format_message_summary,
)
from .logging_utils import build_audit_message

__all__ = [
    "add_numbers",
    "format_message",
    "format_excited_message",
    "format_message_summary",
    "build_audit_message",
]
