## Problem Description

Some review from Programming 2.

### Exercise 1: Code improvement

In the file `hog.py`:

1. Apply the Python coding standard.  Fix names of variables and the spacing in the code.
2. Write (or improve) the docstring comments in the methods, so they are correctly formatted and document the parameters and return values.  How to write docstring comments is discussed in class on Week 1.

Optional: use the [flake8][flake8] utility to check the code. (`pip3 install flake8`) We will use flake8 later in the course.

**Commit and push** your code to Github when done.


### Exercise 2: Write a Test Plan

We want to thoroughly test the `roll_dice` function. 

Add 1 line to the table below to describe in words a **very important test
case** for the `roll_dice` function that is not tested yet.  
Review the comments in `roll_dice` that describe what the function should do.

| Test Case                               | Expected Result        |
|:----------------------------------------|------------------------|
| Roll a single dice one time.            | The face value of the dice |
| Roll two dice, none of them roll a one. | sum of the dice values. |
| Roll dice with ones in it.              | The values show result with one.  |
| Test call_count on dice.                | The result of everytime the dice roll |

Note: This table uses Markdown format.

**Commit and push** your changes to README.md to Github.


### Exercise 3: Write Tests

Write one or more tests in file `hog_test.py` for the test case you added. 

We can't use the `six_sided` dice in tests, because the results would be random.

So, use a mock object (as Aj. Jittat introduced in Programming 2) to
create a "programmable" dice with known values.  This is done in the 
sample code in `hog_test.py`;  use that code as example.

**Important:** Write tests to test what the code **should do**,
not what it **actually does** (the code may be wrong!).

To run the tests:
```bash
python3 -m unittest hog_test.py
```
To see the result of each test (and the docstring!):
```bash
python3 -m unittest -v hog_test.py
```


### Exercise 4: Fix the Bugs

Now that you have unit tests that show there's a bug in `roll_dice` (Exercise 3)
fix the bug(s).  Then run the tests again to verify your code. 

## What to Submit

Push your code to Github when done.


## Using Mock Objects in Tests

To test the `roll_dice` function, we need to create a `dice` function
that returns known values. We can't use a die (dice) that returns random values,
because our test code would not know what values were rolled.

We can create a dice function that returns known values for our tests
using either:

1. Write our own dice function or an *Iterator* that returns known values
2. Use a Mock object

Mock objects are useful for testing and covered in Programming 2.
A mock object can be "programmed" to do whatever you want,
and you can ask it how many times it was called.

So, we'll use a Mock object here.

```python
from unittest.mock import Mock

dice = Mock()
# dice that always return 5
dice.return_value = 5
dice()
5
dice()
5
# how many times was this function called?
dice.call_count
2

# make dice return different values each time
dice.side_effect = [3, 0, 6, 1]
dice()
3
dice()
0
dice()
6
dice()
1
dice.call_count   # total call count since Mock was created
6
# if you exhaust the pre-programmed values, it raises StopIteration error
dice()
StopIteration
Traceback (most recent call last)
   ...
```

Now use a Mock to test rolling dice:

```python
>>> mock_dice = Mock()
>>> mock_dice.side_effect = [2, 3, 6, 1, 5]
>>> result = roll_dice(3, dice=mock_dice)
>>> result
11
>>> mock_dice.call_count
3
>>> roll_dice(2, dice=mock_dice)  # rolls 1 and 5
1                                 # special rule about rolling 1
>>> mock_dice.call_count
5                                 # total call count: 3 + 2
```

## References

* [Mock Objects][python-mock-objects] in Python 3.8 docs.
* [Understanding the Python Mock Object Library](https://realpython.com/python-mock-library/) on RealPython.
* [Unit Testing and Mock Objects](https://classroom.google.com/c/MjUxNzA2Mjk0MTgy/m/MzA2MzU4NDU1NDYx/details) from Programming 2 (Aj. Jittat presentation).

[python-mock-objects]: https://docs.python.org/3.8/library/unittest.mock.html
[flake8]: https://flake8.pycqa.org
