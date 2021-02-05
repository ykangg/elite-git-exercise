def foo(number1, number2):
  return 0

def test_foo():
  number1 = 2
  number2 = 3
  result = foo(number1, number2)
  assert result == 5

if __name__ == '__main__':
  # This calls the test_foo function 
  # when we run from the command line
  test_foo()  