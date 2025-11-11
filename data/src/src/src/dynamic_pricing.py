from demand_forecast import forecast_demand

def calculate_dynamic_price(base_price, competitor_price, inventory, demand_score):
    """
    Calculates dynamic price based on demand, competitor price, and inventory levels.
    """
    demand = forecast_demand(base_price, demand_score, competitor_price)
    
    # Adjust price based on inventory
    if inventory < 20:
        price_adjustment = 1.2  # Increase price if low stock
    elif inventory > 50:
        price_adjustment = 0.9  # Decrease price if overstock
    else:
        price_adjustment = 1.0

    dynamic_price = base_price * demand * price_adjustment
    return round(dynamic_price, 2)
