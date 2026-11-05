# Copilot Productivity Sprint - Benchmark Tasks

## Objective

Define three independent Python programming tasks to compare development productivity with and without GitHub Copilot.

Each task is designed to take approximately 15–30 minutes and includes explicit requirements, inputs, outputs and acceptance criteria - to support consistent implementation and objective evaluation.

All tasks will use Python 3, with the same specifications and acceptance criteria applied to both manual and AI-assisted coding sessions.

---

## Task 1 - User Registration Validation

**Estimated Time**: 15–20 minutes

**Requirements**:

Implement a Python function named `validate_user(data)` that validates user registration information.

The function must:

- Accept a dictionary containing `name`, `email` and `age`.
- Require `name` to be a non-empty string after removing surrounding whitespace.
- Require `email` to be a string containing exactly one `@`, with non-empty text before and after it and a period in the domain portion.
- Require `age` to be an integer between 18 and 120 inclusive; Boolean values must not count as integers.
- Return validation errors without raising exceptions for missing or invalid fields.

**Inputs**:

```python
{
    "name": "Alex",
    "email": "alex@example.com",
    "age": 25
}
```

**Outputs**:

A dictionary containing a Boolean `valid` field and a list of error messages.

Example successful output:

```python
{
    "valid": True,
    "errors": []
}
```

Example invalid output for `{"name": "", "email": "invalid", "age": 16}`:

```python
{
    "valid": False,
    "errors": [
        "Invalid name",
        "Invalid email",
        "Invalid age"
    ]
}
```

**Acceptance Criteria**:

- Returns `valid: True` and an empty error list for valid registration data.
- Returns `valid: False` when one or more fields are missing or invalid.
- Validates all three fields independently and reports errors in the order: name, email, age.
- Uses the exact error messages `Invalid name`, `Invalid email`, and `Invalid age`.
- Rejects empty names, malformed email addresses, and ages outside the specified range.
- Handles missing fields and incorrect field types without raising exceptions.
- Does not modify the input dictionary.

---

## Task 2 - Sales Data Analysis

**Estimated Time**: 20–25 minutes

**Requirements**:

Implement a Python function named `analyze_sales(transactions)` that calculates total sales revenue and aggregates revenue by product.

The function must:

- Accept a list of transaction dictionaries.
- Read the `product`, `quantity`, and `price` fields from each transaction.
- Calculate revenue for each transaction as `quantity * price`.
- Calculate total revenue across all transactions.
- Aggregate revenue for transactions sharing the same product name.
- Return an empty summary when no transactions are provided.

For this benchmark, inputs are assumed to be valid: product names are non-empty strings, quantities are positive integers, and prices are non-negative integers representing whole currency units. Input validation and currency conversion are outside the scope.

**Inputs**:

```python
[
    {"product": "Keyboard", "quantity": 2, "price": 50},
    {"product": "Mouse", "quantity": 3, "price": 20},
    {"product": "Keyboard", "quantity": 1, "price": 50}
]
```

**Outputs**:

A dictionary containing `total_revenue` and `revenue_by_product`.

Example output:

```python
{
    "total_revenue": 210,
    "revenue_by_product": {
        "Keyboard": 150,
        "Mouse": 60
    }
}
```

**Acceptance Criteria**:

- Correctly calculates revenue for every transaction.
- Returns the correct combined revenue for all transactions.
- Groups transactions with identical product names.
- Handles multiple products and repeated product entries.
- Returns `{"total_revenue": 0, "revenue_by_product": {}}` for an empty list.
- Preserves the original transaction data without modification.
- Produces consistent results regardless of transaction order.

---

## Task 3 - User Creation REST API

**Estimated Time**: 20–30 minutes

**Requirements**:

Implement a small REST API using Python and Flask with a `POST /users` endpoint.

The endpoint must:

- Accept a JSON object containing `name` and `email`.
- Require `name` to be a non-empty string after removing surrounding whitespace.
- Require `email` to be a string containing exactly one `@`, with non-empty text before and after it and a period in the domain portion.
- Reject missing fields, invalid field types, and malformed JSON request bodies.
- Store successfully created users in an in-memory collection.
- Assign sequential integer IDs beginning at `1`.
- Return appropriate HTTP status codes and JSON responses.

A database, authentication system, and persistent storage are not required.

**Inputs**:

HTTP request:

```http
POST /users
Content-Type: application/json
```

JSON body:

```json
{
    "name": "Alex",
    "email": "alex@example.com"
}
```

**Outputs**:

Successful response — HTTP `201 Created`:

```json
{
    "id": 1,
    "name": "Alex",
    "email": "alex@example.com"
}
```

Invalid request response — HTTP `400 Bad Request`:

```json
{
    "error": "Invalid user data"
}
```

**Acceptance Criteria**:

- Provides a working `POST /users` endpoint using Flask.
- Returns HTTP `201` with the created user's ID, name, and email for valid requests.
- Returns HTTP `400` with `{"error": "Invalid user data"}` for missing or invalid fields, malformed JSON, or a non-object JSON body.
- Generates unique sequential integer IDs starting at `1` for successful requests.
- Stores valid users in memory for the lifetime of the running application.
- Does not store invalid submissions or consume an ID when validation fails.
- Uses the same name and email validation rules as Task 1.
- Does not require a database or external storage service.

---

## Benchmark Consistency and Evaluation

All three tasks will be completed under two conditions:

- **Manual Development**: Implement the solution without AI coding assistance.
- **AI-Assisted Development**: Implement the same solution with GitHub Copilot enabled.

For a fair comparison:

- Use the same Python version, development environment, task requirements, and acceptance criteria.
- Record the time required to complete each implementation.
- Measure lines of code consistently, excluding blank lines and comments.
- Evaluate correctness against the defined acceptance criteria.
- Record debugging effort, issues encountered, and any AI-generated code requiring correction.
- Consider the influence of prior task familiarity when interpreting results.

The benchmarks focus on input validation, data processing, and API development, providing a varied but manageable comparison of coding productivity.
