from data_loader import load_product_data
from dynamic_pricing import calculate_dynamic_price

def main():
    products = load_product_data("data/sample_products.csv")
    
    print("Dynamic Pricing Dynamo\n")
    print("Product\tBase Price\tCompetitor Price\tInventory\tDynamic Price")
    
    for _, row in products.iterrows():
        dynamic_price = calculate_dynamic_price(
            base_price=row['base_price'],
            competitor_price=row['competitor_price'],
            inventory=row['inventory'],
            demand_score=row['demand_score']
        )
        print(f"{row['product_name']}\t{row['base_price']}\t\t{row['competitor_price']}\t\t{row['inventory']}\t\t{dynamic_price}")

if __name__ == "__main__":
    main()
