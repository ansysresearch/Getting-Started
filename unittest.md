# Testing

There are multiple methods for writing test functions. Here we briefly review `unittest`

## Unittest
Go to `code` folder and then run 
```
python -m unittest test/test_area.py
```

This will automatically run all test functions implemented in `test/test_area.py` file. 
The content of `test_area.py` is a class inheriting from `unittest.TestCase`. 
Any method in this class that starts with `test` is considere a test function and `unittest` will execute them.
In addition, `unittest` provide assertion methods such as `assertTrue, assertEqual, assertAlmostEqual` that can be used to verify the outcome of tested modules.

The common practice is to create a `test_X.py` file for test module `X` of your code. Within this file, different elements of the module can be test by various `test_xx` methods.

For more detail, see [here](https://realpython.com/python-testing/)