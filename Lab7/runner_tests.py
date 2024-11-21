import coverage
import unittest
import os

def run_tests():
    cov = coverage.Coverage(source=['Classes', 'UI'])
    cov.start()

    loader = unittest.TestLoader()
    test_folder = os.path.abspath('./Tests')
    tests = loader.discover(test_folder)

    test_runner = unittest.TextTestRunner()
    test_runner.run(tests)

    cov.stop()
    cov.save()

    print("\nCoverage Report:")
    cov.report(show_missing=True)


if __name__ == "__main__":
    run_tests()