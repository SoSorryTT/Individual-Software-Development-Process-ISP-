"""
A Money class with operator overloading for comparisons (>, >=) and equality.
Write __gt__ (a > b) and __ge__ (a >= b) and get < and <= for free,
since Python reverses the comparison automatically when only __gt__
and __ge__ are present.
"""


class Money:
    """
    TODO replace this line with a class docstring in the correct format.
    It should describe what the class represents and what it does.
    A class used to represent Money.
    value
        Return the value of the money
    
    Examples:
    >>> m = Money(1000)
    >>> m.value
    1000
    >>> m.currency
    'Baht'
    >>> str(m)            # don't print decimal part if value is an integer
    '1,000 Baht'
    >>> m2 = Money(1000)
    >>> m == m2
    True
    >>> m2 = Money(100)
    >>> m == m2
    False
    >>> sum = m + m2
    >>> str(sum)
    '1,100 Baht'
    >>> m > m2
    True
    >>> m2 > m
    False
    >>> d = Money(0.5, "USD")
    >>> str(d)                # value is not integer, so print 2 decimal digits
    '0.50 USD'
    >>> d2 = Money(100, 'USD')
    >>> m2 == d2              # value is same but currencies are different
    False
    """

    # TODO complete the constructor -- fix the parameters, too.
    def __init__(self, value, currency="Bath"):
        """Initialize a new money object with given value and currency."""
        self._value = value
        self._currency = currency
  
    @property
    def value(self):
        """The value of this money object without the currency."""
        return self._value

    @property
    def currency(self):
        """The type of the money object currency."""
        return self._currency

    def __str__(self):
        return str(self.value) + " " + self.currency

    def __add__(self, obj):
        self._value = self.value + obj.value
        return self._value

    def __eq__(self, obj):
        if (self.value == self.value and
                self.currency == obj.currency):
            return True
        else:
            return False

    def __gt__(self, obj):
        if self.value > obj.value:
            return True
        else:
            return False

m = Money(20)
print(m)