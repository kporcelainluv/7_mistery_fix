# Quadratic equations solver
The program helps to solve quadratic equasions

# How to use

Function get_roots(a, b, c) returns roots for the quadratic equation ax**2 + bx + c = 0

Function output:

* root1, root2 if discriminant > 0
* root1, None if discriminant == 0
* None, None if discriminant < 0


# How to launch

Example:

```
from quadratic_equation import get_roots
root1, root2 = get_roots(1, 2, 3)
```

Scrit requires installed Python interpretator, version 3.5

Linux launch:

```bash
python tests.py # you man need to call python3 instead python, depends on one's operating system settings
```

The launch on Windows is done in similar way.

# Project aims

The code is developed for educational purposes. Check web-development course ― DEVMAN.org
