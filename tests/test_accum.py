"""
This module contains basic unit tests the the accum module.
Their purpose is to show how to use the pytest framework by example
"""

# ------------------------------------------------------------------
# imports
# ------------------------------------------------------------------


import pytest
from stuff.accum import Accumulator

# -------------------------------------------------------------------
# Fixture
# -------------------------------------------------------------------

"""
* Fixtures are special functions that pytest can call before test case functions.
* They're the best way to handle "Arrange" steps shared by multiple tests in the context of the "Arrange-Act-Assert" pattern.
* Fixtures are functions.
* This accum fixture is concise because the only thing it needs to do is create a new Accumulator object.
* Importantly, note that the function _returns _the newly constructed object. It does not assign the object to a global variable. A fixture should always return a value.
* Remove the object creation line accum = Accumulator() and add a parameter to the test function signature named accum.
* When pytest discovers a test case function, it looks at the function's parameter list.
* If the function has parameters, then it will search for fixtures to match each parameter's name.
* In our case, the test function has a parameter named accum, so pytest looks for a fixture named accum which it will find in the same module.
* Pytest will then execute the fixture and pass the fixture's return value into the test case function.
* Thus, in our test case, the accum variable will refer to the new Accumulator object created by the accum fixture. 
* This is a clever form of dependency injection.
* The test case doesn't set up or "arrange" the test objects itself.
* Instead, the fixture handles setup and injects the required objects as dependencies into the test function.
* This separation of concerns makes test cases more readable, more consistent, and more maintainable.
* It also makes new test cases easier to write.

* pytest avoids the limitations of classes by structuring tests as functions.

* Fixtures are simply the function-based way to handle setup and cleanup operations.

* Fixtures can be used by any test function in any module, so they are universally shareable since they use dependency injection to share state, they protect tests against unintended side effects.


Advanced Fixture Features
* There are a few advanced tricks you can do with fixtures as well. If you want to share fixtures between multiple test modules, you can move it to a module in the "tests" directory named "conftest.py".
* Conftest modules share test code for pytest. The name of the module is important. Pytest will automatically pick up any fixtures here.

* A test case can also use multiple fixtures, just make sure each fixture has a unique name: 

@pytest.fixture
def accum():
  return Accumulator()

@pytest.fixture
def accum2():
  return Accumulator()

def test_accumulator_init(accum, accum2):
  assert accum.count == 0


* I also mentioned that fixtures can handle both setup _and _cleanup. If you use a yield statement instead of a return statement in a fixture, then the fixture function becomes something known in Python as a "generator".

@pytest.fixture
def accum():
  yield Accumulator()
  print("DONE-ZO!")

"""

@pytest.fixture
def accum():
    return Accumulator()


# ------------------------------------------------------------------
# Tests
# ------------------------------------------------------------------


"""
* Method test_accumulator_init() verifies that the new instance of the Accumulator class has a starting count of zero.

* Method test_accumulator_add_one() verifies that the add() method adds one to the internal count when it is called with no other arguments.

* Method test_accumulator_add_three() verifies that the add() method adds 3 to the count when it is called with the argument of 3.

* Method test_accumulator_add_twice() verifies that the count increases appropriately with multiple add() calls.

* Finally, method test_accumulator_cannot_set_count_directly() verifies that the count attribute cannot be assigned directly because it is a read-only property. Notice how we use pytest.raises to verify the attribute error.

* Take a moment to review and study these tests functions.

* You will notice that all of these unit tests follow a common pattern.

* They construct an Accumulator object, they make calls to the Accumulator object, and they verify the counts of the Accumulator objects or else verify some error.
"""

@pytest.mark.accumulator
def test_accumulator_init(accum):
    assert accum.count == 0


@pytest.mark.accumulator
def test_accumulator_add_one(accum):
    accum.add()
    assert accum.count == 1


@pytest.mark.accumulator
def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count == 3


@pytest.mark.accumulator
def test_accumulator_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count == 2


@pytest.mark.accumulator
def test_accumulator_cannot_set_count_directly(accum):
    with pytest.raises(AttributeError, match=r"can't set attribute") as e:
        accum.count = 10


"""
* This pattern is called "Arrange-Act-Assert". It is the classic three-step pattern for functional test cases.

1. Arrange assets for the test (like a setup procedure).

2. Act by exercising the target behavior.

3. Assert that expected outcomes happened.

* Remember this pattern whenever you write test cases. Following this pattern will keep your tests simple, focused, and valuable. It will also help you separate tests by unique behaviors.
* Notice how none of our tests take any more Act steps after their Assert steps.
* Separate, small, independent tests make failure analysis easier in the event of a regression.
"""