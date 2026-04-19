

def zeroes(a,b,c) -> tuple[int, int]:
    """Assumes discriminant is a perfect square. Doesn't care if it's a double root lol."""
    discr = b**2-(4*a*c)
    denominator=(2*a)
    return (
        (-b-discr)/denominator,
        (-b+discr)/denominator
    )

