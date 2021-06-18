# Python Code Style

At Ansys, we encourage you to follow PEP8 coding style. Below, you can find some of most important guidelines. Additional examples can be found at [here](https://www.python.org/dev/peps/pep-0008/).

- Naming Conventions:
    - Choose meaningful names for your variables.
    - Use lower_case_with_underscore convection for variable and function names.
	- Use CAPTITAL convection to define constants.
	- Use CamelCase convention for classes.

	```python
	# bad example, poor naming
	def my_function(x):
	    return x ** 2

	# good example
	def square(x):
		return x ** 2

	# defining constant
	PI = 3.1415

	# CamelCase convention for classes
	class GraphNode:
	    def __init__(self, x, y):
	        self.x = x
	        self.y = x
	```

- Indentation: Use four (and not two) spaces (and not tabs).
- Whitespace:
    - use whitespace before and after operation like `+, -, /, *, =, ==, <, >, +=` unless inside function arguments.
    - use whitespace after comma `,`.
    - avoid using whitespace before open parenthesis/brackets when calling functions or indexing list.

    ```python
    # bad examples
    spam( ham[ 1 ], { eggs: 2 } )  #unneccesary whitespace
    print (1)  #unneccesary whitespace
    dct ['key'] = lst [index]  #unneccesary whitespace
    i=i*3  #necessary whitespace
    np.sum(x, axis = 1)  #unnecessary whitespace

    # good examples
    spam(ham[1], {eggs: 2})
    print(1)
    dct['key'] = lst[index]
    i = i * 3
    np.sum(x, axis=1)
    ```
- Handling directory and file addresses
	- Use the built-in `os` library to combine directories.
	- Do not hard code any file/directory address.
	- A list of useful functions: `os.path.join, os.path.split, os.path.abspath, os.listdir, os.makesdir, os.path.isfile, os.path.isdir`

	```python
	# bad example
	full_file_name = parent_dir + "/" + file_name

	# good example
	full_file_name = os.path.join(parent_dir, file_name)

	# bad example
	data_folder = "C:/Users/amaleki/data/"

	# better example, assuming args hold the arguments passed to the program
	data_folder = args.data_folder

	# create a folder if it does not exist
	if not os.path.isdir(parent_folder):
	    os.makesdir(parent_folder)

	```

	- when designing functions:
		- each function shall do one and only one thing.
		- functions should not have side effects.
		- if you find yourself with functions with lots of arguments, chances are you can refactor your code, e.g. use classes.

		```python
		# bad example
		full_file_name = parent_dir + "/" + file_name

		# good example
		full_file_name = os.path.join(parent_dir, file_name)

		# bad example
		data_folder = "C:/Users/amaleki/data/"

		# better example, assuming args hold the arguments passed to the program
		data_folder = args.data_folder

		# create a folder if it does not exist
		if not os.path.isdir(parent_folder):
			os.makesdir(parent_folder)

		```
