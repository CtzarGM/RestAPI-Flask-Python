# Sec02 Python Refresher

## 01. Variables in Python (Memory Model & Reference Tracking)

In Python, variables do not act like static "boxes" where values are permanently stored. Instead, they act as pointers or labels that refer to specific objects residing in system memory.

When building an enterprise inventory system, understanding this reference model is critical. Mishandling object references is one of the most common ways to introduce subtle bugs, such as accidentally mutating product states across different stores.

Understanding the Pointer Model in Python
Every time you create a variable in Python, two things happen:

1. An object is created in memory (with a specific value and type).
1. The variable name is bound to that object's memory address.

We can inspect the exact memory address of any object using Python's built-in id() function.

- Immutable Types (Strings, Integers, Floats, Tuples): Once created in memory, their value cannot be changed. If you "modify" them, \* Python actually creates a new object at a new memory address and points the variable to it.
- Mutable Types (Lists, Dictionaries, Sets): The container itself can be modified in place. Multiple variables pointing to the same mutable object will all reflect any changes made to it.

[Variables example](../src/sec02_python_refresher/01_variables.py)

### Key Takeaway

When passing database models, list parameters, or JSON payloads between service layers in our REST API, passing a mutable object (like a list of products) does not copy the data. It passes the pointer. If you mutate that list inside a validation helper, you mutate the original data everywhere else in that execution thread!

## 02. String Formatting in Python

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

## 03. Getting User Input in Python

While our production Flask REST API will ultimately receive data through HTTP requests (using JSON payloads), during early development and system scripting, we often rely on command-line prompts to interact with scripts.

In Python, we capture user input using the built-in `input()` function.

### How `input()` Operates Under the Hood

1. Blocking Operation: When Python hits `input()`, it pauses execution and waits for the user to type something in the terminal and press `Enter`.

1. String Default: The `input()` function always returns a string, regardless of what the user types. If you expect a number (like a product's price or count), you must explicitly convert (cast) it to the target data type (e.g., `int()` or `float()`).

### Practical Example: CLI Product Intake Tool

Let's write a simple command-line intake wizard. This tool prompts an administrator for a product's details, casts the data to the appropriate types, handles potential input errors gracefully, and prints a formatted confirmation.

[User input example](../src/sec02_python_refresher/03_getting_user_input.py)

### Key Takeaway

User inputs cannot be trusted. Just like we cast `input()` strings and catch potential `ValueError` exceptions here, our API will need strict validation rules (which we'll handle elegantly later using Marshmallow schemas) to ensure a user doesn't pass letters to an integer stock field

## 04. Writing Our First Python App

Up to this point, we have explored variables, formatted text, and accepted input. Now, we are combining these foundational elements to build our first mini-application: an Interactive Store Valuation Calculator.

This app simulates a lightweight command-line portal where a retail manager can calculate key financial metrics for a specific shop's inventory on the fly.

### Architectural Concept: Input, Process, Output (IPO)

Every solid backend service or script follows the IPO design pattern:

1. Input: Securely capture raw data (simulating our future HTTP payloads).

1. Process: Transform, clean, and compute the data (business logic).

1. Output: Formulate a structured, readable response (simulating our future JSON responses).

### Practical Example: Store Valuation Calculator

We will write an interactive utility that takes store details and product metrics to calculate total value, average item price, and return a clean, executive-level terminal summary.

[First app example](../src/sec02_python_refresher/03_getting_user_input.py)

### Key Takeaway for our Inventory Engine

Even simple apps require strict control flow, type transformations, and zero-division protection to remain stable. When we transition this logic into REST API controllers, the core calculation logic remains identical—only the delivery system changes from terminal strings to HTTP JSON bodies.

## 05. Lists, Tuples, and Sets in Python

When building a system to track stock, we rarely deal with just one product at a time. We need collections to group our items together. Python offers three primary built-in collection types, each designed for a specific structural purpose.

### The Three Core Collection Types

- Lists (`[]`): Ordered, mutable sequence of elements. Elements can be modified, added, or duplicated.
  - Best for: A dynamic queue of products in a store's active stock list where items can be added, sorted, or removed.

- Tuples (`()`): Ordered, immutable sequence of elements. Once created, a tuple cannot be changed or resized.
  - Best for: Fixed data structures, like latitude/longitude coordinates of a warehouse, or database connection settings `(host, port)`.

- Sets (`{}`): Unordered, mutable collection of unique elements with no duplicates.
  - Best for: Rapidly checking membership or grouping unique tags (like `{"electronics", "sale"}`) where duplicates don't make sense.

### Practical Example: Managing Collections of Stock

Let's write a script that illustrates the practical behavior of all three collections under the hood.

[Python Collections example](../src/sec02_python_refresher/03_getting_user_input.py)

### Key Takeaway for our Inventory Engine

Selecting the right collection prevents performance issues and design bugs. We use lists to order and manipulate query results, tuples to safely pass read-only config properties, and sets when we need to instantly check if a product has a specific permission tag without searching through an entire array item-by-item.

## 06. Booleans in Python (Evaluating Logic & State)

Booleans in Python represent one of two logical states: `True` or `False`.

When coding the business logic of our API, booleans drive security checks (e.g., `is_admin = True`), database queries (e.g., `is_active = False`), and stock level flags (e.g., `needs_restock = True`).

### Comparison Operators

Booleans are typically generated by evaluating comparisons between variables:

- `==` : Equal to (checks if values match)

- `!=` : Not equal to

- `> / <` : Greater than / Less than

- `> = / <=` : Greater than or equal / Less than or equal

- `is` : Identity check (checks if two variables refer to the exact same memory object)

### Logical Operators

We combine boolean expressions using logical operators:

- `and` : Evaluates to True only if both sides are True.

- `or` : Evaluates to True if at least one side is True.

- `not` : Reverses the boolean state.

### Practical Example: Stock Level Flags and Access Auditing

Let's write a script that validates if a shop has stock issues and evaluates if an incoming transaction payload meets both permission and inventory requirements.

[Booleans Examples](../src/sec02_python_refresher/06_booleans.py)

### Key Takeaway for our Inventory Engine

In Python, `==` checks for value equality, which is what we want 99% of the time when comparing database IDs or string keys. We rarely use `is` unless checking against the singleton value `None` (e.g., `if product is None:`), which indicates a record was not found in the database.

## 07. Advanced Set Operations (Tag & Category Math)

In our inventory system, products will have tags (e.g., `{"electronics", "home-office", "wireless"}`).
When a user filters products, or when we want to recommend related items, we can use Set Operations to compare these lists instantly without writing nested loops. This is incredibly fast, optimized, and elegant.

###Core Set Operations

- Difference (`.difference()` or `-`): Returns elements in the first set that are not in the second set.
  - Use case: Finding which tags are missing from an incoming product payload compared to our master list of allowed categories.

- Intersection (`.intersection()` or `&`): Returns elements that are common to both sets.
  - Use case: Finding matching tags between a user's interests and a product's categories.

- Union (`.union()` or `|`): Combines all unique elements from both sets.
  - Use case: Merging category tags when combining two store catalogs.

### Practical Example: Product Tag Auditing

Let's write a script that compares an incoming product's tags against our store's allowed master tags to see if they match, have invalid entries, or share common categories.

[Advanced set operations example](../src/sec02_python_refresher/07_advanced_sets_operations.py)

### Key Takeaway for our Inventory Engine

Using set operations like `.difference()` allows us to perform validation checks in $O(1)$ average time complexity. This is significantly faster and cleaner than writing nested `for` loops to compare arrays, keeping our backend insertion pipeline lightweight.

## 08. `if` Statements (Conditional Branching)

In code, conditional branching is how our application makes decisions. When our REST API receives a request, we will use `if` statements to evaluate conditions like: "Is this product out of stock?", "Does the user have admin privileges?", or "Is the database connection alive?".

### Anatomy of an `if` Statement in Python

Python uses indentation (4 spaces) instead of curly braces {} to define blocks of code.

```Python
if condition:
    # Executed if condition is True
elif another_condition:
    # Executed if the first condition is False AND this one is True
else:
    # Executed if all above conditions are False
```

### Practical Example: Automated Order Processing Decision Tree

Let's write a script that evaluates an incoming order against stock levels, warehouse status, and a customer's VIP standing to decide if an order can be fulfilled, backordered, or rejected.

[If statements example](../src/sec02_python_refresher/08_if_statements.py)

### Key Takeaway for our Inventory Engine

Indentation is syntax in Python. Misaligning your spaces by even one character will throw an IndentationError. When we write routes in Flask, the entire execution logic of the endpoint will be nested inside an indented block under the route definition.

## 09. The `in` Keyword in Python

In backend development, we constantly need to check for membership. We might need to ask: "Is this product category supported by our store?", "Is this SKU in our recalled items list?", or "Does this user's list of roles contain 'admin'?"

In Python, the `in` keyword makes these membership checks incredibly readable and highly efficient.

### How `in` Works Across Different Collections

- Lists / Tuples: Python iterates through the elements one by one until it finds a match. (Time complexity: $O(N)$).
- Sets: Python uses a hash table to check membership almost instantly, regardless of how large the set is. (Time complexity: $O(1)$).
- Strings: Checks if a substring exists inside another string.
- Dictionaries: Checks if a key exists in the dictionary's keys (not its values).

### Practical Example: SKU Blacklist and Tag Validation

Let's write a script that checks if an incoming product's tag or SKU belongs to a specific collection (like a list of recalled product SKUs or an active campaign tag set).

[In keyword example](../src/sec02_python_refresher/09_in_keyword.py)

### Key Takeaway for our Inventory Engine

Checking membership in a `set` or a `dict` is practically instantaneous because of hashing. If you are validating millions of records against a blacklist, always store your blacklist as a set (e.g., `{}`) rather than a list (e.g., `[]`) to keep your API response times lightning fast.

## 10. `if` Statements with the `in` Keyword

In our REST API, we will frequently use `if` statements combined with the `in` keyword to handle dynamic request validation, such as:

1. Payload Key Checks: Ensuring a client sent mandatory keys in a JSON object before we try to read them.

1. Access Control Checks: Verifying if a client's role is in an allowed set of roles.

1. Data Sanitization: Checking if a user's input contains restricted or blacklisted characters.

### Practical Example: API Payload Validator

Let's write a script that acts as an API validation gatekeeper. It will inspect an incoming dictionary (simulating a JSON request payload) to ensure it contains required fields, uses an approved currency, and doesn't contain blacklisted terms.

[IF + IN example](../src/sec02_python_refresher/10_if_statements_with_in.py)

### Key Takeaway for our Inventory Engine

Checking `key in dictionary` is extremely fast ($O(1)$) and safe. It prevents your application from raising a `KeyError` and crashing when accessing fields that a user or third-party client forgot to include in their API request.

## 11. Loops in Python: The `for` Loop

In Python, a `for` loop is an "iterator-based" loop. Instead of manually incrementing an index variable (like $i$ in a traditional $C$-style loop), Python cleanly binds each item in a collection to a temporary variable, one by one, until the collection is exhausted.

### Common Iteration Patterns

- Iterating Over Lists/Tuples: Accesses each element sequentially.
- Iterating Over Dictionaries: By default, iterating over a dictionary loops through its keys. To loop through keys and values together, we use the `.items()` method.
- The `range()` Function: Generates a sequence of numbers on the fly, useful when you want to run a block of code a specific number of times.

### Practical Example: Batch Inventory Value Reporting

Let's write a script that processes a list of raw stock dictionaries. We will use a `for` loop to calculate the valuation of each item, maintain a running total of our store's total value, and print out a clean, formatted report.

[For Loop example](../src/sec02_python_refresher/11_loops_for.py)

### Key Takeaway for our Inventory Engine

The `for ... in ...` loop is your workhorse for backend data transformations. When querying a database using SQLAlchemy, it will return collections of model instances. We will use for loops just like this one to serialize those models into JSON-compatible lists for our API responses.

## 12. Loops in Python: The `while` Loop

While a `for` loop is built to run over a pre-defined, finite collection, a `while` loop runs indefinitely until a specific condition becomes false.

In backend engineering, we use `while` loops for tasks that don't have a pre-determined end point, such as:

1. Background Workers: Continually polling a message queue or database for new inventory updates.

1. Retry Logic: Trying to reconnect to a PostgreSQL database or MinIO object storage if the initial connection fails, up to a maximum number of attempts.

1. Interactive CLIs: Keeping an administrative terminal session open until the operator types "exit".

### Key Flow Controls: `break` and `continue`

- `break`: Instantly terminates the loop and jumps to the code below it.

- `continue`: Skips the rest of the current iteration and jumps straight back to the condition check at the top of the loop.

### Practical Example: Simulated Database Connection Retrier

Let's write a utility that simulates attempting to connect to our PostgreSQL instance. It will retry the connection until it succeeds, but will gracefully bail out (`break`) if it exceeds a maximum retry limit to avoid infinite loops and hanging threads.

[While Loop example](../src/sec02_python_refresher/11_loops_for.py)
