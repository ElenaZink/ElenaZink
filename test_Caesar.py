import pytest
import Caesar

def test_encrypt_basic():
    assert Caesar.encrypt("abc", 1) == "bcd"
    assert Caesar.encrypt("a", 3) == "d"
    assert Caesar.encrypt("", 1) == ""
    assert Caesar.encrypt("hallo", 2) == "jcnnq"
