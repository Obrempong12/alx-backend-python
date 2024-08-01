#!/usr/bin/env python3

"""This func adds annotations for the func beneath


```python
def element_length(lst):
    return [(i, len(i)) for i in lst]
```
"""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    This func takes a list of sequences and returns a list of tuples
    where each tuple contains a sequence and its length.

    Args:
        lst (Iterable[Sequence]): A list of sequences

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
        a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
