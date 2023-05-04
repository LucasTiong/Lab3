import lab2.bmi as bmi

def test_bmi_over_weight():
    weight, height = 100, 1.40
    result = bmi.calculate_bmi(weight, height)
    assert(result == -1)
def test_bmi_normal_weight():
    weight, height = 57, 1.73
    result = bmi.calculate_bmi(weight, height)
    assert(result == -1)
def test_bmi_under_weight():
    weight, height = 50, 1.80
    result = bmi.calculate_bmi(weight, height)
    assert(result == -1)