def divide(a: float, b: float) -> float:
    ### Assumptions:
    ###  - 'b' is never zero (caller ensures this).
    ###  - Both a and b are finite floats (not NaN or inf).
    ###  - Precision loss is acceptable for small denominators.
    
    return a / b