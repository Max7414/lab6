"""Core logic for the CI lab sample project."""


def add_numbers(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def format_message(name: str) -> str:
    """Return a friendly message, used to demonstrate lint/test steps."""
    cleaned = name.strip()
    if not cleaned:
        raise ValueError("name must not be empty")
    return f"Hello from both collaborators, {cleaned}!"



def format_message_summary(name: str) -> str:
    """Return a short summary used for logging."""
    cleaned = name.strip() or "<unknown>"
    return f"Greeting prepared for {cleaned}"
