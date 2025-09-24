"""
Adapter layer implementation for extensible architecture.

This module provides a registry-based adapter system that allows easy
modification and extension of functionality without refactoring existing code.
The adapter pattern enables polyglot support and cross-platform compatibility.
"""

from typing import TypeVar, Generic, Dict, Any, Optional, Callable, Type
from abc import ABC, abstractmethod
from dataclasses import dataclass
from .results import Result, Ok, Err
from .monads import Maybe

T = TypeVar("T")
R = TypeVar("R")


@dataclass
class AdapterConfig:
    """Configuration for adapter instances."""

    name: str
    version: str
    platform: str
    config: Dict[str, Any]


class AdapterInterface(ABC, Generic[T, R]):
    """
    Abstract base class for all adapters.

    Adapters provide a consistent interface for different implementations
    of the same functionality, enabling easy swapping and extension.
    """

    @abstractmethod
    def can_handle(self, input_data: T) -> bool:
        """Check if this adapter can handle the given input."""
        pass

    @abstractmethod
    def process(self, input_data: T) -> Result[R, str]:
        """Process the input data and return a result."""
        pass

    @abstractmethod
    def get_config(self) -> AdapterConfig:
        """Get the adapter configuration."""
        pass

    @abstractmethod
    def validate_config(self) -> Result[bool, str]:
        """Validate the adapter configuration."""
        pass


class AdapterRegistry:
    """
    Registry for managing adapters with automatic selection and fallback.

    The registry maintains a collection of adapters and provides methods
    for registering, finding, and executing adapters based on input data
    and platform requirements.
    """

    def __init__(self):
        self._adapters: Dict[str, AdapterInterface] = {}
        self._priority_order: Dict[str, int] = {}
        self._platform_adapters: Dict[str, list] = {}

    def register(
        self, adapter: AdapterInterface[T, R], priority: int = 0
    ) -> Result[bool, str]:
        """
        Register an adapter in the registry.

        Args:
            adapter: The adapter to register
            priority: Priority for selection (higher = preferred)

        Returns:
            Result indicating success or failure
        """
        try:
            config = adapter.get_config()

            # Validate adapter configuration
            validation_result = adapter.validate_config()
            if validation_result.is_err():
                return Err(
                    f"Adapter validation failed: {validation_result.unwrap_err()}"
                )

            # Register the adapter
            self._adapters[config.name] = adapter
            self._priority_order[config.name] = priority

            # Register by platform
            if config.platform not in self._platform_adapters:
                self._platform_adapters[config.platform] = []
            self._platform_adapters[config.platform].append(config.name)

            return Ok(True)

        except Exception as e:
            return Err(f"Failed to register adapter: {str(e)}")

    def unregister(self, adapter_name: str) -> Result[bool, str]:
        """
        Unregister an adapter from the registry.

        Args:
            adapter_name: Name of the adapter to unregister

        Returns:
            Result indicating success or failure
        """
        if adapter_name not in self._adapters:
            return Err(f"Adapter '{adapter_name}' not found")

        try:
            adapter = self._adapters[adapter_name]
            config = adapter.get_config()

            # Remove from main registry
            del self._adapters[adapter_name]
            del self._priority_order[adapter_name]

            # Remove from platform registry
            if config.platform in self._platform_adapters:
                self._platform_adapters[config.platform].remove(adapter_name)
                if not self._platform_adapters[config.platform]:
                    del self._platform_adapters[config.platform]

            return Ok(True)

        except Exception as e:
            return Err(f"Failed to unregister adapter: {str(e)}")

    def find_adapter(
        self, input_data: T, platform: Optional[str] = None
    ) -> Maybe[AdapterInterface[T, R]]:
        """
        Find the best adapter for the given input data and platform.

        Args:
            input_data: The input data to process
            platform: Optional platform constraint

        Returns:
            Maybe containing the best adapter or Nothing
        """
        candidates = []

        # Filter adapters by platform if specified
        adapter_names = list(self._adapters.keys())
        if platform and platform in self._platform_adapters:
            adapter_names = self._platform_adapters[platform]

        # Find adapters that can handle the input
        for name in adapter_names:
            adapter = self._adapters[name]
            if adapter.can_handle(input_data):
                candidates.append((name, adapter, self._priority_order[name]))

        if not candidates:
            return Maybe[AdapterInterface[T, R]]()

        # Sort by priority (highest first)
        candidates.sort(key=lambda x: x[2], reverse=True)

        return Maybe[AdapterInterface[T, R]](candidates[0][1])

    def process_with_best_adapter(
        self, input_data: T, platform: Optional[str] = None
    ) -> Result[R, str]:
        """
        Process input data using the best available adapter.

        Args:
            input_data: The input data to process
            platform: Optional platform constraint

        Returns:
            Result containing the processed data or error
        """
        adapter_maybe = self.find_adapter(input_data, platform)

        if adapter_maybe.is_nothing:
            return Err("No suitable adapter found for the given input")

        adapter = adapter_maybe.unwrap()
        return adapter.process(input_data)

    def list_adapters(self) -> Dict[str, AdapterConfig]:
        """List all registered adapters with their configurations."""
        return {name: adapter.get_config() for name, adapter in self._adapters.items()}

    def get_adapter(self, name: str) -> Maybe[AdapterInterface[T, R]]:
        """Get a specific adapter by name."""
        if name in self._adapters:
            return Maybe[AdapterInterface[T, R]](self._adapters[name])
        return Maybe[AdapterInterface[T, R]]()

    def clear(self) -> None:
        """Clear all registered adapters."""
        self._adapters.clear()
        self._priority_order.clear()
        self._platform_adapters.clear()


class MonadicAdapter(AdapterInterface[T, R]):
    """
    Base class for monadic adapters that use Result types.

    This provides a convenient base for implementing adapters that
    follow the Result pattern for error handling.
    """

    def __init__(self, config: AdapterConfig):
        self._config = config

    def get_config(self) -> AdapterConfig:
        return self._config

    def validate_config(self) -> Result[bool, str]:
        """Default implementation validates required fields."""
        try:
            assert self._config.name, "Adapter name is required"
            assert self._config.version, "Adapter version is required"
            assert self._config.platform, "Adapter platform is required"
            return Ok(True)
        except AssertionError as e:
            return Err(str(e))
        except Exception as e:
            return Err(f"Configuration validation failed: {str(e)}")


class DataProcessingAdapter(MonadicAdapter[T, R]):
    """
    Specialized adapter for data processing operations.

    This adapter provides common functionality for processing
    large datasets with memory efficiency and progress tracking.
    """

    def __init__(self, config: AdapterConfig):
        super().__init__(config)
        self._progress_callback: Optional[Callable[[float], None]] = None

    def set_progress_callback(self, callback: Callable[[float], None]) -> None:
        """Set a progress callback for monitoring processing."""
        self._progress_callback = callback

    def _update_progress(self, progress: float) -> None:
        """Update progress if callback is set."""
        if self._progress_callback:
            self._progress_callback(progress)

    def can_handle(self, input_data: T) -> bool:
        """Default implementation checks data type and size."""
        # Override in subclasses for specific handling logic
        return True

    def process(self, input_data: T) -> Result[R, str]:
        """Process input data with progress tracking."""
        try:
            self._update_progress(0.0)
            result = self._process_data(input_data)
            self._update_progress(1.0)
            return result
        except Exception as e:
            return Err(f"Processing failed: {str(e)}")

    @abstractmethod
    def _process_data(self, input_data: T) -> Result[R, str]:
        """Override this method to implement specific processing logic."""
        pass


# Global adapter registry instance
_global_registry = AdapterRegistry()


def get_global_registry() -> AdapterRegistry:
    """Get the global adapter registry instance."""
    return _global_registry


def register_adapter(
    adapter: AdapterInterface[T, R], priority: int = 0
) -> Result[bool, str]:
    """Register an adapter in the global registry."""
    return _global_registry.register(adapter, priority)


def unregister_adapter(adapter_name: str) -> Result[bool, str]:
    """Unregister an adapter from the global registry."""
    return _global_registry.unregister(adapter_name)
