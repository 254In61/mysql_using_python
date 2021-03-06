#!/usr/bin/bash
# Beautiful approach:
# 1) Try to have the class or function as independent as possible during development.
# 2) For every class developed, create the test case before moving to the next.These are unit tests.
# When you are done, and code is sorted end to end, then develop a combined integration-testing.
# pip3 install pytest

python3 -m pytest -v tests/test_query.py

