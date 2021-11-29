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


from mrmustard.utils.types import *
from mrmustard import settings
import mrmustard.physics.fock
import mrmustard.physics.gaussian
from mrmustard.lab.abstract import State


def entropy_VonNeumann(a: State) -> float:
    r"""
    Compute the Von Neumann entropy of a state.
    """
    if a.is_pure:
        return 0.0
    if a.is_gaussian:
        return gaussian.entropy(a.cov, settings.HBAR)
    else:
        return fock.entropy(a.fock)


def entropy_conditional(a: State, b: State) -> float:
    r"""
    Compute the conditional entropy of a state.
    """
    raise NotImplementedError()


def entropy_relative(a: State, b: State) -> float:
    r"""
    Compute the relative entropy of a state.
    """
    raise NotImplementedError()