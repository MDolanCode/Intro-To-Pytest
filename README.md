# -------------------------------------------------------
# Get help
# -------------------------------------------------------
python3 -m pytest --help

# -------------------------------------------------------
# Run Tests
# -------------------------------------------------------
python3 -m pytest

# -------------------------------------------------------
# Pytest Prints More Data When Running This Command 
# -------------------------------------------------------
python3 -m pytest --verbose

# -------------------------------------------------------
# Pytest prints less data when running this command
# -------------------------------------------------------
python3 -m pytest --quiet

# -------------------------------------------------------
# Pytest command to exit tests when 1st failure happens
# -------------------------------------------------------
python3 -m pytest --exitfirst

# -------------------------------------------------------
# Pytest command to exit tests when maxfail is indicated
# -------------------------------------------------------
python3 -m pytest --maxfail=1

# -------------------------------------------------------
# Pytest junit test report
# -------------------------------------------------------
python3 -m pytest --junit-xml report.xml

# -------------------------------------------------------
# Pytest filtering - examples
# -------------------------------------------------------
python3 -m pytest tests/test_accum.py
python3 -m pytest tests/test_rest_api.py
python3 -m pytest tests/test_math.py::test_one_plus_one

python3 -m pytest -k one

python3 -m pytest -k "one and not accum"

# Using markers
python3 -m pytest -m math
python3 -m pytest -m accumulator

# --------------------------------------------------------
# There is a difference between testing code and testing
# features.
# --------------------------------------------------------

White Box -> Is the code written to do expected things?
"Unit" or "Subcutaneous."
They directly test code.
Testing code directly is very important for several reasons. Unit tests are typically small and simple to write. Unit tests catch low-level problems at the source where they're easy to identify and fix. And unit tests run very quickly, meaning you can write several unit tests to maximize coverage.

Black Box -> Does the product meet the requirements?
"Integration" or "End-to-End."
Pytest can also handle what we call "feature" tests (alternately: "black box" tests, "integration tests", "end-to-end" tests, "system" tests, or a whole bunch of other similar names).
Instead of making direct calls to the product code, they interact with a live instance of the product.
For example, calling a REST API and loading a web page in a browser would both be examples of feature tests.
Feature tests are important because they test the product in ways that it would actually be used. For instance, all of the individual methods in the code may work as intended, but building and running everything together might expose integration problems.

Feature testing has downsides, though:
Feature tests require extra setup because they need a live product instance, whether that's the deployed service, a web app, or something else.
Feature tests are prone to interruptions and intermittent errors due to their dependencies on the systems under test.
Feature tests are also slower than unit tests because they need to wait for the product under test to respond.

Nevertheless, testing both the code and the features is important. Each type of test mitigates unique types of risks.


# -------------------------------------------------------------------------
# Pytest Plugins
# -------------------------------------------------------------------------

* Pytest HTML
* Install -> pip3 install pytest-html
* Run -> python3 -m pytest --html=report.html

* Pytest Cov
* Install -> pip3 install pytest-cov
* Run -> python3 -m pytest --cov
* Run -> python3 -m pytest --cov=stuff
* Coverage should only run for product code.
* It can generate an html report -> python3 -m pytest --cov=stuff --cov-report
* You can also override the report name.

* Pytest xdist
* Install -> pip3 install pytest-xdist
* Run -> python3 -m pytest -n 3 
* -n 3 <- number of threads you wish to run at the same time.
* Let's you run tests in parallel.
* Be careful when trying to run tests in parallel though.
* Test cases must be independent, meaning they cannot share any resources or data.
* Otherwise, they could collide and cause each other to fail.
* Test machines and test environments must also be powerful enough to handle multiple tests for it.
* If you aren't careful, you may try to run more tests than your system can effectively handle. "pytest-xdist" also lets you distribute test execution across multiple machines using SSH or sockets.

* Pytest bdd
* Behaviour driven development -> Gerkin



