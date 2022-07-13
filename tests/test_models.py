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

@pytest.mark.parametrize(
    "test, expected, expect_rises",
    [
        (np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]], None),
        (np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), [[0, 0, 0], [0, 0, 0], [0, 0, 0]], None),
        (np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]]), [[1, 1, 1], [1, 1, 1], [1, 1, 1]], None),
        (np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]], None),
        (np.array([[np.inf, np.inf], [np.inf, np.inf], [np.inf, np.inf]]), [[0, 0], [0, 0], [0, 0]], None),
        (np.array([[1, 2, 3], [4, float('nan'), 6], [7, 8, 9]]), [[0.33, 0.67, 1], [0.66, 0, 1], [0.78, 0.89, 1]], None),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[0.33, 0.67, 1], [0.66, 0.83, 1], [0.88, 1, 0]], TypeError),
        (np.array([[1, 2, 3], [4, 5, 6], [7, 8, -9]]), [[0.33, 0.67, 1], [0.66, 0.83, 1], [0.88, 1, 0]], ValueError),
        (np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]), [[0.33, 0.67, 1], [0.66, 0.83, 1], [0.78, 1, 0]], ValueError),

    ])
def test_patient_normalize(test, expected, expect_rises):
    """Test normalization works for arrays of one and positive integers.
    Assumption that test accuracy of two decimal places is sufficient."""
    from inflammation.models import patient_normalize
    if expect_rises is not None:
        with pytest.raises(expect_rises):
            npt.assert_almost_equal(patient_normalize(test), np.array(expected), decimal=2)
    else:
        npt.assert_almost_equal(patient_normalize(test), np.array(expected), decimal=2)

@pytest.mark.parametrize(
    "data, names, expected",
    [
        ([[1,2,3],[2,2,5]], ['Alice','Bob'], [{'name':'Alice', 'data':[1,2,3]}, {'name':'Bob', 'data':[2,2,5]}]),
        (np.array([[1,2,3],[2,2,5]]), ['Alice','Bob'], [{'name':'Alice', 'data':[1,2,3]}, {'name':'Bob', 'data':[2,2,5]}])
    ]
)
def test_attach_names(data, names, expected):
    """Test that assigning names to inflammation data works."""
    from inflammation.models import attach_names
    patients = attach_names(data,names)
    # Result must be exactly equal
    npt.assert_equal(patients, expected)
