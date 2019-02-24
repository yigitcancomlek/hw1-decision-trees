def test_sklearn_import():
    """
    Please don't import sklearn to solve any of the problems in this assignment. If you
    fail this test, we will give you a zero for this assignment, regardless of how
    sklearn was used in your code.

    the 'a' in the file name is so this test is run first on a clean Python interpreter.
    """
    import sys
    import code
    assert 'sklearn' not in sys.modules.keys()