import price_info

def test_total_cost_shopping():
    total_cost = price_info.total_cost_shopping()
    assert (total_cost == 46.75)

def test_cost_of_fruit():
    cost = price_info.cost_of_fruits('orange', 10)
    assert (cost == 14.0)
