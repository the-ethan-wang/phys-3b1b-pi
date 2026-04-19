import math
from typing import Union
from fractions import Fraction

def zeroes(quadratic: tuple[int, int, Fraction]) -> Union[tuple[Fraction, Fraction], Fraction, None]:
    """Find the zeroes of a quadratic lol. input a b and c as fractions."""

    a,b,c=quadratic

    discriminant = b*b-4*a*c
    if discriminant<0:
        return
    elif discriminant==0:
        return Fraction(-b, 2*a)
    else:
        return (Fraction(-b+math.sqrt(discriminant), ))