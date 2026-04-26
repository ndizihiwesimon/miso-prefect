import unittest

from main import DEFAULT_NAME, build_greeting, hello


class GreetingTests(unittest.TestCase):
    def test_build_greeting_uses_default_name(self):
        self.assertEqual(build_greeting(), f"Hello, {DEFAULT_NAME}!")

    def test_build_greeting_strips_input(self):
        self.assertEqual(build_greeting(" Miso "), "Hello, Miso!")

    def test_hello_task_function_returns_greeting(self):
        self.assertEqual(hello.fn("Prefect"), "Hello, Prefect!")


if __name__ == "__main__":
    unittest.main()
