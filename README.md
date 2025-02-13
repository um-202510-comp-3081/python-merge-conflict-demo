# Git Merge Conflict Exercise

This exercise will help you understand how merge conflicts occur and how to resolve them. You'll work with a simple Python calculator that's being developed by multiple team members simultaneously.

## Setup

1. Clone the repository:
    ```
    git clone [repository-url]
    cd [repository-name]
    ```

    The repository contains:
    - A basic calculator with add and subtract functions
    - A feature branch (`feature-multiply`) that adds multiplication

## Your Task

1. Make sure you're on the main branch:
    ```
    git switch main
    ```

2. Add a division function to `calculator.py`. Your function should:
   - Take two parameters: `num1` and `num2`
   - Include error handling for division by zero
   - Return the result of `num1 / num2`
   - Add a test case in the `__main__` block

3. Commit your changes.

4. Try to merge in the multiplication feature:
    ```
    git merge feature-multiply
    ```

## Resolving the Conflict

You'll encounter a merge conflict! This happens because both branches modified the same file in similar locations. In the code, you'll see conflict markers.

To resolve the conflict:

1. Open `calculator.py` in your editor
2. Identify both sets of changes
3. Combine them logically:
   - Keep both functions (multiply and divide)
   - Maintain consistent code style
   - Include both test cases in the `__main__` block
4. Remove the conflict markers (if any remain)
5. Test that your calculator works
6. Stage and commit the resolved file

## Success Criteria

Your final calculator should:
- Have four functions: add, subtract, multiply, and divide
- Handle division by zero appropriately
- Have test cases for all functions in the `__main__` block
- Maintain consistent code style
- Run without errors
