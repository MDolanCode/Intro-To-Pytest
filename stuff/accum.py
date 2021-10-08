"""
This module contains a basic accumulator class.
Its purpose is to show how to use the pytest framework for testing classes.
"""

# -------------------------------------------------------------------------
# Class: Accumulator
# -------------------------------------------------------------------------

"""
* The Accumulator class is very simple, it saves a tally of numbers.
* the __init__(self): method initializes the class with a starting count of zero.
* Internally the tally is saved in the self._count. This variable should be treated as private because it is prefixed with a single underscore.
* The count method returns the value of the count and the method is a property as denoted by the @property. In Python properties control how callers can "get" and "set" values.
* With this property the caller can get the value of count, but cannot set the value directly with an assigment staement.
* The add method is the only way to change the internal count value. It takes in an amount to add and it adds the amount to the internal account. Be default the amount to add is one, but this value may be overwritten.
"""

class Accumulator:

    def __init__(self):
        self._count = 0

    @property
    def count(self):
        return self._count

    def add(self, more=1):
        self._count += more