from scipy.optimize import minimize
import numpy as np

# Prompt user to input price and sales data for two periods
print("Enter price and sales data for two different time periods\n")

# Collect and validate input
while True:
    try:
        price1 = float(input("Enter the first price: "))
        sales1 = float(input("Enter the sales at this price: "))
        price2 = float(input("Enter the second price: "))
        sales2 = float(input("Enter the sales at this price: "))
        
        # Ensure inputs are non-negative
        if min(price1, sales1, price2, sales2) < 0:
            raise ValueError("All values must be non-negative.")
        # Prevent division by zero in slope calculation
        if sales1 == sales2:
            raise ValueError("Sales values must differ to define a relationship.")
        break
    except ValueError as e:
        print(f"Error: {e}. Please enter valid numbers.")

# Calculate the slope of the linear relationship between price and sales
slope = (price2 - price1) / (sales2 - sales1)

# Define the demand function based on price
def demand(price):
    return sales2 + (price - price2) / slope

# Define the revenue function (negated for optimization)
def revenue(price):
    return -price * demand(price)

# Set bounds for the price (0 to twice the maximum input price)
price_bounds = [(0, max(price1, price2) * 2)]

# Find the optimal price using numerical optimization
result = minimize(revenue, (price1 + price2) / 2, bounds=price_bounds)

# Calculate key outputs
optimal_price = result.x[0]
optimal_sales = demand(optimal_price)
optimal_revenue = optimal_price * optimal_sales

# Display the results
print("\nOptimized Results:")
print(f"Optimal price: {optimal_price:.2f}")
print(f"Expected sales: {optimal_sales:.2f}")
print(f"Expected revenue: {optimal_revenue:.2f}")
