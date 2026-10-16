from calculator.engines.base import MathEngine
from calculator.engines.native import NativeEngine


class Operations:
    """Stable interface for calculator operations."""

    def __init__(self, engine: MathEngine | None = None):
        self.engine = engine or NativeEngine()

    def add(self, a: float, b: float) -> float:
        return self.engine.add(a, b)

    def subtract(self, a: float, b: float) -> float:
        return self.engine.subtract(a, b)

    def multiply(self, a: float, b: float) -> float:
        return self.engine.multiply(a, b)

    def divide(self, a: float, b: float) -> float:
        return self.engine.divide(a, b)