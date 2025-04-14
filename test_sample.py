# def add(a, b):
#     return a + b
#
# def test_add():
#     assert add(2, 3) == 5
#
# def test_example():
#     assert 2 + 2 == 4  # ✅ Pass
#     assert "hello".upper() == "HELLO"  # ✅ Pass
#     assert len([1, 2, 3]) == 3  # ❌ Fail

# import pytest
# @pytest.fixture
# def address():  # This is a fixture function
#     return {"name": "Tufan", "age": 30}  # Returns a dictionary
#
# def test_user1(address):  # sample_data is automatically passed
#     assert address["name"] == "Tufan"  # Checks if name is 'Tufan'
#
# def test_user2(address):  # Again, sample_data is passed automatically
#     assert address["age"] == 30  # Checks if age is 30


# import pytest
# from Practice import Calculater
# @pytest.fixture
# #
# def ght():
#     return Calculater
#
# def test_add(ght):
#     assert ght.add(2,3) ==5
#
# def test_subtract(ght):
#     assert ght.subtract(5,4) ==1
#
# def test_multiply(ght):
#     assert ght.multiply(4,6) ==24
#
# def test_devide(ght):
#     assert ght.devide(4,2)==2


# import pytest
# @pytest.mark.parametrize("a,b,result",[(1,5,6),(23,25,48),(45,46,91)])
# def test_add(a,b,result):
#     assert (a+b)==result

# import pytest
# from Practice import Calculater
# @pytest.mark.parametrize("a,b,result",[(4,6,24),(3,9,27),(9,4,36)])
# def test_multi(a,b,result):
#     assert Calculater.multiply(a,b)==result


