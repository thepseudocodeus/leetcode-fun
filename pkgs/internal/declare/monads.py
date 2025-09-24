"""
Monadic patterns for functional composition and error handling.

This module implements common monadic patterns like Maybe and Either,
providing a functional approach to handling optional values and computations
that may fail.
"""

from typing import TypeVar, Generic, Callable, Any, Optional
from abc import ABC, abstractmethod
from .results import Result, Ok, Err

T = TypeVar("T")
U = TypeVar("U")
E = TypeVar("E")


class Monad(Generic[T], ABC):
    """
    Abstract base class for monadic types.

    A monad is a design pattern that allows structuring programs generically
    while automating away boilerplate code needed by the program logic.
    """

    @abstractmethod
    def bind(self, func: Callable[[T], "Monad[U]"]) -> "Monad[U]":
        """Bind operation (>>=) - chains monadic computations."""
        pass

    @abstractmethod
    def unit(self, value: U) -> "Monad[U]":
        """Unit operation (return) - lifts a value into the monad."""
        pass

    def __rshift__(self, func: Callable[[T], "Monad[U]"]) -> "Monad[U]":
        """Operator overload for bind (>>)."""
        return self.bind(func)


class Maybe(Monad[T]):
    """
    Maybe monad for handling optional values.

    Represents values that may or may not be present, avoiding None/NoneType errors
    and providing a clean way to chain operations on optional values.
    """

    def __init__(self, value: Optional[T] = None):
        self._value = value

    @property
    def is_just(self) -> bool:
        """Check if the Maybe contains a value."""
        return self._value is not None

    @property
    def is_nothing(self) -> bool:
        """Check if the Maybe is empty."""
        return self._value is None

    def bind(self, func: Callable[[T], "Maybe[U]"]) -> "Maybe[U]":
        """Apply function to contained value if present."""
        if self.is_just:
            return func(self._value)
        return Maybe[U]()

    def unit(self, value: U) -> "Maybe[U]":
        """Lift a value into Maybe."""
        return Maybe[U](value)

    def unwrap(self) -> T:
        """Extract the value, raising ValueError if Nothing."""
        if self.is_just:
            return self._value
        raise ValueError("Called unwrap on Nothing")

    def unwrap_or(self, default: T) -> T:
        """Extract value or return default."""
        return self._value if self.is_just else default

    def unwrap_or_else(self, func: Callable[[], T]) -> T:
        """Extract value or compute default."""
        return self._value if self.is_just else func()

    def map(self, func: Callable[[T], U]) -> "Maybe[U]":
        """Apply function to contained value if present."""
        if self.is_just:
            return Maybe[U](func(self._value))
        return Maybe[U]()

    def filter(self, predicate: Callable[[T], bool]) -> "Maybe[T]":
        """Keep value only if it satisfies the predicate."""
        if self.is_just and predicate(self._value):
            return self
        return Maybe[T]()

    def to_result(self, error: E) -> Result[T, E]:
        """Convert Maybe to Result, using error for Nothing."""
        if self.is_just:
            return Ok(self._value)
        return Err(error)

    def __str__(self) -> str:
        return f"Just({self._value})" if self.is_just else "Nothing"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Maybe):
            return False
        return self._value == other._value


class Either(Monad[T]):
    """
    Either monad for handling computations that may fail.

    Represents values that can be either Left (error/failure) or Right (success),
    providing a clean way to handle error cases without exceptions.
    """

    def __init__(self, value: T, is_right: bool = True):
        self._value = value
        self._is_right = is_right

    @property
    def is_right(self) -> bool:
        """Check if this is a Right (success) value."""
        return self._is_right

    @property
    def is_left(self) -> bool:
        """Check if this is a Left (error) value."""
        return not self._is_right

    def bind(self, func: Callable[[T], "Either[U]"]) -> "Either[U]":
        """Apply function if Right, propagate Left unchanged."""
        if self.is_right:
            return func(self._value)
        return Either[U](self._value, False)

    def unit(self, value: U) -> "Either[U]":
        """Lift a value into Either as Right."""
        return Either[U](value, True)

    def unwrap(self) -> T:
        """Extract value from Right, raise ValueError if Left."""
        if self.is_right:
            return self._value
        raise ValueError(f"Called unwrap on Left: {self._value}")

    def unwrap_or(self, default: T) -> T:
        """Extract value from Right or return default."""
        return self._value if self.is_right else default

    def unwrap_or_else(self, func: Callable[[T], T]) -> T:
        """Extract value from Right or compute from Left."""
        return self._value if self.is_right else func(self._value)

    def map(self, func: Callable[[T], U]) -> "Either[U]":
        """Apply function to Right value, leave Left unchanged."""
        if self.is_right:
            return Either[U](func(self._value), True)
        return Either[U](self._value, False)

    def map_left(self, func: Callable[[T], U]) -> "Either[U]":
        """Apply function to Left value, leave Right unchanged."""
        if self.is_left:
            return Either[U](func(self._value), False)
        return Either[U](self._value, True)

    def to_result(self) -> Result[T, T]:
        """Convert Either to Result."""
        if self.is_right:
            return Ok(self._value)
        return Err(self._value)

    @classmethod
    def right(cls, value: T) -> "Either[T]":
        """Create a Right (success) value."""
        return cls(value, True)

    @classmethod
    def left(cls, value: T) -> "Either[T]":
        """Create a Left (error) value."""
        return cls(value, False)

    def __str__(self) -> str:
        side = "Right" if self.is_right else "Left"
        return f"{side}({self._value})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Either):
            return False
        return self._value == other._value and self._is_right == other._is_right


# Utility functions for creating monadic values
def Just(value: T) -> Maybe[T]:
    """Create a Maybe with a value."""
    return Maybe[T](value)


def Nothing() -> Maybe[T]:
    """Create an empty Maybe."""
    return Maybe[T]()


def Right(value: T) -> Either[T]:
    """Create an Either with a Right (success) value."""
    return Either.right(value)


def Left(value: T) -> Either[T]:
    """Create an Either with a Left (error) value."""
    return Either.left(value)
