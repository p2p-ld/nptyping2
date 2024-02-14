# nptyping2

> [!IMPORTANT]
> Help wanted! Calling all python typing understanders who know how variadic generics are supposed to work <3

nptyping, updated for [PEP 646](https://peps.python.org/pep-0646/)

Instead of 

```python
>>> from nptyping import NDArray, Int, Shape

>>> arr: NDArray[Shape["2, 2"], Int]
```

How about

```python
>>> from nptyping2 import NDArray, Shape

>>> arr: NDArray[Shape[2, 2], int]
```

nptyping was a lovely hack for a long time, simulating generics with a microsyntax
for array shapes and types before that was possible. As of python 3.11, it is possible!
And it's one of the specific motivations for PEP 646!

Additional features:
- [ ] Range syntax - specify a range of shapes like `Shape[(2,4), ...]`
