# CS2006Python1 #

## Dependencies ##

This library requires the unittest module which is part of the standard Python library.

If it's not installed, you can install it using:

```pip install unittest```

## Interactive Use ##

Import the libraries using:

```from IntricateInteger import IntricateInteger # Assuming IntricateInteger.py is in the current directory```
```from IntricateIntegers import IntricateIntegers # Assuming IntricateIntegers.py is in the current directory```

Create an IntricateInteger object:

```x = IntricateInteger(2, 3, 2)  # value, modulus, multiplier```
```print(x)  # Output: <2 mod 3 | 2>```

Iterate over IntricateIntegers object:

```for x in IntricateIntegers(3,2):```
```     print(x)```

Output:
```<0 mod 3 | 2>```
```<1 mod 3 | 2>```
```<2 mod 3 | 2>```

## Running Tests ##

Run the tests from the command line using:

```python test_intricate_integer.py```
