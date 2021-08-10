## Money

Write a **Money** class that represents money with a value and a currency.

Write the methods shown in the UML class diagram and described below.

Write the best, cleanest code that you can.
* code **formatted** according to the Python standard.
* use meaningful variable names.
* each method has a 1-sentence docstring that describes what is does.

Example:
```python
>>> m1 = Money(10)    # same as Money(10, 'Baht')
>>> m2 = Money(1000)
>>> print(m1)
10 Baht
>>> print(m2)
1,000 Baht
>>> m1 > m2
False
>>> m2 > m1
True
>>> m1 > m1
False
>>> m3 = Money(10, 'Baht')
>>> m1 == m3
True
>>> d1 = Money(10, 'Dollar')
>>> m1 == d1
False
# Addition
>>> print(m1 + m2)
1,010 Baht
>>> print(m1 + d1)
ValueError: Currency must be same
```

![Money UML class diagram](money.png)

Write or complete these methods:

| Method      | Description                   |
|:------------|:------------------------------|
| `__init__`  | Initialize a new money object with a value and currency (default is "Baht").(1) |
| `__eq__`    | Test for equality. True only if objects have the same value and currency. |
| `__add__`   | Add two money objects and return result as a new Money object. (3) |
| `__gt__`    | Test `self > other`. First compare currency, then value. (4) |
| `__ge__`    | (Optional) Test `self >= other`. Use methods you already wrote. (4) |
| `__str__`   | Return string form of money, e.g. 0.25 Baht or 10 Baht. (5) |
| `currency`  | Property to get the currency. (2) |
| `value`     | Property to get the value. (2)    |


1. The constructor has parameters `value` and `currency`. The currency parameter has a default value 'Baht'.
2. Money is **immutable**. Name the attributes as shown in the UML diagram and write read-only properties to get the value and currency.
3. Write `__add__` that adds two money objects and returns the sum, provided they have the same currency.  
   - when you write `m1 + m2`, Python invokes `m1.__add__(m2)`, which should return the result as a new Money object.
   - if `m1` and `m2` (being added) have different currencies, raise a ValueError with the message "Currency must be same".
4. Money objects can be compared using `m1 > m2`.  The rule for comparison is: first compare the currency strings ('Euro' is greater than 'Baht').  If the currency is the same, then compare the value ('10 Baht' > '5 Baht').  
   - Write a `__gt__` method to test `m1 > m2`.  `m1 > m2` invokes `m1.__gt__(m2)`.
   - It returns True of False, of course.
   - Optional: write `__ge__` that tests `m1 >= m2`. Use your other methods instead of writing duplicate code.
5. `__str__` should return a string as follows:
   - if the value is an integer, return it as integer, such as "12 Baht"
   - if value is non-integer, return 2 decimal places, such as "0.39 Baht"
   - if absolute value is 1000 or more, include commas, such as "12,345 Baht"
   - Hint: in f-strings write a colon and then a format `{value:.2f}` or `{value:.,2f}`
6. Write a brief **docstring** comment in each method that describes its purpose. Don't document the parameters and return value. The docstring should be one complete sentence.


## Testing

The starter code contains doctest comments.  You can run the tests using either of these commands:
```shell
python3 -m doctest money.py
# to see more detailed results
python3 -m doctest -v money.py
```

The final `money_test.py` contains pytest-style tests.  Github will run these automatically when you push your code.  You can run them on your computer using:
```shell
pytest money_test.py
```
If your Python does not have `pytest` then install it using `pip3 intall pytest`.


## What to Submit

Push your code to Github.
