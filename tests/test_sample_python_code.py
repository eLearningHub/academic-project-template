import pytest

from src.pixi_project.sample_python_code import SampleClass


@pytest.fixture()
def sample_class():
    return SampleClass()


def test_sum_test_success(sample_class: SampleClass) -> None:
    input_x = 2
    input_y = 3
    expected_output = 5

    assert sample_class.sample_sum(input_x, input_y) == expected_output
