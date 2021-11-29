# Copyright 2021 Xanadu Quantum Technologies Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from mrmustard import settings
import mrmustard.physics.fock
import mrmustard.physics.gaussian
from mrmustard.lab.abstract import State



def fidelity(a: State, b: State) -> float:
    r"""
    Compute the fidelity between two states.
    """
    # if both states are gaussian use the gaussian fidelity
    if a.is_gaussian and b.is_gaussian:
        return mrmustard.physics.gaussian.fidelity(a.means, a.cov, b.means, b.cov, hbar=settings.HBAR)
    else:
        # fock representation is automatically generated
        return mrmustard.physics.fock.fidelity(a.fock, b.fock, a_pure=a.is_pure, b_pure=b.is_pure)


def purity(a: State) -> float:
    r"""
    Compute the purity of a state.
    """
    if a.is_pure:
        return 1.0
    if a.is_gaussian:
        return gaussian.purity(a.cov, settings.HBAR)
    else:
        return fock.purity(a.fock)  # dm


def entropy(a: State) -> float:
    r"""
    Compute the entropy of a state.
    """
    if a.is_pure:
        return 0.0
    if a.is_gaussian:
        return gaussian.entropy(a.cov, settings.HBAR)
    else:
        return fock.entropy(a.fock)



def number_means(a: State) -> Vector:
    r"""
    Returns the mean photon number for each mode.
    """
    if a.is_gaussian:
        return gaussian.number_means(a.cov, a.means, settings.HBAR)
    else:
        return fock.number_means(tensor=a.fock, is_dm=a.is_mixed)



def number_cov(self) -> Matrix:
    r"""
    Returns the complete photon number covariance matrix.
    """
    if a.is_gaussian:
        return gaussian.number_cov(a.cov, a.means, settings.HBAR)
    else:
        raise NotImplementedError("number_cov not implemented for non-Gaussian states")