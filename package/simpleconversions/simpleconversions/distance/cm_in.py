_CM_PER_IN = 2.54
_IN_PER_CM = 1.0 / _CM_PER_IN

def cm_to_in(cm: float) -> float:
    """Convert centimeters to inches."""
    return cm * _IN_PER_CM

def in_to_cm(inches: float) -> float:
    """Convert inches to centimeters."""
    return inches * _CM_PER_IN
