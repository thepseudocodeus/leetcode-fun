"""
Results pattern implementation for robust error handling.

This module provides a Result type that represents either success (Ok) or failure (Err),
enabling explicit error handling without exceptions and promoting functional composition.
"""

from typing import TypeVar, Generic, Callable, Any, Optional
from dataclasses import dataclass
from functools import wraps

T = TypeVar("T")
E = TypeVar("E")
U = TypeVar("U")


@dataclass(frozen=True)
class Result(Generic[T, E]):
    """
    A Result type that represents either success (Ok) or failure (Err).

    This provides a functional approach to error handling, making it explicit
    and composable without relying on exceptions.
    """

    def is_ok(self) -> bool:
        """Check if the result is Ok."""
        return isinstance(self, Ok)

    def is_err(self) -> bool:
        """Check if the result is Err."""
        return isinstance(self, Err)

    def unwrap(self) -> T:
        """Unwrap the value, raising an exception if Err."""
        if self.is_ok():
            return self.value
        raise ValueError(f"Called unwrap on Err: {self.error}")

    def unwrap_or(self, default: T) -> T:
        """Unwrap the value or return default if Err."""
        return self.value if self.is_ok() else default

    def unwrap_or_else(self, op: Callable[[E], T]) -> T:
        """Unwrap the value or compute from error if Err."""
        return self.value if self.is_ok() else op(self.error)

    def map(self, op: Callable[[T], U]) -> "Result[U, E]":
        """Apply a function to the contained value if Ok."""
        if self.is_ok():
            return Ok(op(self.value))
        return Err(self.error)

    def map_err(self, op: Callable[[E], U]) -> "Result[T, U]":
        """Apply a function to the contained error if Err."""
        if self.is_err():
            return Err(op(self.error))
        return Ok(self.value)

    def and_then(self, op: Callable[[T], "Result[U, E]"]) -> "Result[U, E]":
        """Chain operations that return Results."""
        if self.is_ok():
            return op(self.value)
        return Err(self.error)

    def or_else(self, op: Callable[[E], "Result[T, U]"]) -> "Result[T, U]":
        """Chain operations on the error side."""
        if self.is_err():
            return op(self.error)
        return Ok(self.value)


@dataclass(frozen=True)
class Ok(Result[T, E]):
    """Represents a successful result containing a value."""

    value: T

    def __str__(self) -> str:
        return f"Ok({self.value})"


@dataclass(frozen=True)
class Err(Result[T, E]):
    """Represents an error result containing an error value."""

    error: E

    def __str__(self) -> str:
        return f"Err({self.error})"


def result_decorator(f: Callable[..., Result[T, E]]) -> Callable[..., Result[T, E]]:
    """
    Decorator to ensure functions return Result types.

    This decorator wraps functions to ensure they always return Result types,
    converting exceptions to Err results automatically.
    """

    @wraps(f)
    def wrapper(*args, **kwargs) -> Result[T, E]:
        try:
            result = f(*args, **kwargs)
            if not isinstance(result, Result):
                return Ok(result)
            return result
        except Exception as e:
            return Err(str(e))

    return wrapper


def assert_result(result: Result[T, E], error_message: str = "Assertion failed") -> T:
    """
    Assert that a Result is Ok and return its value.

    This function serves as both an assertion and a way to extract values
    from Results in contexts where we expect success.

    Args:
        result: The Result to check
        error_message: Custom error message if assertion fails

    Returns:
        The contained value if Ok

    Raises:
        AssertionError: If the Result is Err
    """
    if result.is_ok():
        return result.value
    raise AssertionError(f"{error_message}: {result.error}")


# Type aliases for common Result patterns
StringResult = Result[str, str]
IntResult = Result[int, str]
BoolResult = Result[bool, str]
ListResult = Result[list, str]
DictResult = Result[dict, str]
