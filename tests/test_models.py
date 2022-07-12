"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3, 4], [5, 6]], [3, 4]),
        ([[2, 7], [4, 3], [9, 2]], [5, 4])
    ]
)
def test_daily_mean(test, expected):
    """Test that mean function works for an array of integers, zero included."""
    from inflammation.models import daily_mean

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_mean(test), expected)


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3, 4], [5, 6]], [5, 6]),
        ([[3, 4], [8, 4], [1, 7]], [8, 7])
    ]
)
def test_daily_max_zeros(test, expected):
    """Test that max function works for an array of zeroes."""
    from inflammation.models import daily_max

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_max(test), expected)


@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3, 4], [5, 6]], [1, 2]),
        ([[0, 9], [3, 1], [18, 6]], [0, 1])
    ]
)
def test_daily_min_zeros(test, expected):
    """Test that min function works for an array of zeroes."""
    from inflammation.models import daily_min

    # Need to use Numpy testing functions to compare arrays
    npt.assert_array_equal(daily_min(test), expected)


def test_daily_min_string():
    """Test for TypeError when passing strings"""
    from inflammation.models import daily_min

    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello', 'there'], ['General', 'Kenobi']])
