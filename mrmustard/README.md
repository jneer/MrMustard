# Contributing to MrMustard
Write tests for any new functionality.

# Structure of MrMustard
MrMustard is split into four components: the concrete classes, the abstract classes, the plugins and the backends.
We also have a utils module, which we plan to deprecate.

## 1. Abstract base classes
Abstract base classes cannot be instantiated, as they are abstract.
At the moment the main abstract classes are:
    - `Parametrized` (functionality for all parametrized objects (Ops, Detectors, etc...))
    - `Op` (abstract parent class for gates and Gaussian detectors)
    - `State` (abstract parent class for all types of states (Vacuum, Coherent, etc...))
    - `Detector` (abstract parent class for non-Gaussian detectors (PNRs, Threshold, etc...))

Unless it's for a bug or a planned feature, we don't expect to touch these classes very often.

## 2. Concrete classes
Concrete classes are the specific Ops (like Squeezers, Homodyne detectors, etc...)
or Detectors (like PNRs, Threshold, etc...) or states (Vacuum, Coherent, etc...).

To develop additional concrete classes, determine which type of object you are implementing 
e.g. a new gate) and add it to the appropriate file, 
following the conventions you see holding for other similar objects.

## 3. Plugins
Plugins add functionality without committing to a specific numerical library
(which is instead handled by the backend). At the moment the main plugins are:
    - `SymplecticPlugin` (phase space functionality)
    - `FockPlugin` (Fock space functionality)
    - `TrainPlugin` (optimization functionality)

To develop the existing plugins (or to add new ones) one needs to make sure that only the 
math backend is used when calling numerical math methods.

## 4. Backends
The numerical functionality (be it with autodiff or not) is supplied by the backends.

To write a new backend (e.g. at the time of writing we don't have a pytorch backend) 
ne needs to create a new directory inside `backends/` for the new backend and implement
a concrete interface for low-level math according to the `BackendInterface`.