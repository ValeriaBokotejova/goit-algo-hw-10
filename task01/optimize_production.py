import pulp as lp
from colorama import Fore, Style

# Creating a linear programming problem for maximization
prob = lp.LpProblem("Maximize_Production", lp.LpMaximize)

# Variables - number of "Lemonade" and "Fruit Juice" to be produced
lemonade = lp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
fruit_juice = lp.LpVariable('Fruit_Juice', lowBound=0, cat='Continuous')

# Objective function - maximize total number of products
prob += lemonade + fruit_juice, "Total_Production"

# Resource constraints
prob += 2*lemonade + 1*fruit_juice <= 100, "Water_Limit"
prob += 1*lemonade <= 50, "Sugar_Limit"
prob += 1*lemonade <= 30, "Lemon_Juice_Limit"
prob += 2*fruit_juice <= 40, "Fruit_Puree_Limit"

# Solving the problem
prob.solve()

# Outputting the results
print(f"{'Optimization Results':=^40}")
print(f"{Fore.GREEN}Status: {lp.LpStatus[prob.status]}{Style.RESET_ALL}")
print(f"Lemonade: {Fore.YELLOW}{lemonade.varValue:.2f} units{Style.RESET_ALL}")
print(f"Fruit Juice: {Fore.YELLOW}{fruit_juice.varValue:.2f} units{Style.RESET_ALL}")
print(f"Total number of products: {Fore.CYAN}{lp.value(prob.objective):.2f} units{Style.RESET_ALL}")
print("="*40)
