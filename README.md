# Differential-Calculus
Its Calculus, Differential Calculus a.k.a DiffCalculus, a Python 3.x package for Implementing Differentiation in Python

It is also available on [PyPI](https://pypi.org/project/DiffCalculus/)

## Installation
***Note :- Requires Python Version 3.x***

**If there are 2 or more versions of Python installed in your system (which mostly occurs in UNIX/Linux systems) then please run any one of the commands in the BASH/ZSH Shell \:-**
```bash
$ pip3 install DiffCalculus
```
```bash
$ python3 -m pip install DiffCalculus
```

**If there is only Python 3.x installed in your system like in Windows systems then please run any one of commands in the Command Prompt \:-**
```cmd
>pip install DiffCalculus
```
```cmd
>python -m pip install DiffCalculus
```
## Quick Guide

## Examples
***Note :- Differentiation of all the functions happens with respect to the variable x only.***
### 1. Differentiation of Simple Functions :-

a) Differentiate sin(x)
```python3
import diffcalculus as dc

sin = dc.functions.sin()
print(dc.differentiate(sin))
```

b) Differentiate sin⁻¹(x)
```python3
import diffcalculus as dc

sin_inv = dc.functions.sinInv()
print(dc.differentiate(sin_inv))
```

c) Differentiate x² + 2x + 1
```python3
import diffcalculus as dc

poly = dc.functions.polynomial([1, 2], constant=1)
print(dc.differentiate(poly))
```

### 2. Differentiation of Complex Functions :-
a) Differentiate sin(sqrt(x))
```python3
import diffcalculus as dc

sqrt_x = dc.functions.x()
func = dc.functions.sin(sqrt_x)

print(dc.differentiate(func))
```

b) Differentiate ln(3x³ + 2x² + 5x)
```python3
import diffcalculus as dc

poly = dc.functions.polynomial([3, 2, 5])
func = dc.functions.log(poly)

print(dc.differentiate(func))
```

c) Differentiate sin(x) + cos(x)
```python3
import diffcalculus as dc

sin = dc.functions.sin()
cos = dc.functions.cos()
func = a+b

print(dc.differentiate(func))
```

### 3. Differentiation of a Function at a particular point :-
a) **Differentiate sin(x) at π/2**	_Result Should be 0_
```python3
import diffcalculus as dc
from math import pi

sin, point = dc.functions.sin(), pi/2

print(dc.differentiateAtPoint(sin, point))
```

b) **Differentiate sqrt(x) at 4**	_Result Should be 0.25_
```python3
import diffcalculus as dc

sqrt_x, point = dc.functions.x(), 4

print(dc.differentiateAtPoint(sqrt_x, point))
```

##\'substitute\' Function Implementation \:-
**Besides Differentiation of Functions and also their Differentiation at a particular point; The Package also contains a 'substitute' Function which substitutes a value for the variable x in the given function.**
```python3
import diffcalculus as dc
from math import pi

sin, point = dc.functions.sin(), pi/2

print(dc.substitute(sin, point))
```
