import numpy as np
from hypothesis import given, strategies as st
from mrmustard import *
from mrmustard.plugins import gaussian as gp


def test_partition_means():
    A, B = gp.partition_means(gp.backend.astensor(np.array([1, 2, 3, 4, 5, 6])), Amodes=[0, 2])
    assert np.allclose(A, [1, 3, 4, 6])
    assert np.allclose(B, [2, 5])

    A, B = gp.partition_means(gp.backend.astensor(np.array([1, 2, 3, 4, 5, 6])), Amodes=[0])
    assert np.allclose(A, [1, 4])
    assert np.allclose(B, [2, 3, 5, 6])

    A, B = gp.partition_means(gp.backend.astensor(np.array([1, 2, 3, 4, 5, 6])), Amodes=[1])
    assert np.allclose(A, [2, 5])
    assert np.allclose(B, [1, 3, 4, 6])


def test_partition_cov_2modes():
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
    A, B, AB = gp.partition_cov(gp.backend.astensor(arr), Amodes=[0, 1])
    assert np.allclose(A, arr)
    assert np.allclose(B, [])
    assert np.allclose(AB, [])

    A, B, AB = gp.partition_cov(gp.backend.astensor(arr), Amodes=[0])
    assert np.allclose(A, [[1, 3], [9, 11]])
    assert np.allclose(B, [[6, 8], [14, 16]])
    assert np.allclose(AB, [[2, 4], [10, 12]])

    A, B, AB = gp.partition_cov(gp.backend.astensor(arr), Amodes=[1])
    assert np.allclose(A, [[6, 8], [14, 16]])
    assert np.allclose(B, [[1, 3], [9, 11]])
    assert np.allclose(AB, [[5, 7], [13, 15]])  # effectively BA because A is mode 1


def test_cloning():
    cov = np.array([[1,2],[3,4]])
    cov_cloned = gp.clone_cov(cov, modes=[0], times=1)
    cov_expected = np.array([[1,0,2,0],[0,3,0,4],[0,1,0,2],[0,3,0,4]])
    assert np.allclose(cov_cloned, cov_expected)

def test_cloning_means():
    means = np.array([1,2])
    means_cloned = gp.clone_means(means, modes=[0], times=1)
    means_expected = np.array([1,1,2,2])
    assert np.allclose(means_cloned, means_expected)
