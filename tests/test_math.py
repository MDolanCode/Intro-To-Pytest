"""
This module contains basic unit tests for math operations.
Their purpose is to show how to use the pytest framework by example.
"""

# -------------------------------------------------------------------
# imports
# -------------------------------------------------------------------

import pytest

# -------------------------------------------------------------------
# A most basic test function
#--------------------------------------------------------------------

# Always use the convention test_ when writing tests.
# You can have other functions that are not test functions within the test.
# Pytest uses Python's native assert. No special library.
# To run the test in terminal use: python3 -m pytest

@pytest.mark.math
def test_one_plus_one():
    assert 1 + 1 == 2


# --------------------------------------------------------------------
# A test function to show assertion introspection
# --------------------------------------------------------------------
""""
* When you run the test it will show assertion introspection, 
and show you what is wrong in Terminal. It shows the variables values.

* When a test fails it will show the type of exception that causes the test to fail.
* When a test fails with assert it will be an assertion error. 
* However tests will fail for any unhandled exception type.

* Pay attention to the exception types to determine if test failures are due to legitimate
defects or automation bugs.

* Pytest lists the failed tests in terminal and concludes by printing the test result totals.
* Pytest's test report is concise and helpful.
"""

# Failed test below
# def test_one_plus_two():
#     a = 1
#     b = 2
#     c = 0
#     assert a + b == c

@pytest.mark.math
def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c

# ---------------------------------------------------------------------
# A test function that verifies an exception. 
# ---------------------------------------------------------------------
"""
* Dividing by zero raises and ZeroDivisionError.
* Pytest safely catches any and all unhandled exceptions, performs any cleanup
and moves onto the next test case.
* Exceptions for one test case won't effect other tests.
"""

# Failed test because of exception.
# def test_divide_by_zero():
#     num = 1 / 0

@pytest.mark.math
def test_divide_by_zero():
    """
    * "with" is a special statement for automatically handling extra enter and exit logic for our caller.
    commonly used for file input and output.
    * Enter logic opens the file; the boady reads or writes.
    * Exit logic closes the file.
    * For pytest.raises the enter logic makes the code catch any exceptions and the exit logic asserts 
    the desired exception type was actually raised.
    * In this case it catches the ZeroDivisionError.
    * pytest.raises looks for an exception of a specific type. If the steps within the "with" statements body 
    do not raise the desired exception, then it will raise a assertion error to fail the test.
    * pytest.raises makes the test code more concise and avoids repeatitive try except blocks.
    * Can also verify attributes of the raised exception. "with" statement stores exception object in a variable. with pytest.raises(ZeroDivisionError) as e: (e is the variable)
    * Can verify the exception's message -> assert 'division by zero' in str(e.value)
    """
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

        assert 'division by zero' in str(e.value)


# Multiplication test ideas

# two positive integers
# identity: mutiplying any number by 1
# zero: multiply any number by 0
# positive by a negative
# negative by a negative
# multiply floats

# Unnessessary tests should be avoided because they add time and cost for little value in return. 


# writing tests like below get repetitive and go against DRY.
# DRY Principle: Don't Repeat Yourself!
# Code duplication becomes code cancer. Copies of the same logic becomes burdensome too. 
# pytest has a better pattern -> @pytest.mark.parametrize: parametrizing test functions.

# def test_multiply_two_positive_ints():
#     assert 2 * 3 == 6


# def test_multiply_identity():
#     assert 1 * 99 == 99


# def test_multiply_zero():
#     assert 0 * 100 == 0

# -------------------------------------------------------------------
# A parametrized test function
# -------------------------------------------------------------------

products = [
    (2, 3, 6),          # positive integers
    (1, 99, 99),        # identity
    (0, 99, 0),         # zero
    (3, -4,-12),        # positive by negative
    (-5, -5, 25),       # negative by negative
    (2.5, 6.7, 16.75)   # floats
]
"""
* @pytest.mark.parametrize is a decorator for the test_multiplication function.
* In Python a decorator is a special function that wraps around another function. A simple form of aspect oriented programming.
* Inner function is the test case, outer function is the decorator.
* Will call test case per input tuple.
* Can use @pytest.mar.parametrize to run a test case with multiple inputs.
* The decorator uses British English for spelling.
* Two parameters are passed 1st argument is a string of a comma separated list of variable names. These names must match the parameter names in the test case function.
The second argument is the list of parametrized values. Note that the number of varibale names and the length of each tuple in the list is 3. These must match.
* When pytest runs this test it will run it 6 times. Once for each tuple in the parameter list.

*  pytest parameters make it easy to do data driven testing in which the same test cases crank through multiple inputs.
"""

@pytest.mark.math
@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product


