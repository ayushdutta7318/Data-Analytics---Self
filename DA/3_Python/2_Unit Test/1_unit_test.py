import pytest;
import square_2;

print(square_2.square(2));
print(square_2.square(3));

def main():
    test_square();
    test_positive_num();
    test_negative_num();

def test_square():
    try:
        assert square_2.square(2) == 4;
    except:
        print("2 sq != 4");

    try:
        assert square_2.square(3) == 9;
    except:
        print("sq 3 != 9");


def test_positive_num():
    assert square_2.square(2) == 4;
    assert square_2.square(3) == 9;

def test_negative_num():
    assert square_2.square(-2) == 4;
    assert square_2.square(-3) == 9;

def test_zero():
    assert square_2.square(0) == 0;

def test_str():
    with pytest.raises(TypeError):
        square_2.square("cat");


if __name__ == "__main__":
    main();