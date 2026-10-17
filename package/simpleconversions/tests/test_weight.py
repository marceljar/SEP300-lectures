from simpleconversions.weight import kg_to_lb, lb_to_kg

def test_roundtrip_weight():
    kg = 3.0
    lb = kg_to_lb(kg)
    assert abs(lb_to_kg(lb) - kg) < 1e-9

def test_known_value():
    assert abs(kg_to_lb(1.0) - 2.20462262185) < 1e-9
