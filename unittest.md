# Testing

There are multiple methods for writing test functions. Here we briefly review `unittest`

## Unittest
We have an example module implemented in `code/src/area.py` where we compute surface area of 
triangulated mesh file by computing the surface area of all triangles. Test functions are implemented
in `code/test` folder. To run the tests run 
```
cd code
python -m unittest test/test_area.py
```

This will automatically run all test functions implemented in `test/test_area.py` file. 
The content of `test_area.py` is a class inheriting from `unittest.TestCase`. 
Any method in this class that starts with `test` is considered a test function and `unittest` will execute them.
In addition, `unittest` provide assertion methods such as `assertTrue, assertEqual, assertAlmostEqual` that can be used to verify the outcome of tested modules.

The common practice is to create a `test_X.py` file for test module `X` of your code. 
Within this file, different elements of the module can be test by various `test_xx` methods.
For example for the module `area` we defined `test_area` which test submodules such as 
`compute_triangle_area` and `compute_mesh_area`.

For more detail, see [here](https://realpython.com/python-testing/)