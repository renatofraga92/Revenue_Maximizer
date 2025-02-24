# Revenue_Maximizer
Python tool for optimizing pricing to maximize revenue using linear and exponential models, with sensitivity analysis and visualizations for pricing strategy analysis

# Revenue_Maximizer

## Overview
This repository contains two Python tools for optimizing pricing to maximize revenue based on different demand models: `Revenue_Maximizer_Linear_Model` and `Revenue_Maximizer_Exponential_Model`. These tools are designed for pricing strategy analysis but are restricted for use without explicit permission from the author.

### Revenue_Maximizer_Linear_Model
Revenue_Maximizer_Linear_Model is a Python tool designed to determine the optimal price that maximizes revenue based on two price-sales data points. It assumes a linear relationship between price and sales, using numerical optimization to find the best pricing strategy. This project is ideal for simple revenue optimization tasks in pricing analysis or economic modeling.

### Revenue_Maximizer_Exponential_Model
Revenue_Maximizer_Exponential_Model is a Python tool that optimizes pricing to maximize revenue using an exponential demand model. It takes two price-sales data points, fits an exponential curve (sales = a * exp(-b * price)), and determines the optimal price. Expected sales are rounded to the nearest integer for practical use. The tool includes sensitivity analysis and visualizations to explore the price-revenue relationship, ideal for pricing strategies with non-linear demand decay.

## Features

### Revenue_Maximizer_Linear_Model
- Input Validation: Ensures non-negative prices and sales, and prevents division by zero errors.
- Linear Demand Model: Calculates a linear demand function from two user-provided data points.
- Revenue Optimization: Uses SciPy's `minimize` function to find the price that maximizes revenue.
- Output: Provides the optimal price, expected sales, and maximum revenue.

### Revenue_Maximizer_Exponential_Model
- Input Validation: Ensures non-negative prices and sales, preventing invalid inputs.
- Exponential Model: Fits an exponential demand function to the data using SciPy's `curve_fit`.
- Revenue Optimization: Uses SciPy's `minimize` to find the price that maximizes revenue.
- Integer Sales: Rounds expected sales to the nearest whole number.
- Sensitivity Analysis: Evaluates revenue across a range of prices.
- Visualizations: Plots exponential demand and revenue curves with Matplotlib.

## How It Works

### Revenue_Maximizer_Linear_Model
1. The user inputs two pairs of price and sales data (e.g., price1 with sales1, price2 with sales2).
2. The code calculates the slope of the linear demand curve connecting these points.
3. A demand function is defined based on this linear relationship.
4. The revenue function (price × sales) is optimized using numerical methods, with bounds set to realistic price ranges (0 to twice the maximum input price).
5. Results are displayed: optimal price, expected sales, and maximum revenue.

### Revenue_Maximizer_Exponential_Model
1. The user enters two price-sales data pairs.
2. An exponential demand model is fitted to the data using curve fitting.
3. Revenue (price × sales) is optimized within bounds (0 to twice the maximum input price).
4. Expected sales are rounded to the nearest integer.
5. Results show the optimal price, integer sales, and maximum revenue.
6. Graphs display the demand and revenue curves, highlighting the optimal point.

## Requirements
- Python 3.x
- NumPy
- SciPy
- Matplotlib (for Revenue_Maximizer_Exponential_Model)

## Code Explanation

### Revenue_Maximizer_Linear_Model
- Input Collection: Gathers two price-sales pairs with error handling.
- Slope Calculation: Computes the linear slope between the data points.
- Demand Function: Defines sales as a linear function of price.
- Revenue Function: Calculates revenue, negated for optimization.
- Optimization: Uses `minimize` from SciPy with a starting point (average of input prices) and bounds.
- Results: Outputs the optimal price, sales, and revenue.

### Revenue_Maximizer_Exponential_Model
- Input Collection: Gathers two price-sales pairs with error handling.
- Exponential Model: Fits an exponential function (sales = a * exp(-b * price)) to the data.
- Revenue Function: Defines revenue, negated for optimization.
- Optimization: Applies `minimize` with bounds and a starting point (average of input prices).
- Integer Adjustment: Rounds expected sales to the nearest integer.
- Sensitivity Analysis: Computes revenues over a price range.
- Visualization: Plots demand and revenue curves with the optimal price marked.

## Limitations

### Revenue_Maximizer_Linear_Model
- Assumes a linear relationship between price and sales, which may not fit all real-world scenarios.
- Requires exactly two data points; additional points are not supported in this version.

### Revenue_Maximizer_Exponential_Model
- Requires exactly two data points; more points could refine the fit but aren't supported here.
- Assumes an exponential decay in demand, which may not fit all scenarios.
- Rounding sales may slightly alter the revenue from the theoretical maximum.

## License
This code is protected by copyright and is not licensed for use, modification, or distribution without explicit permission from the author. All rights reserved. Please contact renatofraga.rr@gmail.com for inquiries.

## Notes
- Visualizations for the exponential model will appear showing the demand and revenue curves.
- This repository combines both tools for convenience, but they can be used independently.
