# import numpy as np
# calculator.py

class Calculator:
    """A simple calculator class that does operations on two numbers."""

    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the difference of a and b."""
        return a - b

    def multiply(self, a, b):
        """Return the product of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the division of a by b.
        
        Raises:
            ValueError: If b is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    # def add_lists(self, a, b):
    #     """Return the sum of a and b."""
    #     return np.array(a) + np.array(b)
