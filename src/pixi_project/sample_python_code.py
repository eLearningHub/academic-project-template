class SampleClass:
    def __init__(self):
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
