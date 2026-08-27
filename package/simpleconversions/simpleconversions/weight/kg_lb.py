_KG_PER_LB = 0.45359237
_LB_PER_KG = 1 / _KG_PER_LB

def kg_to_lb(kg: float) -> float:
    """Convert kilograms to pounds."""
    return kg * _LB_PER_KG

def lb_to_kg(lb: float) -> float:
    """Convert pounds to kilograms."""
    return lb * _KG_PER_LB
