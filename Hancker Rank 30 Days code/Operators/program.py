def solve(meal_cost,tip_percent,tax_percent):
    tip = (tip_percent/100.)* meal_cost
    tax = (tax_percent/100.)* meal_cost
    total_cost = int(round(meal_cost+tip+tax))
    print(total_cost)
meal_cost = 12.00
tip_percent = 20
tax_percent = 8
solve(meal_cost,tip_percent,tax_percent)