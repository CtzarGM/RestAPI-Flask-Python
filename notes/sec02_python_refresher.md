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

[This snippet exemplifies this](../src/sec02_python_refresher/01_variables.py)

### Key Takeaway

When passing database models, list parameters, or JSON payloads between service layers in our REST API, passing a mutable object (like a list of products) does not copy the data. It passes the pointer. If you mutate that list inside a validation helper, you mutate the original data everywhere else in that execution thread!

## 03. String Formatting in Python

As our Inventory Engine processes incoming payloads, queries databases, and routes traffic, our server will need to output clean, readable logs. String formatting is how we construct these messages dynamically.

While Python has historically supported multiple ways to format strings (like `%` formatting and `.format()`), modern Python relies heavily on F-strings (Formatted String Literals), introduced in Python 3.6. They are not only cleaner and more readable but also significantly faster.

### The Evolution of String Formatting

1. Format Method (`.format()`): Useful when you want to define a template string in one place and reuse it with different variables later.

   ```Python
   template = "Product: {} | Price: ${:.2f}"
   log = template.format("Mechanical Keyboard", 129.99)
   ```

2. F-Strings (`f""`): Evaluated at runtime, allowing you to embed Python expressions directly inside curly braces `{}`.
   ```Python
   name = "Mechanical Keyboard"
   price = 129.99
   log = f"Product: {name} | Price: ${price:.2f}"
   ```

### Practical Example: Generating Server & Ledger Logs

Let's write a script that simulates a database record pull and formats a structured log entry for a warehouse operator. We will format raw values into currency, pad strings for neat tabular display, and execute inline expressions.

[String formatting example](../src/sec02_python_refresher/02_string_formatting.py)

### Key Takeaway

When emitting structured logs to standard output (stdout) or writing automated test assertions, F-strings let us easily align data columns and clean up floating-point values (like rounding money to two decimals: `:.2f`) without altering the actual data types stored in our PostgreSQL tables.
