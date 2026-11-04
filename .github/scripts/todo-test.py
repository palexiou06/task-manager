import sys
import unittest
from io import StringIO

sys.path.insert(0, __file__.rsplit("/", 1)[0] if "/" in __file__ else ".")
from todo import Task, TaskPool


class TestTaskPool(unittest.TestCase):
    def setUp(self):
        self.pool = TaskPool()

    def test_add_task(self):
        task = Task("New Task")
        self.pool.add_task(task)
        self.assertEqual(len(self.pool.tasks), 1)

    def test_get_open_tasks(self):
        self.pool.populate()
        open_tasks = self.pool.get_open_tasks()
        self.assertEqual(len(open_tasks), 3)
        self.assertTrue(all(task.status == "ToDo" for task in open_tasks))

    def test_get_done_tasks(self):
        self.pool.populate()
        done_tasks = self.pool.get_done_tasks()
        self.assertEqual(len(done_tasks), 3)
        self.assertTrue(all(task.status == "Done" for task in done_tasks))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTaskPool)
    captured_output = StringIO()
    result = unittest.TextTestRunner(stream=captured_output, verbosity=2).run(suite)

    for line in captured_output.getvalue().splitlines():
        if line.endswith("ok"):
            print(line.split(" (")[0] + " ... ok")

    total_tests = result.testsRun
    failed_tests = len(result.failures) + len(result.errors)
    passed_tests = total_tests - failed_tests
    print(f"Total Tests: {total_tests}")
    print(f"Passed: {passed_tests} ({passed_tests / total_tests * 100:.2f}%)")
    print(f"Failed: {failed_tests} ({failed_tests / total_tests * 100:.2f}%)")
    sys.exit(0 if failed_tests == 0 else 1)
