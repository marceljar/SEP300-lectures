from simpleconversions.distance import cm_to_in, in_to_cm

def test_roundtrip_cm_in():
    cm = 12.7         # 5 inches
    inches = cm_to_in(cm)
    assert abs(in_to_cm(inches) - cm) < 1e-12

def test_known_value():
    assert abs(cm_to_in(2.54) - 1.0) < 1e-12

