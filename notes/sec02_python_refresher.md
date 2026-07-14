# Sec02 Python Refresher

## 02. Variables in Python (Memory Model & Reference Tracking)

In Python, variables do not act like static "boxes" where values are permanently stored. Instead, they act as pointers or labels that refer to specific objects residing in system memory.

When building an enterprise inventory system, understanding this reference model is critical. Mishandling object references is one of the most common ways to introduce subtle bugs, such as accidentally mutating product states across different stores.

Understanding the Pointer Model in Python
Every time you create a variable in Python, two things happen:

1. An object is created in memory (with a specific value and type).
1. The variable name is bound to that object's memory address.

We can inspect the exact memory address of any object using Python's built-in id() function.

- Immutable Types (Strings, Integers, Floats, Tuples): Once created in memory, their value cannot be changed. If you "modify" them, \* Python actually creates a new object at a new memory address and points the variable to it.
- Mutable Types (Lists, Dictionaries, Sets): The container itself can be modified in place. Multiple variables pointing to the same mutable object will all reflect any changes made to it.

[This is an example](../src/sec02_python_refresher/01_variables.py)

### Key Takeaway

When passing database models, list parameters, or JSON payloads between service layers in our REST API, passing a mutable object (like a list of products) does not copy the data. It passes the pointer. If you mutate that list inside a validation helper, you mutate the original data everywhere else in that execution thread!
