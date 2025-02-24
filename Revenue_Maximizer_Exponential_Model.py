from scipy.optimize import minimize, curve_fit
import numpy as np
import matplotlib.pyplot as plt

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
        # Prevent identical sales to ensure a meaningful fit
        if sales1 == sales2:
            raise ValueError("Sales values must differ to define a relationship.")
        break
    except ValueError as e:
        print(f"Error: {e}. Please enter valid numbers.")

# Data points
prices = np.array([price1, price2])
sales = np.array([sales1, sales2])

# --- Exponential Model ---
# Define an exponential demand function: sales = a * exp(-b * price)
def exp_demand(price, a, b):
    return a * np.exp(-b * price)

# Fit exponential model to the two data points
params, _ = curve_fit(exp_demand, prices, sales, p0=[max(sales1, sales2), 0.1])

# Exponential demand and revenue functions
def exp_demand_fit(price):
    return exp_demand(price, *params)

def exp_revenue(price):
    return -price * exp_demand_fit(price)

# --- Optimization ---
# Set bounds for price optimization
price_bounds = [(0, max(price1, price2) * 2)]

# Optimize the exponential model
exp_result = minimize(exp_revenue, (price1 + price2) / 2, bounds=price_bounds)

# Calculate results
exp_opt_price = exp_result.x[0]
exp_opt_sales = round(exp_demand_fit(exp_opt_price))  # Round sales to the nearest integer
exp_opt_revenue = exp_opt_price * exp_opt_sales

# --- Sensitivity Analysis ---
price_range = np.linspace(0, max(price1, price2) * 1.5, 100)
exp_revenues = [price * exp_demand_fit(price) for price in price_range]

# --- Display Results ---
print("\nExponential Model Results:")
print(f"Optimal price: {exp_opt_price:.2f}")
print(f"Expected sales: {exp_opt_sales}")
print(f"Expected revenue: {exp_opt_revenue:.2f}")

# --- Visualization ---
plt.figure(figsize=(12, 6))

# Plot demand curve
plt.subplot(1, 2, 1)
plt.plot(price_range, [exp_demand_fit(p) for p in price_range], label='Exponential Demand', color='green')
plt.scatter(prices, sales, color='red', label='Data Points')
plt.axvline(exp_opt_price, color='green', linestyle='--', label=f'Optimal Price ({exp_opt_price:.2f})')
plt.xlabel('Price')
plt.ylabel('Sales')
plt.title('Exponential Demand Curve')
plt.legend()

# Plot revenue curve (sensitivity analysis)
plt.subplot(1, 2, 2)
plt.plot(price_range, exp_revenues, label='Exponential Revenue', color='green')
plt.axvline(exp_opt_price, color='green', linestyle='--', label=f'Max Revenue ({exp_opt_revenue:.2f})')
plt.xlabel('Price')
plt.ylabel('Revenue')
plt.title('Exponential Revenue Curve')
plt.legend()

plt.tight_layout()
plt.show()
