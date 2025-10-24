"""Utilities for producing audit-friendly log messages."""

from datetime import datetime


def build_audit_message(
    actor: str, action: str, *, timestamp: datetime | None = None
) -> str:
    """Compose a structured audit log message.

    Parameters
    ----------
    actor: name performing the action
    action: description of the change
    timestamp: optional datetime for reproducibility; defaults to utcnow
    """
    stamp = (timestamp or datetime.utcnow()).strftime("%Y-%m-%dT%H:%M:%SZ")
    actor_clean = actor.strip() or "<unknown>"
    action_clean = action.strip() or "<no-action>"
    return f"[{stamp}] {actor_clean}: {action_clean}"
