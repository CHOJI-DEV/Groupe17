
print("=================================================")
print("    STUDENT ROAD TRIP BUDGET CALCULATOR          ")
print("=================================================")
print("Please enter the trip details below.\n")

# --- 1. COLLECT DATA (INPUTS) ---

# STR (Strings)

destination = input("1. What is the destination of the trip? : ")
car = input("2. What is the car model used? : ")

# INT (Integers)
num_people = int(input("3. Total number of travelers (including driver)? : "))
days = int(input("4. Duration of the trip (in days)? : "))

# FLOAT (Decimal numbers)

dist = float(input("5. Total distance round trip (km)? : "))
consumption = float(input("6. Average car fuels consumption (L/100km)? : "))
fuel_price = float(input("7. Price of fuel per liter (CFA)? : "))

food_budget = float(input("8. Food budgets per person per day (CFA)? : "))
accommodation_total_cost = float(input("9. Total accommodation cost for the group (CFA)? : "))
misc_money_total = float(input("10. Budget for misc/fun activities for the group (CFA)? : "))

# BOOL (Boolean)

print("\nFor the next question, just press 'Enter' for NO, or type 'Yes' for YES.")
toll_road = bool(input("11. Does the route include tolls? : "))


# --- 2. PROCESS (CALCULATIONS) ---

# Calculate fuel needed: (Distance * Consumption) / 100
fuel_needed = (dist * consumption) / 100

# Total fuel cost
fuel_cost = fuel_needed * fuel_price

# Total food cost: Price * Days * People
total_food_cost = food_budget * days * num_people

# Grand Total Cost (Fuel + Food + Accommodation + Misc)
grand_total_cost = fuel_cost + total_food_cost + accommodation_total_cost + misc_money_total

# Cost per person (Division)
cost_per_person = grand_total_cost / num_people

# --- 3. SUMMARY SCREEN (OUTPUT) ---

print("\n\n")
print("=================================================")
print(f"        TRIP SUMMARY TO: {destination.upper()}")
print("=================================================")
print(f"Vehicle : {car}")
print(f"Duration : {days} days | Travelers : {num_people}")
print(f"Tolls Included : {toll_road}")
print("-------------------------------------------------")
print("ESTIMATED COST BREAKDOWN:")
print(f"- Fuel ({fuel_needed} L)         : {fuel_cost:.2f} CFA")
print(f"- Food (Total)           : {total_food_cost:.2f} CFA")
print(f"- Stay & Misc            : {accommodation_total_cost + misc_money_total:.2f} CFA")
print("-------------------------------------------------")
print(f" GRAND TOTAL TRIP COST   : {grand_total_cost:.2f} CFA")
print("=================================================")
print(f" COST PER PERSON         : {cost_per_person:.2f} CFA ")
print("=================================================")
