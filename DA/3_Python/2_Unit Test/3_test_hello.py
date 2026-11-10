from hello_4 import hello;

def test_hello():
    assert hello("Ayush") == "hello, Ayush";

def test_hello_2():
    assert hello("David") == "hello, David";

def test_hello_3():
    assert hello("Harry") == "hello, Harry";

def test_default():
    assert hello() == "hello, world";

