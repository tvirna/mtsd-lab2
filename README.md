# Typed List Implementation with Unit Testing

## Overview

This project showcases the development of a **character-based linked list** implementation in Python, featuring comprehensive **unit test coverage** and automated **Continuous Integration** through GitHub Actions. The application demonstrates working with typed lists and includes a complete refactoring process from one list implementation to another.

## Variant Details and Calculation

Student ID: 4
Variant calculation: 4 % 4 = 0

**Variant 0 Specifications:**
- **Primary implementation:** Singly linked circular list
- **Refactored implementation:** Array-based list (using built-in arrays/lists)

## Functionality

The list class implements the following core operations for Character elements:

- `length() -> int` - Determines list size (returns 0 for empty lists)
- `append(element: Character) -> None` - Appends element to list end
- `insert(element: Character, index: int) -> None` - Inserts element at specified position
- `delete(index: int) -> Character` - Removes and returns element at given index
- `deleteAll(element: Character) -> None` - Eliminates all matching elements
- `get(index: int) -> Character` - Retrieves element at specified position
- `clone() -> List` - Creates independent list copy
- `reverse() -> None` - Reverses element order in-place
- `findFirst(element: Character) -> int` - Locates first occurrence (returns -1 if not found)
- `findLast(element: Character) -> int` - Locates last occurrence (returns -1 if not found)
- `clear() -> None` - Removes all elements
- `extend(elements: List) -> None` - Appends all elements from another list

## Build Instructions and Test Execution

### Prerequisites
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Test Execution
Execute the complete test suite:
```bash
python -m pytest
```

For detailed test output:
```bash
python -m pytest -v
```

### Continuous Integration Setup
- **GitHub Actions** workflow automatically triggers on commits to the main branch
- CI pipeline executes all unit tests and reports results
- Failed builds are clearly indicated in the repository

## Failed Test Commit Reference

Link to commit demonstrating CI failure detection: [Failed Test Commit](https://github.com/tvirna/mtsd-lab2/commit/c711559ed52a10ad008ba8ddb9c88aff39c0f253)

This commit intentionally contains code that breaks existing functionality, showcasing the CI system's ability to catch regressions.

## Development Insights and Conclusions

**Unit Testing Benefits:**
Unit testing significantly enhanced the development process by providing immediate feedback on code correctness. The tests served as a safety net during refactoring, allowing confident implementation changes while maintaining functional integrity. Test-driven development practices helped identify edge cases and boundary conditions that might have been overlooked otherwise.

**CI Integration Value:**
The continuous integration setup proved invaluable for maintaining code quality. Automated test execution on every commit ensures that regressions are caught immediately, preventing broken code from entering the main branch. This automation reduces manual testing overhead and increases development confidence.

**Overall Assessment:**
Rather than being a time waste, unit testing and CI integration represent essential investments in code quality and maintainability. The initial setup effort pays dividends through reduced debugging time, increased refactoring confidence, and improved overall software reliability.