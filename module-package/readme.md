## module vs package

-the terms 'module' and 'package' are used to organize and structure code.

- let's clarify the distinctions between the two

-module: - modules are meant to be resuable pieces of code that can be imported into other modules or scripts. - a module is a single file containing python code (simply .py file)- it can define functions,classes and variables.

-package: - a package is way of organizing related modules into a single directory hierarchy. - it include a special `__init__.py` file(which can be empty) to indicate that the directory should be treated as package - packages can contain sub-packages and modules, allowing for a nested structure.

# example

my_package/
├── **init**.py
├── module1.py
├── module2.py
└── subpackage/
├── **init**.py
└── module3.py

# to use modules from package

from my_package import module1,subpackage.module3

# note library is a collection of package
