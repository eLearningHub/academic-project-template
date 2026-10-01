"""A sample module, to show how code, tests and docs fit together."""


class SampleClass:
    """A sample class with one class method."""

    def __init__(self):
        """Give the instance a name."""
        self.name = "sample class"

    @classmethod
    def sample_sum(cls, x: int, y: int) -> int:
        """
        Calculate the sum of two numbers

        :param x: int: first number
        :param y: int: second number

        :return: int: sum of x and y
        :rtype: int
        """
        return x + y
