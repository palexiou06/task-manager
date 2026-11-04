# Task Manager CI/CD

A small Python task manager (todo.py) with unit tests (todo-test.py).
On every push to main, GitHub Actions builds a Docker image, runs the app and the tests,
and updates index.html with the task lists and test results.
Merged pull requests are tracked on a GitHub Projects board.
