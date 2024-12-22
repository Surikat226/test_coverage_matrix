from tabulate import tabulate
import pytest

def main():
    coverage_table = [
        pytest.main(['.\\test_strings.py', '.\int_tests\\test2.py' '--collect-only'])
    ]


if __name__ == '__main__':
    main()