class Calculator:
    @staticmethod
    def _require_nonzero(b, op):
        if b == 0:
            raise ValueError(f"Cannot {op} by zero")

    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        self._require_nonzero(b, "divide")
        return a / b
    def modulo(self, a, b):
        self._require_nonzero(b, "modulo")
        return a % b
    def power(self, a, b):
        return a ** b
