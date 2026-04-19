import math
from typing import Union

def zeroes(quadratic: tuple[float, float, float]) -> Union[tuple[float, float], float, None]:
    """Find the zeroes of a quadratic lol. input a b and c as fractions."""

    a,b,c=quadratic

    discriminant = b*b-4*a*c
    if discriminant<0:
        return
    elif discriminant==0:
        return -b/(2*a)
    else:
        return ((-b+discriminant)/(2*a), (-b-discriminant)/(2*a))

