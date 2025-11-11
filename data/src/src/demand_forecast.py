def forecast_demand(base_price, demand_score, competitor_price):
    """
    Simple demand forecast model.
    Higher demand_score increases sales,
    higher competitor_price gives advantage.
    """
    price_factor = max(0, (competitor_price - base_price) / competitor_price)
    demand = demand_score * (1 + price_factor)
    return round(demand, 2)
